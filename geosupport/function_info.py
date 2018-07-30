from csv import DictReader
import glob
from os import path

from geosupport.config import FUNCTION_INFO_CSV, FUNCTION_INPUTS_CSV, WORK_AREA_LAYOUTS_PATH

MODES = ['regular', 'extended', 'long', 'long+tpad']
AUXILIARY_SEGMENT_LENGTH = 500

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
    FUNCTIONS = FunctionDict()

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

            FUNCTIONS[function] = row

    FUNCTIONS.alt_names = alt_names

    with open(FUNCTION_INPUTS_CSV) as f:
        csv = DictReader(f)

        for row in csv:
            if row['function']:
                FUNCTIONS[row['function']]['inputs'].append({
                    'name': row['field'],
                    'comment': row['comments']
                })

    return FUNCTIONS

def list_functions():
    s = sorted([
        "%s (%s)" % (
            function['function'], ', '.join(function['alt_names'])
        ) for function in FUNCTIONS.values()
    ])
    s = ["List of functions (and alternate names):"] + s
    s.append("\nUse Geosupport.help(<function>) to read about specific function.")
    return '\n'.join(s)

def function_help(function):
    function = FUNCTIONS[function]

    s = [
        "%s (%s)" % (function['function'], ', '.join(function['alt_names'])),
        "="*40,
        function['description'],
        "",
        "Input: %s" % function['input'],
        "Output: %s" % function['output'],
        "Modes: %s" % ', '.join([
            m for m in MODES if function[m] is not None
        ]),
        "",
        "Inputs",
        "="*40,
    ]

    for i in function['inputs']:
        s.append("%s - %s" % (i['name'], i['comment']))

    s = "\n".join(s)

    return s

FUNCTIONS = load_function_info()

def load_work_area_layouts():
    WORK_AREA_LAYOUTS = {}

    for csv in glob.glob(path.join(WORK_AREA_LAYOUTS_PATH, '*', '*.csv')):
        directory = path.basename(path.dirname(csv))
        if directory not in WORK_AREA_LAYOUTS:
            WORK_AREA_LAYOUTS[directory] = {}

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
            WORK_AREA_LAYOUTS[directory][function + mode] = layout

        '''df = pd.read_csv(
            csv, encoding='latin-1', dtype={'from': int, 'to': int, 'formatter': str}
        ).fillna('')'''

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
                    #'formatter': get_formatter(row['formatter'])
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

    return WORK_AREA_LAYOUTS

WORK_AREA_LAYOUTS = load_work_area_layouts()