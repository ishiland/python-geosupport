from functools import partial
import os
import sys
import logging
from configparser import ConfigParser
from typing import Optional, Tuple

# Set up module-level logging.
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Adjust log level as needed.
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(name)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Platform-specific imports
if sys.platform == 'win32':
    from ctypes import (
        c_char, c_char_p, c_int, c_void_p, c_uint, c_ulong,
        cdll, create_string_buffer, sizeof, windll, WinDLL, wintypes
    )
else:
    from ctypes import (
        c_char, c_char_p, c_int, c_void_p, c_uint, c_ulong,
        cdll, create_string_buffer, sizeof, CDLL, RTLD_GLOBAL
    )
    import ctypes.util

from .config import USER_CONFIG
from .error import GeosupportError
from .function_info import FUNCTIONS, function_help, list_functions, input_help
from .io import format_input, parse_output, set_mode
from .sysutils import build_win_dll_path

# Global variable to hold the loaded geosupport library.
GEOLIB = None
# Constants for work area sizes.
WA1_SIZE: int = 1200
WA2_SIZE: int = 32767  # Maximum size for WA2.

class Geosupport:
    """
    Python wrapper for the Geosupport library.

    This class loads the Geosupport C library and provides a method to
    call its functions by preparing fixed-length work areas (WA1 and WA2)
    according to the Geosupport COW specifications.
    """
    def __init__(self, geosupport_path: Optional[str] = None,
                 geosupport_version: Optional[str] = None) -> None:
        global GEOLIB
        self.platform: str = sys.platform
        self.py_bit: str = '64' if (sys.maxsize > 2 ** 32) else '32'

        # If a specific geosupport version is requested, look it up in the user config file.
        if geosupport_version is not None:
            config = ConfigParser()
            config.read(os.path.expanduser(USER_CONFIG))
            versions = dict(config.items('versions'))
            geosupport_path = versions.get(geosupport_version.lower())
            logger.debug("Using geosupport version: %s", geosupport_version)

        # Set environment variables if a geosupport_path is provided (only valid on Windows).
        if geosupport_path is not None:
            if self.platform.startswith('linux'):
                raise GeosupportError(
                    "geosupport_path and geosupport_version are not valid on Linux. "
                    "You must set LD_LIBRARY_PATH and GEOFILES before running Python."
                )
            os.environ['GEOFILES'] = os.path.join(geosupport_path, 'Fls' + os.sep)
            os.environ['PATH'] = ';'.join(
                i for i in os.environ.get('PATH', '').split(';') if 'GEOSUPPORT' not in i.upper()
            )
            os.environ['PATH'] += ';' + os.path.join(geosupport_path, 'bin')
            logger.debug("Environment variables set using geosupport_path: %s", geosupport_path)

        try:
            if self.platform == 'win32':
                self._load_windows_library(geosupport_path)
            elif self.platform.startswith('linux'):
                self._load_linux_library()
            else:
                raise GeosupportError("This Operating System is currently not supported.")

            GEOLIB = self.geolib
            logger.debug("Geosupport library loaded successfully.")
        except OSError as e:
            logger.exception("Error loading Geosupport library.")
            raise GeosupportError(
                f"{e}\nYou are currently using a {self.py_bit}-bit Python interpreter. "
                f"Is the installed version of Geosupport {self.py_bit}-bit?"
            )

    def _load_windows_library(self, geosupport_path: Optional[str]) -> None:
        """Load the Geosupport library on Windows."""
        from ctypes import windll, WinDLL, wintypes
        global GEOLIB

        if GEOLIB is not None:
            kernel32 = WinDLL('kernel32')
            kernel32.FreeLibrary.argtypes = [wintypes.HMODULE]
            kernel32.FreeLibrary(GEOLIB._handle)
            logger.debug("Unloaded previous Geosupport library instance.")

        nyc_geo_dll_path = build_win_dll_path(geosupport_path)
        logger.debug("NYCGEO.dll path: %s", nyc_geo_dll_path)
        if self.py_bit == '64':
            self.geolib = cdll.LoadLibrary(nyc_geo_dll_path)
        else:
            self.geolib = windll.LoadLibrary(nyc_geo_dll_path)

    def _load_linux_library(self) -> None:
        """Load the Geosupport library on Linux."""
        # Using default library name "libgeo.so"
        self.geolib = cdll.LoadLibrary("libgeo.so")
        # Set up function prototype for geo
        from ctypes import c_char_p, c_int
        self.geolib.geo.argtypes = [c_char_p, c_char_p]
        self.geolib.geo.restype = c_int
        logger.debug("Loaded libgeo.so and set up function prototype for geo.")

    def _call_geolib(self, wa1: str, wa2: Optional[str]) -> Tuple[str, str]:
        """
        Prepares mutable buffers for the Geosupport function call, then
        calls the library and returns the resulting work areas.
        
        Assumes wa1 and wa2 are strings with proper fixed lengths (e.g., 1200 bytes for WA1).
        If wa2 is None, an empty buffer of WA2_SIZE is used.
        """
        # Create buffer for WA1.
        buf1 = create_string_buffer(wa1.encode('utf8'), WA1_SIZE)
        if wa2 is None:
            buf2 = create_string_buffer(WA2_SIZE)
        else:
            buf2 = create_string_buffer(wa2.encode('utf8'), WA2_SIZE)

        logger.debug("Calling Geosupport function with WA1 size: %d and WA2 size: %d", WA1_SIZE, WA2_SIZE)
        # Call the geosupport function.
        if self.platform == 'win32':
            self.geolib.NYCgeo(buf1, buf2)
        else:
            self.geolib.geo(buf1, buf2)

        # Decode the output buffers.
        out_wa1 = buf1.value.decode('utf8')
        out_wa2 = buf2.value.decode('utf8')
        logger.debug("Geosupport call completed.")
        return out_wa1, out_wa2

    def call(self, kwargs_dict: Optional[dict] = None, mode: Optional[str] = None, **kwargs) -> dict:
        """
        Prepares work areas (WA1 and WA2) using format_input, calls the Geosupport library,
        and then parses and returns the output as a dictionary.
        
        Raises a GeosupportError if the Geosupport Return Code indicates an error.
        """
        if kwargs_dict is None:
            kwargs_dict = {}
        kwargs_dict.update(kwargs)
        kwargs_dict.update(set_mode(mode))
        flags, wa1, wa2 = format_input(kwargs_dict)
        logger.debug("Formatted WA1 and WA2 using input parameters.")
        wa1, wa2 = self._call_geolib(wa1, wa2)
        result = parse_output(flags, wa1, wa2)
        return_code = result.get('Geosupport Return Code (GRC)', '')
        if not return_code.isdigit() or int(return_code) > 1:
            error_message = result.get('Message', '') + ' ' + result.get('Message 2', '')
            logger.error("Geosupport call error: %s", error_message)
            raise GeosupportError(error_message, result)
        logger.debug("Geosupport call returned successfully.")
        return result

    def __getattr__(self, name: str):
        """
        Allows calling Geosupport functions as attributes of this object.
        For example, geosupport.some_function(...).
        """
        if name in FUNCTIONS:
            p = partial(self.call, function=name)
            p.help = partial(function_help, name)
            return p
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __getitem__(self, name: str):
        return self.__getattr__(name)

    def help(self, name: Optional[str] = None, return_as_string: bool = False):
        """
        Displays or returns help for a Geosupport function. If no name is provided,
        lists all available functions.
        """
        if name:
            if name.upper() == 'INPUT':
                return_val = input_help()
            else:
                try:
                    return_val = function_help(name, return_as_string)
                except KeyError:
                    return_val = f"Function '{name}' does not exist."
        else:
            return_val = list_functions()

        if return_as_string:
            return return_val
        elif return_val:
            print(return_val)
