WA1_PARAMETERS = {
    "Geosupport Function Code": {
        "functions": "All",
        "i": (0, 2),
        "alt_names":['func', 'function_code']
    },
    "House Number - Display Format": {
        "functions": "1, 1A, 1B, 1E, AP",
        "i": (2, 18),
        "alt_names":['house_number']
    },
    "House Number - Sort Format": {
        "functions": "1, 1A, 1B, 1E, AP, D*",
        "i": (18, 29),
        "alt_names":[]
    },
    "Low House Number - Display Format": {
        "functions": "Internal Use",
        "i": (29, 45),
        "alt_names":['']
    },
    "Low House Number - Sort Format": {
        "functions": "D*, Internal Use",
        "i": (45, 56),
        "alt_names":[]
    },
    "B10SC-1 (includes Borough Code 1, B5SC-1 and B7SC-1)": {
        "functions": "See next 2 entries",
        "i": (56, 67),
        "alt_names":['borough']
    },
    "Borough Code-1": {
        "functions": "Required for All Functions but BL, BN. Ignored if Fn 2 has Node Number input",
        "i": (56, 57),
        "alt_names":['borough_code']
    },
    "10SC-1": {
        "functions": "All but 1N, B*",
        "i": (57, 67),
        "alt_names":['street_code']
    },
    "Street Name-1": {
        "functions": "All but BL, BN, D*",
        "i": (67, 99),
        "alt_names":['street_name', 'street']
    },
    "B10SC-2 (includes Borough Code 2, B5SC-2 and B7SC-2)": {
        "functions": "2, 3*, D*",
        "i": (99, 110),
        "alt_names":['borough_2']
    },
    "Borough Code-2": {
        "functions": "2, 3*, D*",
        "i": (99, 100),
        "alt_names":['borough_code_2']
    },
    "10SC-2": {
        "functions": "2, 3*, D*",
        "i": (100, 110),
        "alt_names":['street_code_2']
    },
    "Street Name-2": {
        "functions": "2, 3*",
        "i": (110, 142),
        "alt_names":['street_name_2']
    },
    "B10SC-3 (includes Borough Code 3, B5SC-3 and B7SC-3)": {
        "functions": "3*, D*",
        "i": (142, 153),
        "alt_names":['borough_3']
    },
    "Borough Code-3": {
        "functions": "3*, D*",
        "i": (142, 143),
        "alt_names":['borough_code_3']
    },
    "10SC-3": {
        "functions": "3*, D*",
        "i": (143, 153),
        "alt_names":['street_code_3']
    },
    "Street Name-3": {
        "functions": "3*",
        "i": (153, 185),
        "alt_names":['street_name_3']
    },
    "BOROUGH BLOCK LOT (BBL)": {
        "functions": "BL",
        "i": (185, 195),
        "alt_names":['bbl']
    },
    "Borough Code": {
        "functions": "BL",
        "i": (185, 186),
        "alt_names":['bbl_borough']
    },
    "Tax Block": {
        "functions": "BL",
        "i": (186, 191),
        "alt_names":['bbl_block']
    },
    "Tax Lot": {
        "functions": "BL",
        "i": (191, 195),
        "alt_names":['bbl_lot']
    },
    "Filler for Tax Lot Version Number": {
        "functions": "Not Implemented",
        "i": (195, 196),
        "alt_names":[]
    },
    "Building Identification Number (BIN)": {
        "functions": "BN",
        "i": (196, 203),
        "alt_names":['bin']
    },
    "Compass Direction": {
        "functions": "2, 3C, 3S",
        "i": (203, 204),
        "alt_names":['compass_direction']
    },
    "Compass Direction for 2nd Intersection": {
        "functions": "3S",
        "i": (204, 205),
        "alt_names":['compass_direction_2']
    },
    "Node Number": {
        "functions": "2, 2W",
        "i": (205, 212),
        "alt_names":['node_number', 'node']
    },
    "Work Area Format Indicator": {
        "functions": "All",
        "i": (212, 213),
        "alt_names":['work_area_format']
    },
    "ZIP Code Input": {
        "functions": "1*, AP",
        "i": (213, 218),
        "alt_names":['zip', 'zip_code']
    },
    "Unit Input": {
        "functions": "1*",
        "i": (218, 232),
        "alt_names":[]
    },
    "Long Work Area 2 Flag": {
        "functions": "1A, BL",
        "i": (314, 315),
        "alt_names":['long_work_area_2']
    },
    "House Number Justification Flag": {
        "functions": "Not Implemented",
        "i": (315, 316),
        "alt_names":[]
    },
    "House Number Normalization Length": {
        "functions": "Not Implemented",
        "i": (316, 318),
        "alt_names":[]
    },
    "House Number Normalization Override Flag": {
        "functions": "Internal Use",
        "i": (318, 319),
        "alt_names":[]
    },
    "Street Name Normalization Length Limit (SNL)": {
        "functions": "All but B*",
        "i": (319, 321),
        "alt_names":[]
    },
    "Street Name Normalization Format Flag": {
        "functions": "All but B*",
        "i": (321, 322),
        "alt_names":[]
    },
    "Cross Street Names Flag a.k.a. Expanded Format Flag": {
        "functions": "1, 1A, 1B, 1E, 2, 3, 3C",
        "i": (322, 323),
        "alt_names":[]
    },
    "Roadbed Request Switch": {
        "functions": "1, 1B, 1E, 3S (Limited)",
        "i": (323, 324),
        "alt_names":[]
    },
    "Reserved for Internal Use": {
        "functions": "Internal GRC Flag",
        "i": (324, 325),
        "alt_names":[]
    },
    "Auxiliary Segment Switch": {
        "functions": "3, 3C",
        "i": (325, 326),
        "alt_names":['auxiliary_segments']
    },
    "Browse Flag": {
        "functions": "1*, 2, 3, 3C, BB, BF",
        "i": (326, 327),
        "alt_names":[]
    },
    "Real Streets Only Flag": {
        "functions": "3S",
        "i": (327, 328),
        "alt_names":[]
    },
    "TPAD Switch": {
        "functions": "1A, 1B, BL, BN",
        "i": (328, 329),
        "alt_names":["tpad"],
        "formatter": lambda v: 'Y' if v else 'N'
    },
    "Mode Switch": {
        "functions": "1, 1E, 1A, 3, 3C, AP",
        "i": (329, 330),
        "alt_names":['mode_switch']
    },
    "WTO Switch": {
        "functions": "All",
        "i": (330, 331),
        "alt_names":[]
    }
}

FORMATTERS = {
    'tpad': lambda v: 'Y' if v else 'N',
    'long_work_area_2': lambda v: 'L' if v else '',
    '': lambda v: v
}

WA1 = {}

import pandas as pd
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../work_areas/wa1_input.csv")
df = pd.read_csv(path, encoding='latin-1').fillna('')

for i,row in df.iterrows():
    name = row['name'].strip(':').strip()
    alt_names = [n.strip() for n in row['alt_names'].split(',')]
    v = {
        'i': (row['from'] - 1, row['to']),
        'formatter': FORMATTERS[row['formatter']]
    }
    WA1[name] = v
    for n in alt_names:
        WA1[n] = v

def format_wa1_input(kwargs):
    kwargs['work_area_format'] = 'C'
    b = bytearray(b' '*1200)
    mv = memoryview(b)

    for key,value in kwargs.items():
        if 'formatter' in WA1[key]:
            value = WA1[key]['formatter'](value)

        value = '' if value is None else str(value)

        i = WA1[key]['i']
        mv[i[0]:i[1]] = value.ljust(i[1]-i[0]).encode()

    return b.decode()
