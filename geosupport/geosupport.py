from functools import partial
import os
import sys
import logging
from configparser import ConfigParser
from typing import Any, Optional, Tuple

from .config import USER_CONFIG, WA1_SIZE, WA2_SIZE
from .error import GeosupportError
from .function_info import FUNCTIONS, function_help, list_functions, input_help
from .io import format_input, parse_output, set_mode
from .platform_utils import load_geosupport_library

# Set up module-level logging.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class Geosupport:
    """
    Python wrapper for the Geosupport library.

    This class loads the Geosupport C library using a helper function
    to encapsulate platform-specific logic. Work areas (WA1 and WA2)
    are allocated with fixed sizes according to the Geosupport COW requirements.
    """

    def __init__(
        self,
        geosupport_path: Optional[str] = None,
        geosupport_version: Optional[str] = None,
    ) -> None:
        global GEOLIB
        self.platform: str = sys.platform
        self.py_bit: str = "64" if (sys.maxsize > 2**32) else "32"

        if geosupport_version is not None:
            config = ConfigParser()
            config.read(os.path.expanduser(USER_CONFIG))
            versions = dict(config.items("versions"))
            geosupport_path = versions.get(geosupport_version.lower())
            logger.debug("Using geosupport version: %s", geosupport_version)

        # On Windows, if a geosupport_path is provided, set the necessary environment variables.
        if geosupport_path is not None:
            if self.platform.startswith("linux"):
                raise GeosupportError(
                    "geosupport_path and geosupport_version are not valid on Linux. "
                    "You must set LD_LIBRARY_PATH and GEOFILES before running Python."
                )
            os.environ["GEOFILES"] = os.path.join(geosupport_path, "Fls" + os.sep)
            os.environ["PATH"] = ";".join(
                i
                for i in os.environ.get("PATH", "").split(";")
                if "GEOSUPPORT" not in i.upper()
            )
            os.environ["PATH"] += ";" + os.path.join(geosupport_path, "bin")
            logger.debug(
                "Environment variables set using geosupport_path: %s", geosupport_path
            )

        try:
            # Load the Geosupport library using the helper function.
            self.geolib = load_geosupport_library(geosupport_path or "", self.py_bit)
            GEOLIB = self.geolib
            logger.debug("Geosupport library loaded successfully.")
        except OSError as e:
            logger.exception("Error loading Geosupport library.")
            raise GeosupportError(
                f"{e}\nYou are currently using a {self.py_bit}-bit Python interpreter. "
                f"Is the installed version of Geosupport {self.py_bit}-bit?"
            )

    def _call_geosupport(self, wa1: str, wa2: Optional[str]) -> Tuple[str, str]:
        """
        Prepares mutable buffers for the Geosupport function call, calls the library,
        and returns the resulting work areas as a tuple (WA1, WA2).

        Assumes that wa1 and wa2 (if not None) are formatted to the exact fixed lengths.
        """
        from ctypes import create_string_buffer

        buf1 = create_string_buffer(wa1.encode("utf8"), WA1_SIZE)
        if wa2 is None:
            buf2 = create_string_buffer(WA2_SIZE)
        else:
            buf2 = create_string_buffer(wa2.encode("utf8"), WA2_SIZE)

        logger.debug(
            "Calling Geosupport function with WA1 size: %d and WA2 size: %d",
            WA1_SIZE,
            WA2_SIZE,
        )
        if self.platform.startswith("win"):
            self.geolib.NYCgeo(buf1, buf2)
        else:
            self.geolib.geo(buf1, buf2)

        out_wa1 = buf1.value.decode("utf8")
        out_wa2 = buf2.value.decode("utf8")
        logger.debug("Geosupport call completed.")
        return out_wa1, out_wa2

    def call(
        self, kwargs_dict: Optional[dict] = None, mode: Optional[str] = None, **kwargs
    ) -> dict:
        """
        Prepares work areas using format_input, calls the Geosupport library,
        and returns the parsed output as a dictionary.

        Raises a GeosupportError if the Geosupport Return Code indicates an error.
        """
        if kwargs_dict is None:
            kwargs_dict = {}
        kwargs_dict.update(kwargs)
        kwargs_dict.update(set_mode(mode))
        flags, wa1, wa2 = format_input(kwargs_dict)
        # Ensure wa2 is a string.
        wa2 = wa2 if wa2 is not None else ""
        logger.debug("Formatted WA1 and WA2 using input parameters.")
        wa1, wa2 = self._call_geosupport(wa1, wa2)
        result = parse_output(flags, wa1, wa2)
        return_code = result.get("Geosupport Return Code (GRC)", "")
        if not return_code.isdigit() or int(return_code) > 1:
            error_message = (
                result.get("Message", "") + " " + result.get("Message 2", "")
            )
            logger.error("Geosupport call error: %s", error_message)
            raise GeosupportError(error_message, result)
        logger.debug("Geosupport call returned successfully.")
        return result

    def __getattr__(self, name: str) -> Any:
        """
        Allows calling Geosupport functions as attributes.
        For example, geosupport.some_function(...).
        """
        if name in FUNCTIONS:
            p: Any = partial(self.call, function=name)
            p.help = partial(function_help, name)
            return p
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def __getitem__(self, name: str) -> Any:
        return self.__getattr__(name)

    def help(self, name: Optional[str] = None, return_as_string: bool = False) -> Any:
        """
        Displays or returns help for a Geosupport function.
        If no name is provided, lists all available functions.
        """
        return_val: Optional[str] = None
        if name:
            if name.upper() == "INPUT":
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
