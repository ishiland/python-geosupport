import sys

from ..testcase import TestCase


class TestHelp(TestCase):

    def test_get_function_list(self):
        h = self.geosupport.help(return_as_string=True)

        self.assertTrue("1" in h)
        self.assertTrue("bbl" in h)

    def test_function_help(self):
        h = self.geosupport.help("bbl", return_as_string=True)

        self.assertTrue("Function BL processes" in h)
        self.assertTrue("Input: Borough" in h)
        self.assertTrue("Output: Tax lot" in h)
        self.assertTrue("Modes: regular, extended" in h)
        self.assertTrue("Mode Switch" in h)

    def test_invalid_function_help(self):
        h = self.geosupport.help("fake", return_as_string=True)

        self.assertEqual(h, "Function 'fake' does not exist.")

    def test_print(self):

        try:
            import StringIO  # python 2

            h = StringIO.StringIO()
        except ImportError:
            import io  # python 3

            h = io.StringIO()

        sys.stdout = h

        o = self.geosupport.help()

        sys.stdout = sys.__stdout__

        self.assertTrue("bbl" in h.getvalue())
        self.assertTrue(o is None)
