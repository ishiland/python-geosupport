from geosupport import Geosupport
from geosupport.error import GeosupportError

from ..testcase import TestCase


class TestCallByName(TestCase):

    def test_address(self):
        result = self.geosupport.address(
            {
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            }
        )

        self.assertDictSubsetEqual(
            {
                "Physical ID": "0079828",
                "From LION Node ID": "0015487",
                "To LION Node ID": "0015490",
                "Blockface ID": "0212261942",
            },
            result,
        )

    def test_address_upper(self):
        result = self.geosupport.ADDRESS(
            {
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            }
        )

        self.assertDictSubsetEqual(
            {
                "Physical ID": "0079828",
                "From LION Node ID": "0015487",
                "To LION Node ID": "0015490",
                "Blockface ID": "0212261942",
            },
            result,
        )

    def test_1(self):
        result = self.geosupport["1"](
            {
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            }
        )

        self.assertDictSubsetEqual(
            {
                "ZIP Code": "10013",
                "First Borough Name": "MANHATTAN",
                "First Street Name Normalized": "WORTH STREET",
            },
            result,
        )

        self.assertTrue("Physical ID" not in result)

    def test_1A_extended_mode_parameter(self):
        result = self.geosupport.call(
            {
                "function": "1a",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            },
            mode="extended",
        )

        self.assertTrue("Street Name" in result["LIST OF GEOGRAPHIC IDENTIFIERS"][0])

    def test_1A_long_mode_parameter(self):
        result = self.geosupport.call(
            {
                "function": "1a",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            },
            mode="long",
        )

        self.assertEqual(result["Number of Buildings on Tax Lot"], "0001")

        self.assertTrue(
            "TPAD BIN Status" not in result["LIST OF BUILDINGS ON TAX LOT"][0]
        )

    def test_1A_long_tpad_mode_parameter(self):
        result = self.geosupport.call(
            {
                "function": "1a",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            },
            mode="long+tpad",
        )

        self.assertTrue("TPAD BIN Status" in result["LIST OF BUILDINGS ON TAX LOT"][0])

    def test_1_kwargs(self):
        result = self.geosupport["1"](
            house_number="125",
            street_name="Worth St",
            borough_code="Mn",
        )

        self.assertDictSubsetEqual(
            {
                "ZIP Code": "10013",
                "First Borough Name": "MANHATTAN",
                "First Street Name Normalized": "WORTH STREET",
            },
            result,
        )

        self.assertTrue("Physical ID" not in result)

    def test_call_invalid_function(self):
        with self.assertRaises(AttributeError):
            self.geosupport.fake({})

        with self.assertRaises(AttributeError):
            self.geosupport["fake"]({})

    def test_call_invalid_key(self):
        with self.assertRaises(KeyError):
            self.geosupport.intersection(
                borough_code="BK", street1="east 19 st", street_2="ave h"
            )

        with self.assertRaises(KeyError):
            self.geosupport.intersection(
                borough_code="BK", street_1="east 19 st", street2="ave h"
            )

        self.geosupport.intersection(
            borough_code="BK", street_name_1="east 19 st", street_name_2="ave h"
        )
