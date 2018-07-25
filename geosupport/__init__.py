from functools import partial
import sys
from .work_area_layouts import format_input, parse_output, GeosupportError

FUNCTION_ALT_NAMES = {
    '1': [],
    '1a': [],
    '1b': ['address'],
    '1e': [],
    '1n': ['street_name_to_street_code', 'get_street_code'],
    '2': ['intersection'],
    '2w': ['intersections', 'intersection_wide'],
    '3': ['street_segment'],
    '3c': ['blockface'],
    '3s': ['street_stretch'],
    'ap': ['address_point'],
    'bb': ['browse_back'],
    'bf': ['browse_forward'],
    'bl': ['bbl', 'tax_lot', 'lot'],
    'bn': ['bin', 'building'],
    'd': ['get_street_name'],
    'dg': [],
    'dn': [],
    'n*': ['normalize_street_name']
}

FUNCTIONS = {}

for function, alt_names in FUNCTION_ALT_NAMES.items():
    FUNCTIONS[function] = function
    FUNCTIONS[function.upper()] = function
    for name in alt_names:
        FUNCTIONS[name] = function
        FUNCTIONS[name.upper()] = function

class Geosupport(object):
    def __init__(self):
        self.py_version = sys.version_info[0]
        try:
            self.platform = sys.platform
            if sys.maxsize > 2 ** 32:
                self.py_bit = '64'
            else:
                self.py_bit = '32'
            if self.platform == 'win32':
                if self.py_bit == '64':
                    from ctypes import cdll
                    self.geolib = cdll.LoadLibrary("NYCGEO.dll")
                else:
                    from ctypes import windll  # must use windll for 32-bit Windows binaries
                    self.geolib = windll.LoadLibrary("NYCGEO.dll")
            elif self.platform == 'linux' or self.platform == 'linux2':
                import os
                from ctypes import cdll
                self.geolib = cdll.LoadLibrary(os.path.join(os.environ['LD_LIBRARY_PATH'], "libgeo.so"))
            else:
                raise Exception('This Operating System is currently not supported.')
        except OSError as e:
            sys.exit(
                '{}\n'
                'You are currently using a {}-bit Python interpreter. Is the installed '
                'version of Geosupport {}-bit?'.format(e, self.py_bit, self.py_bit))

    def _call_geolib(self, flags, wa1, wa2):
        """
        Calls the Geosupport libs & encodes/deocodes strings for Python 3.
        :param wa1: Work Area 1
        :param wa2: Work Area 2
        :param func: Function that determines the dictionary to return.
        :return: Dictionary of results
        """

        # encode
        if self.py_version == 3:
            wa1 = bytes(str(wa1), 'utf8')
            wa2 = bytes(str(wa2), 'utf8')

        # Call Geosupport libs
        if self.platform == 'win32':
            self.geolib.NYCgeo(wa1, wa2)  # windows
        else:
            self.geolib.geo(wa1, wa2)  # linux

        # decode
        if self.py_version == 3:
            wa1 = str(wa1, 'utf8')
            wa2 = str(wa2, 'utf8')

        #print(wa1)
        #print(wa2)

        return parse_output(flags, wa1, wa2)

    def __getattr__(self, name):
        if name in FUNCTIONS:
            return partial(self.call, function=FUNCTIONS[name])

        raise AttributeError("'%s' object has no attribute '%s'" %(
            self.__class__.__name__, name
        ))

    def __getitem__(self, name):
        return self.__getattr__(name)

    def call(self, kwargs_dict={}, **kwargs):
        kwargs_dict.update(kwargs)
        flags, wa1, wa2 = format_input(kwargs_dict)
        result = self._call_geolib(flags, wa1, wa2)
        return_code = result['Geosupport Return Code (GRC)']
        if not return_code.isdigit() or int(return_code) > 1:
            raise GeosupportError(
                result['Message'] + ' ' + result['Message 2'],
                result
            )
        return result
