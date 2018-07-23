#import unittest

from geosupport import Geosupport, GeosupportError

from ..testcase import TestCase

class TestCall(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.geosupport = Geosupport()

    def test_invalid_function(self):
        with self.assertRaises(GeosupportError):
            self.geosupport.call({'function': 99})

    def test_1(self):
        result = self.geosupport.call({
            'function': 1,
            'house_number': '125',
            'street_name': 'Worth St',
            'borough_code': 'Mn',
        })

        self.assertDictSubsetEqual({
            'ZIP Code': '10013',
            'First Borough Name': 'MANHATTAN',
            'First Street Name Normalized': 'WORTH STREET'
        }, result)

        self.assertTrue('Physical ID' not in result)

    def test_1_extended(self):
        result = self.geosupport.call({
            'function': 1,
            'house_number': '125',
            'street_name': 'Worth St',
            'borough_code': 'Mn',
            'mode_switch': 'X'
        })

        self.assertDictSubsetEqual({
            'Physical ID': '0079828'
        }, result)

    def test_1E(self):
        result = self.geosupport.call({
            'function': '1e',
            'house_number': '125',
            'street_name': 'Worth St',
            'borough_code': 'Mn',
        })

        self.assertDictSubsetEqual({
            'City Council District': '01',
            'State Senatorial District': '26'
        }, result)

        self.assertTrue('Physical ID' not in result)

        #self.assertDictContainsSubset(, )
