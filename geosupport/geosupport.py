from functools import partial
import sys

from geosupport.error import GeosupportError
from geosupport.function_info import FUNCTIONS, function_help, list_functions, input_help
from geosupport.io import format_input, parse_output, set_mode

class Geosupport(object):
    def __init__(self):
        self.py_version = sys.version_info[0]
        self.platform = sys.platform
        self.py_bit = '64' if (sys.maxsize > 2 ** 32) else '32'

        try:
            if self.platform == 'win32':
                if self.py_bit == '64':
                    from ctypes import cdll
                    self.geolib = cdll.LoadLibrary("NYCGEO.dll")
                else:
                    # must use windll for 32-bit Windows binaries
                    from ctypes import windll
                    self.geolib = windll.LoadLibrary("NYCGEO.dll")
            elif self.platform.startswith('linux'):
                import os
                from ctypes import cdll
                self.geolib = cdll.LoadLibrary(
                    os.path.join(os.environ['LD_LIBRARY_PATH'], "libgeo.so")
                )
            else:
                raise Exception('This Operating System is currently not supported.')
        except OSError as e:
            sys.exit(
                '%s\n'
                'You are currently using a %s-bit Python interpreter. '
                'Is the installed version of Geosupport %s-bit?' % (
                    e, self.py_bit, self.py_bit
                )
            )

    def _call_geolib(self, wa1, wa2):
        """
        Calls the Geosupport libs & encodes/deocodes strings for Python 3.
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

        return wa1, wa2

    def call(self, kwargs_dict={}, mode=None, **kwargs):
        kwargs_dict.update(kwargs)
        kwargs_dict.update(set_mode(mode))

        flags, wa1, wa2 = format_input(kwargs_dict)
        wa1, wa2 = self._call_geolib(wa1, wa2)
        result = parse_output(flags, wa1, wa2)

        return_code = result['Geosupport Return Code (GRC)']
        if not return_code.isdigit() or int(return_code) > 1:
            raise GeosupportError(
                result['Message'] + ' ' + result['Message 2'],
                result
            )
        return result

    def __getattr__(self, name):
        if name in FUNCTIONS:
            p = partial(self.call, function=name)
            p.help = partial(function_help, name)
            return p

        raise AttributeError("'%s' object has no attribute '%s'" %(
            self.__class__.__name__, name
        ))

    def __getitem__(self, name):
        return self.__getattr__(name)

    def help(self, name=None):
        if name:
            if name.upper() == 'INPUT':
                return input_help()
            try:
                return function_help(name)
            except KeyError:
                return "Function '%s' does not exist." % name
        else:
            return list_functions()
