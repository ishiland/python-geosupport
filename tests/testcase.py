import unittest

from geosupport import Geosupport


class TestCase(unittest.TestCase):

    def assertDictSubsetEqual(self, subset, superset):
        for k, v in subset.items():
            self.assertEqual(v, superset[k], k)

    @classmethod
    def setUpClass(cls):
        cls.geosupport = Geosupport()
