import unittest

class TestCase(unittest.TestCase):

    def assertDictSubsetEqual(self, subset, superset):
        for k, v in subset.items():
            self.assertEqual(v, superset[k], k)
