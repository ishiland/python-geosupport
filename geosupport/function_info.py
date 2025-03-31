from csv import DictReader
import glob
from os import path
from typing import Dict, List, Optional, Any, Tuple, cast

from .config import FUNCTION_INFO_CSV, FUNCTION_INPUTS_CSV, WORK_AREA_LAYOUTS_PATH


class FunctionDict(dict):
    alt_names: Dict[str, str]  # Declare as a class attribute.

    def __init__(self) -> None:
        super().__init__()
        self.alt_names = (
            {}
        )  # Now this assignment doesn't include an inline type declaration.

    def __getitem__(self, name: str) -> Any:
        name = str(name).strip().upper()
        if self.alt_names and name in self.alt_names:
            name = self.alt_names[name]
        return super().__getitem__(name)

    def __contains__(self, name: object) -> bool:
        name_str = str(name).strip().upper()
        return (name_str in self.alt_names) or super().__contains__(name_str)


def load_function_info() -> FunctionDict:
    functions = FunctionDict()
    alt_names: Dict[str, str] = {}

    with open(FUNCTION_INFO_CSV) as f:
        csv_reader = DictReader(f)
        for row in csv_reader:
            row = cast(Dict[str, Any], dict(row))
            function = row["function"]
            for k in MODES:
                if row.get(k):
                    row[k] = int(row[k])
                else:
                    row[k] = None

            if row.get("alt_names"):
                row["alt_names"] = [n.strip() for n in row["alt_names"].split(",")]
            else:
                row["alt_names"] = []  # List[str]

            for n in row["alt_names"]:
                alt_names[n.upper()] = function

            row["inputs"] = []  # List[Any]
            functions[function] = row

    functions.alt_names = alt_names

    with open(FUNCTION_INPUTS_CSV) as f:
        csv_reader = DictReader(f)
        for row in csv_reader:
            row = cast(Dict[str, Any], dict(row))
            if row.get("function"):
                functions[row["function"]]["inputs"].append(
                    {"name": row["field"], "comment": row["comments"]}
                )

    return functions


def list_functions() -> str:
    s_list: List[str] = sorted(
        [
            "%s (%s)" % (function["function"], ", ".join(function["alt_names"]))
            for function in FUNCTIONS.values()
        ]
    )
    s_list = ["List of functions (and alternate names):"] + s_list
    s_list.append(
        "\nCall a function using the function code or alternate name using "
        "Geosupport.<function>() or Geosupport['<function>']()."
        "\n\nExample usage:\n"
        "    from geosupport import Geosupport\n"
        "    g = Geosupport()\n"
        "    # Call address using the alternate name.\n"
        "    g.address(house_number=125, street_name='Worth St', borough_code='Mn')\n"
        "    # Call function 3 using the function code.\n"
        "    g['3']({'borough_code': 'MN', 'on': '1 Av', 'from': '1 st', 'to': '9 st'})\n"
        "\nUse Geosupport.help(<function>) or Geosupport.<function>.help() "
        "to read about a specific function."
    )
    return "\n".join(s_list)


def function_help(function: str, return_as_string: bool = False) -> Optional[str]:
    func_info: Dict[str, Any] = FUNCTIONS[function]
    s_parts: List[str] = [
        "",
        "%s (%s)" % (func_info["function"], ", ".join(func_info["alt_names"])),
        "=" * 40,
        func_info["description"],
        "",
        "Input: %s" % func_info["input"],
        "Output: %s" % func_info["output"],
        "Modes: %s" % ", ".join([m for m in MODES if func_info[m] is not None]),
        "\nInputs",
        "=" * 40,
        "\n".join(["%s - %s" % (i["name"], i["comment"]) for i in func_info["inputs"]]),
        "\nReference",
        "=" * 40,
        func_info["links"],
        "",
    ]
    s: str = "\n".join(s_parts)
    if return_as_string:
        return s
    else:
        print(s)
        return None


def input_help() -> str:
    s_parts: List[str] = [
        "\nThe following is a full list of inputs for Geosupport. "
        "It has the full name (followed by alternate names).",
        "To use the full names, pass a dictionary of values to the "
        "Geosupport functions. Many inputs also have alternate names "
        "in parentheses, which can be passed as keyword arguments as well.",
        "\nInputs",
        "=" * 40,
    ]
    for i in INPUT:
        s_parts.append("%s (%s)" % (i["name"], ", ".join(i["alt_names"])))
        s_parts.append("-" * 40)
        s_parts.append("Functions: %s" % i["functions"])
        s_parts.append("Expected Values: %s\n" % i["value"])
    return "\n".join(s_parts)


def load_work_area_layouts() -> Tuple[Dict[str, Dict[str, Any]], List[Dict[str, Any]]]:
    work_area_layouts: Dict[str, Dict[str, Any]] = {}
    inputs: List[Dict[str, Any]] = []

    for csv_file in glob.glob(path.join(WORK_AREA_LAYOUTS_PATH, "*", "*.csv")):
        directory = path.basename(path.dirname(csv_file))
        if directory not in work_area_layouts:
            work_area_layouts[directory] = {}

        layout: Dict[str, Any] = {}
        name = path.basename(csv_file).split(".")[0]

        if "-" in name:
            functions_part, mode = name.split("-")
            mode = "-" + mode
        else:
            functions_part = name
            mode = ""

        functions_list = functions_part.split("_")
        for function in functions_list:
            work_area_layouts[directory][function + mode] = layout

        with open(csv_file) as f:
            rows = DictReader(f)
            for row in rows:
                row = cast(Dict[str, Any], dict(row))
                name_field = row["name"].strip().strip(":").strip()
                parent = row["parent"].strip().strip(":").strip()
                if parent and parent in layout and "i" in layout[parent]:
                    layout[parent] = {parent: layout[parent]}
                alt_names = [n.strip() for n in row["alt_names"].split(",") if n]
                v = {
                    "i": (int(row["from"]) - 1, int(row["to"])),
                    "formatter": row["formatter"],
                }
                if parent:
                    layout[parent][name_field] = v
                else:
                    layout[name_field] = v
                for n in alt_names:
                    layout[n] = v
                    layout[n.upper()] = v
                    layout[n.lower()] = v
                if directory == "input":
                    inputs.append(
                        {
                            "name": name_field,
                            "alt_names": alt_names,
                            "functions": row["functions"],
                            "value": row["value"],
                        }
                    )

    return work_area_layouts, inputs


MODES: List[str] = ["regular", "extended", "long", "long+tpad"]
AUXILIARY_SEGMENT_LENGTH: int = 500
FUNCTIONS = load_function_info()
WORK_AREA_LAYOUTS, INPUT = load_work_area_layouts()
