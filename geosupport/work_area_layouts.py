from functools import partial
import glob
from os import path

import pandas as pd

class GeosupportError(Exception):
    pass

WORK_AREA_LENGTHS = {
    'WA1': 1200,
    '1_1E': {
        'regular': 300,
        'extended': 1500
    },
    '1A_BL_BN': {
        'regular': 1363,
        'extended': 2800,
        'long': 17750,
        'long+tpad': 17750,
    },
    '1B': {
        'regular': 4300
    },
    'AP': {
        'regular': 1363,
        'extended': 2800
    },
    '2': {
        'regular': 200
    },
    '2W': {
        'regular': 4000
    },
    '3': {
        'regular': 450,
        'extended': 1000
    },
    '3C': {
        'regular': 300,
        'extended': 850
    },
    '3S': {
        'regular': 19274
    }
}

for key in list(WORK_AREA_LENGTHS.keys()):
    for k in key.split('_'):
        WORK_AREA_LENGTHS[k] = WORK_AREA_LENGTHS[key]

AUXILIARY_SEGMENT_LENGTH = 500

def create_wa2(flags):
    length = WORK_AREA_LENGTHS[flags['function']][flags['mode']]

    if flags.get('auxiliary_segment_switch', '') == 'Y':
       length += AUXILIARY_SEGMENT_LENGTH

    print('********', flags['function'], length)

    return ' ' * length

def list_of_workareas(name, length, v):
    output = []
    i = 0
    # While the next entry isn't blank
    while v[i:i+length].strip() != '':
        output.append(parse_workarea(
            WORK_AREA_LAYOUTS['output'][name],
            v[i:i+length]
        ))
        i += length

    return output

def list_of_items(length, v):
    output = []
    i = 0
    while v[i:i+length].strip() != '':
        output.append(v[i:i+length].strip())
        i += length
    return output

def borough(v):
    v = str(v).strip()
    boroughs = {'MANHATTAN': 1, 'MN': 1, 'NEW YORK': 1, 'NY': 1,
                'BRONX': 2, 'THE BRONX': 2, 'BX': 2,
                'BROOKLYN': 3, 'BK': 3, 'BKLYN': 3, 'KINGS': 3,
                'QUEENS': 4, 'QN': 4, 'QU': 4,
                'STATEN ISLAND': 5, 'SI': 5, 'STATEN IS': 5, 'RICHMOND': 5}
    if v.upper() in boroughs:
        return boroughs[v.upper()]

    return v

FORMATTERS = {
    'tpad': lambda v: 'Y' if v.strip() else 'N',
    'long_work_area_2': lambda v: 'L' if v.strip() else '',
    'LGI': partial(list_of_workareas, 'LGI', 53),
    'LGI-extended': partial(list_of_workareas, 'LGI-extended', 116),
    'BINs': partial(list_of_workareas, 'BINs', 7),
    'BINs-tpad': partial(list_of_workareas, 'BINs-tpad', 8),
    'B5SCs': partial(list_of_items, 6),
    'B7SCs': partial(list_of_items, 8),
    'street_names': partial(list_of_items, 32),
    'borough': borough,
    '': lambda v: '' if v is None else str(v).strip().upper()
}

directory = path.join(
    path.abspath(path.dirname(__file__)),
    'work_area_layouts'
)

WORK_AREA_LAYOUTS = {}

for csv in glob.glob(path.join(directory, '*', '*.csv')):
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

    df = pd.read_csv(
        csv, encoding='latin-1', dtype={'from': int, 'to': int}
    ).fillna('')

    for i,row in df.iterrows():
        name = row['name'].strip().strip(':').strip()

        parent = row['parent'].strip().strip(':').strip()
        if parent and 'i' in layout[parent]:
            layout[parent] = {parent: layout[parent]}

        alt_names = [n.strip() for n in row['alt_names'].split(',') if n]

        v = {
            'i': (row['from'] - 1, row['to']),
            'formatter': FORMATTERS[row['formatter']]
        }

        if parent:
            layout[parent][name] = v
        else:
            layout[name] = v
            for n in alt_names:
                layout[n] = v

#print(WORK_)

def get_flags(layout, wa1):
    flags = {
        'function': parse_field(layout['function'], wa1),
        'mode_switch': parse_field(layout['mode_switch'], wa1),
        'long_work_area_2': parse_field(layout['long_work_area_2'], wa1),
        'tpad': parse_field(layout['tpad'], wa1),
        'auxiliary_segment_switch': parse_field(
            layout['auxiliary_segment_switch'], wa1
        )
    }

    if flags['mode_switch'] == 'X':
        flags['mode'] = 'extended'
    elif (flags['long_work_area_2'] == 'L') and (flags['tpad'] == 'Y'):
        flags['mode'] = 'long+tpad'
    elif flags['long_work_area_2'] == 'L':
        flags['mode'] = 'long'
    else:
        flags['mode'] = 'regular'

    print(flags)

    return flags

def format_input(kwargs):
    kwargs['work_area_format'] = 'C'
    b = bytearray(b' '*1200)
    mv = memoryview(b)

    layout = WORK_AREA_LAYOUTS['input']['WA1']

    for key,value in kwargs.items():
        value = layout[key]['formatter'](value)

        value = '' if value is None else str(value)

        i = layout[key]['i']
        length = i[1]-i[0]
        mv[i[0]:i[1]] = value.ljust(length)[:length].encode()

    wa1 = b.decode()

    flags = get_flags(layout, wa1)

    if flags['function'] not in WORK_AREA_LENGTHS:
        raise GeosupportError('INVALID FUNCTION CODE')

    wa2 = create_wa2(flags)

    return flags, wa1, wa2

def parse_field(field, wa):
    i = field['i']
    formatter = field['formatter']

    return formatter(wa[i[0]:i[1]])

def parse_workarea(layout, wa):
    output = {}

    for key in layout:
        if 'i' in layout[key]:
            output[key] = parse_field(layout[key], wa)
        else:
            output[key] = {}
            for subkey in layout[key]:
                output[key][subkey] = parse_field(layout[key][subkey], wa)

    return output

def parse_output(flags, wa1, wa2):
    output = {}

    output.update(parse_workarea(WORK_AREA_LAYOUTS['output']['WA1'], wa1))

    output.update(parse_workarea(
        WORK_AREA_LAYOUTS['output'][flags['function']], wa2
    ))

    function_mode = flags['function'] + '-' + flags['mode']

    if function_mode in WORK_AREA_LAYOUTS['output']:
        output.update(parse_workarea(
            WORK_AREA_LAYOUTS['output'][function_mode], wa2
        ))

    return output
