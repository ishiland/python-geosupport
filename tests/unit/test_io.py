from geosupport.error import GeosupportError
from geosupport.io import list_of, list_of_items, borough, flag

from ..testcase import TestCase


class TestIO(TestCase):

    def test_list_of(self):
        result = list_of(3, lambda v: v.strip(), "a   b   c   ")
        self.assertEqual(result, ["a", "b", "c"])

    def test_list_of_items(self):
        result = list_of_items(3)("a   b   c   ")
        self.assertEqual(result, ["a", "b", "c"])

    def test_borough(self):
        self.assertEqual(borough("MN"), "1")
        self.assertEqual(borough("queens"), "4")
        self.assertEqual(borough(None), "")
        self.assertEqual(borough(""), "")
        self.assertEqual(borough(1), "1")
        self.assertEqual(borough("2"), "2")

        with self.assertRaises(GeosupportError):
            borough("Fake")

    def test_flag(self):
        f = flag("Y", "N")
        self.assertEqual(f(True), "Y")
        self.assertEqual(f(False), "N")
        self.assertEqual(f("Y"), "Y")
        self.assertEqual(f("y"), "Y")
        self.assertEqual(f("n"), "N")
        self.assertEqual(f(""), "N")
        self.assertEqual(f(None), "N")
        self.assertEqual(f("Yes"), "Y")
