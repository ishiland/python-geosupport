import os
import sys
from unittest import TestCase, mock, skipUnless
from geosupport.platform_utils import build_win_dll_path


class TestSysUtils(TestCase):

    @skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_build_dll_path_with_geosupport_path(self):
        """test that the dll path is created from the provided geosupport path"""
        dll_path = build_win_dll_path(geosupport_path=r"C:\somewhere\on\my\pc")
        self.assertEqual(dll_path.lower(), r"c:\somewhere\on\my\pc\bin\nycgeo.dll")

    @skipUnless(sys.platform.startswith("win"), "requires Windows")
    @mock.patch.dict(
        os.environ,
        {
            "PATH": r"C:\Program Files\Python311\Scripts\;C:\Program Files\Python311\;c:\another\place\on\my\pc\bin"
        },
    )
    def test_build_dll_path_with_geosupport_path_none(self):
        """test that the dll path is created when geosupport path is not provided"""

        # Create a function to selectively mock isdir for our test path
        def mock_isdir(path):
            return path.lower() == r"c:\another\place\on\my\pc\bin"

        # Mock both isdir and listdir
        with mock.patch("os.path.isdir", side_effect=mock_isdir):
            with mock.patch("os.listdir") as mocked_listdir:
                mocked_listdir.return_value = [
                    "geo.dll",
                    "docs",
                    "nycgeo.exe",
                    "nycgeo.dll",
                ]
                dll_path = build_win_dll_path(geosupport_path=None)
                self.assertEqual(
                    dll_path.lower(), r"c:\another\place\on\my\pc\bin\nycgeo.dll"
                )

    @skipUnless(sys.platform.startswith("win"), "requires Windows")
    @mock.patch.dict(os.environ, {"PATH": "just a bunch of nonsense"})
    def test_build_dll_path_raise_exception(self):
        """test that an exception is raised when the nycgeo.dll is not found"""
        with self.assertRaises(Exception) as context:
            build_win_dll_path(geosupport_path=None)
            self.assertTrue("Unable to locate the nycgeo.dll" in context.exception)
