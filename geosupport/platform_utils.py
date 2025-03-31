import sys
import os
from ctypes import cdll
from .error import GeosupportError
from typing import Optional


def load_geosupport_library(geosupport_path: str, py_bit: str) -> any:
    """
    Loads the Geosupport library in a platform-specific way.

    For Windows, uses geosupport_path to determine the path to NYCGEO.dll.
    For Linux, loads "libgeo.so" (assumed to be in the library path).
    """
    if sys.platform.startswith("win"):
        from ctypes import windll, WinDLL, wintypes  # type: ignore[attr-defined]

        nyc_geo_dll_path = build_win_dll_path(geosupport_path)
        if py_bit == "64":
            return cdll.LoadLibrary(nyc_geo_dll_path)
        else:
            return windll.LoadLibrary(nyc_geo_dll_path)
    elif sys.platform.startswith("linux"):
        # Load the Linux version of the Geosupport library.
        lib = cdll.LoadLibrary("libgeo.so")
        from ctypes import c_char_p, c_int

        lib.geo.argtypes = [c_char_p, c_char_p]
        lib.geo.restype = c_int
        return lib
    else:
        raise GeosupportError("This Operating System is currently not supported.")


def build_win_dll_path(
    geosupport_path: Optional[str] = None, dll_filename: str = "nycgeo.dll"
) -> str:
    """
    Windows-specific function to return the full path of the nycgeo.dll.
    Example: 'C:\\Program Files\\Geosupport Desktop Edition\\Bin\\NYCGEO.dll'
    """
    if geosupport_path:
        return os.path.join(geosupport_path, "bin", dll_filename)

    system_path_entries = os.environ.get("PATH", "").split(";")
    # Filter only directories that exist and end with 'bin' (case-insensitive).
    bin_directories = [
        b for b in system_path_entries if os.path.isdir(b) and b.lower().endswith("bin")
    ]

    for b in bin_directories:
        try:
            for file in os.listdir(b):
                if file.lower() == dll_filename.lower():
                    return os.path.join(b, file)
        except Exception:
            continue

    raise Exception(
        f"Unable to locate the {dll_filename} within your system. Ensure the Geosupport 'bin' directory is in your system PATH."
    )
