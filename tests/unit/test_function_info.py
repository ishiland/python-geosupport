from geosupport.function_info import FunctionDict, load_function_info, FUNCTIONS

from ..testcase import TestCase


class TestFunctionInfo(TestCase):

    def test_function_dict(self):
        d = FunctionDict()
        d["A"] = {}

        self.assertTrue("a" in d)
        self.assertTrue("A" in d)
        self.assertEqual(d["a"], d["A"])

        self.assertFalse("b" in d)
