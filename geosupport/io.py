from functools import partial
from typing import Any, Callable, Dict, List, Optional, Tuple, Union, cast

from .config import BOROUGHS
from .error import GeosupportError
from .function_info import FUNCTIONS, AUXILIARY_SEGMENT_LENGTH, WORK_AREA_LAYOUTS


def list_of(length: int, callback: Callable[[str], Any], v: str) -> List[Any]:
    output: List[Any] = []
    i = 0
    # While the next entry isn't blank
    while v[i : i + length].strip() != "":
        output.append(callback(v[i : i + length]))
        i += length

    return output


def list_of_items(length: int) -> Callable[[str], List[str]]:
    return partial(list_of, length, lambda v: v.strip())


def list_of_workareas(name: str, length: int) -> Callable[[str], List[Dict[str, Any]]]:
    return partial(
        list_of, length, lambda v: parse_workarea(WORK_AREA_LAYOUTS["output"][name], v)
    )


def list_of_nodes(v: str) -> List[List[List[str]]]:
    return list_of(160, lambda w: list_of(32, list_of_items(8), w), v)


def borough(v: Optional[Union[str, int]]) -> str:
    if v:
        v2 = str(v).strip().upper()

        if v2.isdigit():
            return str(v2)

        if v2 in BOROUGHS:
            return str(BOROUGHS[v2])

        raise GeosupportError("%s is not a valid borough" % v)
    else:
        return ""


def function(v: str) -> str:
    v = str(v).upper().strip()
    if v in FUNCTIONS:
        v = FUNCTIONS[v]["function"]
    return v


def flag(true: str, false: str) -> Callable[[Optional[Union[bool, str]]], str]:
    def f(v: Optional[Union[bool, str]]) -> str:
        if type(v) == bool:
            return true if v else false

        if v:
            return str(v).strip().upper()[:1]
        else:
            return false

    return f


FORMATTERS: Dict[str, Any] = {
    # Format input
    "function": function,
    "borough": borough,
    # Flags
    "auxseg": flag("Y", "N"),
    "cross_street_names": flag("E", ""),
    "long_work_area_2": flag("L", ""),
    "mode_switch": flag("X", ""),
    "real_streets_only": flag("R", ""),
    "roadbed_request_switch": flag("R", ""),
    "street_name_normalization": flag("C", ""),
    "tpad": flag("Y", "N"),
    # Parse certain output differently
    "LGI": list_of_workareas("LGI", 53),
    "LGI-extended": list_of_workareas("LGI-extended", 116),
    "BINs": list_of_workareas("BINs", 7),
    "BINs-tpad": list_of_workareas("BINs-tpad", 8),
    "intersections": list_of_workareas("INTERSECTION", 55),
    "node_list": list_of_nodes,
    # Census Tract formatter
    "CT": lambda v: "" if v is None else v.replace(" ", "0"),
    # Default formatter
    "": lambda v: "" if v is None else str(v).strip().upper(),
}


def get_formatter(name: str) -> Callable:
    if name in FORMATTERS:
        return FORMATTERS[name]
    elif name.isdigit():
        return list_of_items(int(name))
    return lambda v: "" if v is None else str(v).strip().upper()


def set_mode(mode: Optional[str]) -> Dict[str, bool]:
    flags: Dict[str, bool] = {}
    if mode:
        if mode == "extended":
            flags["mode_switch"] = True
        if "long" in mode:
            flags["long_work_area_2"] = True
        if "tpad" in mode:
            flags["tpad"] = True

    return flags


def get_mode(flags: Dict[str, bool]) -> str:
    if flags["mode_switch"]:
        return "extended"
    elif flags["long_work_area_2"] and flags["tpad"]:
        return "long+tpad"
    elif flags["long_work_area_2"]:
        return "long"
    else:
        return "regular"


def get_flags(wa1: str) -> Dict[str, Any]:
    layout = WORK_AREA_LAYOUTS["input"]["WA1"]

    flags = {
        "function": parse_field(layout["function"], wa1),
        "mode_switch": parse_field(layout["mode_switch"], wa1) == "X",
        "long_work_area_2": parse_field(layout["long_work_area_2"], wa1) == "L",
        "tpad": parse_field(layout["tpad"], wa1) == "Y",
        "auxseg": parse_field(layout["auxseg"], wa1) == "Y",
    }

    flags["mode"] = get_mode(flags)

    return flags


def create_wa1(kwargs: Dict[str, Any]) -> str:
    kwargs["work_area_format"] = "C"
    b = bytearray(b" " * 1200)
    mv = memoryview(b)

    layout = WORK_AREA_LAYOUTS["input"]["WA1"]

    for key, value in kwargs.items():
        formatter = get_formatter(layout[key]["formatter"])
        value = "" if value is None else str(formatter(value))

        i = layout[key]["i"]
        length = i[1] - i[0]
        mv[i[0] : i[1]] = value.ljust(length)[:length].encode()

    return str(b.decode())


def create_wa2(flags: Dict[str, Any]) -> Optional[str]:
    length = FUNCTIONS[flags["function"]][flags["mode"]]

    if length is None:
        return None

    if flags["auxseg"]:
        length += AUXILIARY_SEGMENT_LENGTH

    return " " * length


def format_input(kwargs: Dict[str, Any]) -> Tuple[Dict[str, Any], str, Optional[str]]:
    wa1 = create_wa1(kwargs)

    flags = get_flags(wa1)

    if flags["function"] not in FUNCTIONS:
        raise GeosupportError("INVALID FUNCTION CODE", {})

    wa2 = create_wa2(flags)

    return flags, wa1, wa2


def parse_field(field: Dict[str, Any], wa: str) -> Any:
    i = field["i"]
    formatter = get_formatter(field["formatter"])
    return formatter(wa[i[0] : i[1]])


def parse_workarea(layout: Dict[str, Any], wa: str) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    for key in layout:
        if "i" in layout[key]:
            output[key] = parse_field(layout[key], wa)
        else:
            output[key] = {}
            for subkey in layout[key]:
                output[key][subkey] = parse_field(layout[key][subkey], wa)

    return output


def parse_output(flags: Dict[str, Any], wa1: str, wa2: Optional[str]) -> Dict[str, Any]:
    output: Dict[str, Any] = {}

    output.update(parse_workarea(WORK_AREA_LAYOUTS["output"]["WA1"], wa1))

    if wa2 is None:
        return output

    function_name = flags["function"]
    if function_name in WORK_AREA_LAYOUTS["output"]:
        output.update(parse_workarea(WORK_AREA_LAYOUTS["output"][function_name], wa2))

    function_mode = function_name + "-" + flags["mode"]
    if function_mode in WORK_AREA_LAYOUTS["output"]:
        output.update(parse_workarea(WORK_AREA_LAYOUTS["output"][function_mode], wa2))

    if flags["auxseg"]:
        output.update(
            parse_workarea(
                WORK_AREA_LAYOUTS["output"]["AUXSEG"], wa2[-AUXILIARY_SEGMENT_LENGTH:]
            )
        )

    return output
