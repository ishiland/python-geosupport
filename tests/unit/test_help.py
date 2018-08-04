from ..testcase import TestCase

class TestHelp(TestCase):

    def test_get_function_list(self):
        h = self.geosupport.help()

        self.assertTrue("1" in h)
        self.assertTrue("bbl" in h)

    def test_function_help(self):
        h = self.geosupport.help("bbl")

        self.assertTrue("Function BL processes" in h)
        self.assertTrue("Input: Borough" in h)
        self.assertTrue("Output: Tax lot" in h)
        self.assertTrue("Modes: regular, extended" in h)
        self.assertTrue("Mode Switch" in h)

    def test_invalid_function_help(self):
        h = self.geosupport.help("fake")

        self.assertEqual(h, "Function 'fake' does not exist.")
