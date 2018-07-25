from geosupport import Geosupport, GeosupportError

from ..testcase import TestCase

class TestCallByName(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.geosupport = Geosupport()

    def test_address(self):
        result = self.geosupport.address({
            'house_number': '125',
            'street_name': 'Worth St',
            'borough_code': 'Mn',
        })

        self.assertDictSubsetEqual({
            'Physical ID': '0079828',
            'From LION Node ID': '0015487',
            'To LION Node ID': '0015490',
            'Blockface ID': '0212261942'
        }, result)

    def test_address_upper(self):
        result = self.geosupport.ADDRESS({
            'house_number': '125',
            'street_name': 'Worth St',
            'borough_code': 'Mn',
        })

        self.assertDictSubsetEqual({
            'Physical ID': '0079828',
            'From LION Node ID': '0015487',
            'To LION Node ID': '0015490',
            'Blockface ID': '0212261942'
        }, result)

    def test_1(self):
        result = self.geosupport['1']({
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

    def test_call_invalid_function(self):
        with self.assertRaises(AttributeError):
            self.geosupport.fake({})

        with self.assertRaises(AttributeError):
            self.geosupport['fake']({})
