from csv import DictReader
import glob
from os import path

from .config import FUNCTION_INFO_CSV, FUNCTION_INPUTS_CSV, WORK_AREA_LAYOUTS_PATH

class FunctionDict(dict):

    def __init__(self):
        super(FunctionDict, self).__init__()
        self.alt_names = {}

    def __getitem__(self, name):
        name = str(name).strip().upper()
        if self.alt_names and name in self.alt_names:
            name = self.alt_names[name]

        return super(FunctionDict, self).__getitem__(name)

    def __contains__(self, name):
        name = str(name).strip().upper()

        return (
            (name in self.alt_names) or
            (super(FunctionDict, self).__contains__(name))
        )

def load_function_info():
    functions = FunctionDict()

    alt_names = {}

    with open(FUNCTION_INFO_CSV) as f:
        csv = DictReader(f)
        for row in csv:
            function = row['function']
            for k in MODES:
                if row[k]:
                    row[k] = int(row[k])
                else:
                    row[k] = None

            if row['alt_names']:
                row['alt_names'] = [
                    n.strip() for n in row['alt_names'].split(',')
                ]
            else:
                row['alt_names'] = []

            for n in row['alt_names']:
                alt_names[n.upper()] = function

            row['inputs'] = []

            functions[function] = row

    functions.alt_names = alt_names

    with open(FUNCTION_INPUTS_CSV) as f:
        csv = DictReader(f)

        for row in csv:
            if row['function']:
                functions[row['function']]['inputs'].append({
                    'name': row['field'],
                    'comment': row['comments']
                })

    return functions

def list_functions():
    s = sorted([
        "%s (%s)" % (
            function['function'], ', '.join(function['alt_names'])
        ) for function in FUNCTIONS.values()
    ])
    s = ["List of functions (and alternate names):"] + s
    s.append(
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
        "to read about specific function."
    )
    return '\n'.join(s)

def function_help(function, return_as_string=False):
    function = FUNCTIONS[function]

    s = [
        "",
        "%s (%s)" % (function['function'], ', '.join(function['alt_names'])),
        "="*40,
        function['description'],
        "",
        "Input: %s" % function['input'],
        "Output: %s" % function['output'],
        "Modes: %s" % ', '.join([
            m for m in MODES if function[m] is not None
        ]),
        "\nInputs",
        "="*40,
        "\n".join([
            "%s - %s" % (i['name'], i['comment']) for i in function['inputs']
        ]),
        "\nReference",
        "="*40,
        function['links'],
        ""
    ]

    s = "\n".join(s)

    if return_as_string:
        return s
    else:
        print(s)

def input_help():
    s = [
        "\nThe following is a full list of inputs for Geosupport. "
        "It has the full name (followed by alternate names.)",
        "To use the full names, pass a dictionary of values to the "
        "Geosupport functions. Many of the inputs also have alternate names "
        "in parantheses, which can be passed as keyword arguments as well.",
        "\nInputs",
        "="*40,
    ]

    for i in INPUT:
        s.append("%s (%s)" % (i['name'], ', '.join(i['alt_names'])))
        s.append("-"*40)
        s.append("Functions: %s" % i['functions'])
        s.append("Expected Values: %s\n" % i['value'])

    return '\n'.join(s)

def load_work_area_layouts():
    work_area_layouts = {}
    inputs = []

    for csv in glob.glob(path.join(WORK_AREA_LAYOUTS_PATH, '*', '*.csv')):
        directory = path.basename(path.dirname(csv))
        if directory not in work_area_layouts:
            work_area_layouts[directory] = {}

        layout = {}
        name = path.basename(csv).split('.')[0]

        if '-' in name:
            functions, mode = name.split('-')
            mode = '-' + mode
        else:
            functions = name
            mode = ''

        functions = functions.split('_')
        for function in functions:
            work_area_layouts[directory][function + mode] = layout

        with open(csv) as f:
            rows = DictReader(f)

            for row in rows:
                name = row['name'].strip().strip(':').strip()

                parent = row['parent'].strip().strip(':').strip()
                if parent and 'i' in layout[parent]:
                    layout[parent] = {parent: layout[parent]}

                alt_names = [
                    n.strip() for n in row['alt_names'].split(',') if n
                ]

                v = {
                    'i': (int(row['from']) - 1, int(row['to'])),
                    'formatter': row['formatter']
                }

                if parent:
                    layout[parent][name] = v
                else:
                    layout[name] = v

                for n in alt_names:
                    layout[n] = v
                    layout[n.upper()] = v
                    layout[n.lower()] = v

                if directory == 'input':
                    inputs.append({
                        'name': name,
                        'alt_names': alt_names,
                        'functions': row['functions'],
                        'value': row['value']
                    })

    return work_area_layouts, inputs

MODES = ['regular', 'extended', 'long', 'long+tpad']
AUXILIARY_SEGMENT_LENGTH = 500
FUNCTIONS = load_function_info()
WORK_AREA_LAYOUTS, INPUT = load_work_area_layouts()
