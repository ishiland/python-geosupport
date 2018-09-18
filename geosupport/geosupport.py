from functools import partial
import os
import sys

try:
    from configparser import ConfigParser # Python 3
except:
    from ConfigParser import ConfigParser # Python 2

from .config import USER_CONFIG
from .error import GeosupportError
from .function_info import FUNCTIONS, function_help, list_functions, input_help
from .io import format_input, parse_output, set_mode

GEOLIB = None

class Geosupport(object):
    def __init__(self, geosupport_path=None, geosupport_version=None):
        global GEOLIB
        self.py_version = sys.version_info[0]
        self.platform = sys.platform
        self.py_bit = '64' if (sys.maxsize > 2 ** 32) else '32'

        if geosupport_version is not None:
            config = ConfigParser()
            config.read(os.path.expanduser(USER_CONFIG))
            versions = dict(config.items('versions'))
            geosupport_path = versions[geosupport_version.lower()]

        if geosupport_path is not None:
            if self.platform.startswith('linux'):
                raise GeosupportError(
                    "geosupport_path and geosupport_version not valid with "
                    "linux. You must set LD_LIBRARY_PATH and GEOFILES "
                    "before running python."
                )
            os.environ['GEOFILES'] = os.path.join(geosupport_path, 'Fls\\')
            os.environ['PATH'] = ';'.join([
                i for i in os.environ['PATH'].split(';') if
                'GEOSUPPORT' not in i.upper()
            ])
            os.environ['PATH'] += ';' + os.path.join(geosupport_path, 'bin')

        try:
            if self.platform == 'win32':
                from ctypes import windll, cdll, WinDLL, wintypes

                if GEOLIB is not None:
                    kernel32 = WinDLL('kernel32')
                    kernel32.FreeLibrary.argtypes = [wintypes.HMODULE]
                    kernel32.FreeLibrary(GEOLIB._handle)

                if self.py_bit == '64':
                    self.geolib = cdll.LoadLibrary("NYCGEO.dll")
                else:
                    self.geolib = windll.LoadLibrary("NYCGEO.dll")
            elif self.platform.startswith('linux'):
                from ctypes import cdll

                if GEOLIB is not None:
                    cdll.LoadLibrary('libdl.so').dlclose(GEOLIB._handle)

                self.geolib = cdll.LoadLibrary("libgeo.so")
            else:
                raise GeosupportError(
                    'This Operating System is currently not supported.'
                )

            GEOLIB = self.geolib
        except OSError as e:
            raise GeosupportError(
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

    def call(self, kwargs_dict=None, mode=None, **kwargs):
        if kwargs_dict is None:
            kwargs_dict = {}
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

    def help(self, name=None, return_as_string=False):
        if name:
            if name.upper() == 'INPUT':
                return_val = input_help()
            try:
                return_val = function_help(name, return_as_string)
            except KeyError:
                return_val = "Function '%s' does not exist." % name
        else:
            return_val = list_functions()

        if return_as_string:
            return return_val
        elif return_val:
            print(return_val)
