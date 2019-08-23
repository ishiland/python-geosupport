from os import path

FUNCTION_INFO_PATH = path.join(
    path.abspath(path.dirname(__file__)),
    'function_info'
)

FUNCTION_INFO_CSV = path.join(FUNCTION_INFO_PATH, 'function_info.csv')
FUNCTION_INPUTS_CSV = path.join(FUNCTION_INFO_PATH, 'function_inputs.csv')
WORK_AREA_LAYOUTS_PATH = path.join(FUNCTION_INFO_PATH, 'work_area_layouts')

BOROUGHS = {
    'MANHATTAN': 1, 'MN': 1, 'NEW YORK': 1, 'NY': 1, '36061': 1,
    'BRONX': 2, 'THE BRONX': 2, 'BX': 2, '36005': 2,
    'BROOKLYN': 3, 'BK': 3, 'BKLYN': 3, 'KINGS': 3, '36047': 3,
    'QUEENS': 4, 'QN': 4, 'QU': 4, '36081': 4,
    'STATEN ISLAND': 5, 'SI': 5, 'STATEN IS': 5, 'RICHMOND': 5, '36085': 5,
    '': '',
}

USER_CONFIG = '~/.python-geosupport.cfg'
