from geosupport import Geosupport
from geosupport.error import GeosupportError

from ..testcase import TestCase


class TestCall(TestCase):

    def test_invalid_function(self):
        with self.assertRaises(GeosupportError):
            self.geosupport.call({"function": 99})

    def test_1(self):
        result = self.geosupport.call(
            {
                "function": 1,
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

    def test_1_extended(self):
        result = self.geosupport.call(
            {
                "function": 1,
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
                "mode_switch": "X",
            }
        )

        self.assertDictSubsetEqual({"Physical ID": "0079828"}, result)

    def test_1E(self):
        result = self.geosupport.call(
            {
                "function": "1e",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            }
        )

        self.assertDictSubsetEqual(
            {"City Council District": "01", "State Senatorial District": "27"}, result
        )

        self.assertTrue("Physical ID" not in result)

    def test_1A(self):
        result = self.geosupport.call(
            {
                "function": "1a",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            }
        )

        self.assertEqual(
            result["BOROUGH BLOCK LOT (BBL)"]["BOROUGH BLOCK LOT (BBL)"], "1001680032"
        )

        self.assertTrue(
            int(result["Number of Entries in List of Geographic Identifiers"]) >= 1
        )

        self.assertTrue(
            "Street Name" not in result["LIST OF GEOGRAPHIC IDENTIFIERS"][0]
        )

    def test_1A_extended(self):
        result = self.geosupport.call(
            {
                "function": "1a",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
                "mode_switch": "X",
            }
        )

        self.assertTrue("Street Name" in result["LIST OF GEOGRAPHIC IDENTIFIERS"][0])

    def test_1A_long(self):
        result = self.geosupport.call(
            {
                "function": "1a",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
                "long_work_area_2": "L",
            }
        )

        self.assertEqual(result["Number of Buildings on Tax Lot"], "0001")

        self.assertTrue(
            "TPAD BIN Status" not in result["LIST OF BUILDINGS ON TAX LOT"][0]
        )

    def test_1A_long_tpad(self):
        result = self.geosupport.call(
            {
                "function": "1a",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
                "long_work_area_2": "L",
                "tpad": "Y",
            }
        )

        self.assertTrue("TPAD BIN Status" in result["LIST OF BUILDINGS ON TAX LOT"][0])

    def test_bl_long(self):
        result = self.geosupport.call(
            {"function": "bl", "bbl": "1001680032", "long_work_area_2": "L"}
        )

        self.assertEqual(
            result["LIST OF BUILDINGS ON TAX LOT"][0][
                "Building Identification Number (BIN)"
            ],
            "1001831",
        )

    def test_bn(self):
        result = self.geosupport.call({"function": "bn", "bin": "1001831"})

        self.assertEqual(
            result["BOROUGH BLOCK LOT (BBL)"]["BOROUGH BLOCK LOT (BBL)"], "1001680032"
        )

    def test_ap(self):
        result = self.geosupport.call(
            {
                "function": "ap",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
            }
        )

        self.assertDictSubsetEqual(
            {
                "Number of Entries in List of Geographic Identifiers": "0001",
                "Address Point ID": "001002108",
            },
            result,
        )

    def test_ap_extended(self):
        result = self.geosupport.call(
            {
                "function": "ap",
                "house_number": "125",
                "street_name": "Worth St",
                "borough_code": "Mn",
                "mode_switch": "X",
            }
        )

        self.assertTrue("Street Name" in result["LIST OF GEOGRAPHIC IDENTIFIERS"][0])

    def test_1b(self):
        result = self.geosupport.call(
            {
                "function": "1b",
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

    def test_2(self):
        result = self.geosupport.call(
            {
                "function": 2,
                "borough_code": "MN",
                "street_name": "Worth St",
                "street_name_2": "Centre St",
            }
        )

        self.assertDictSubsetEqual(
            {"LION Node Number": "0015490", "Number of Intersecting Streets": "2"},
            result,
        )

    def test_2_more_than_2_intersections(self):
        with self.assertRaises(GeosupportError) as cm:
            result = self.geosupport.call(
                {
                    "function": "2",
                    "borough_code": "BK",
                    "street_name": "E 19 St",
                    "street_name_2": "Dead End",
                }
            )

        self.assertEqual(
            str(cm.exception),
            "STREETS INTERSECT MORE THAN TWICE-USE FUNCTION 2W TO FIND RELATED NODES ",
        )

    def test_2W_more_than_2_intersections(self):
        with self.assertRaises(GeosupportError) as cm:
            result = self.geosupport.call(
                {
                    "function": "2w",
                    "borough_code": "BK",
                    "street_name": "grand army plaza oval",
                    "street_name_2": "plaza street east",
                }
            )

        self.assertEqual(
            str(cm.exception),
            "PLAZA STREET EAST IS AN INVALID STREET NAME FOR THIS LOCATION ",
        )

        self.assertEqual(len(cm.exception.result["List of Street Codes"]), 2)
        self.assertEqual(len(cm.exception.result["List of Street Names"]), 2)

        self.assertEqual(cm.exception.result["Node Number"], "")

    def test_2W_with_node(self):
        result = self.geosupport.call({"function": "2w", "node": "0104434"})

        self.assertTrue("GRAND ARMY PLAZA OVAL" in result["List of Street Names"])

        self.assertTrue("PLAZA STREET" in result["List of Street Names"])

    def test_3(self):
        result = self.geosupport.call(
            {
                "function": 3,
                "borough_code": "MN",
                "on": "Lafayette St",
                "from": "Worth st",
                "to": "Leonard St",
            }
        )

        self.assertDictSubsetEqual(
            {"From Node": "0015487", "To Node": "0020353"}, result
        )

        self.assertTrue("Segment IDs" not in result)

    def test_3_auxseg(self):
        result = self.geosupport.call(
            {
                "function": 3,
                "borough_code": "MN",
                "on": "Lafayette St",
                "from": "Worth st",
                "to": "Leonard St",
                "auxseg": "Y",
                "mode_switch": "X",
            }
        )

        self.assertEqual(len(result["Segment IDs"]), 2)
        self.assertTrue("0023578" in result["Segment IDs"])
        self.assertTrue("0032059" in result["Segment IDs"])

    def test_3_extended(self):
        result = self.geosupport.call(
            {
                "function": 3,
                "borough_code": "MN",
                "on": "Lafayette St",
                "from": "Worth st",
                "to": "Leonard St",
                "mode_switch": "X",
            }
        )

        self.assertDictSubsetEqual(
            {
                "From Node": "0015487",
                "To Node": "0020353",
                "Left 2020 Community District Tabulation Area (CDTA)": "MN01",
            },
            result,
        )

        self.assertTrue("Segment IDs" not in result)

    def test_3_extended_auxseg(self):
        result = self.geosupport.call(
            {
                "function": 3,
                "borough_code": "MN",
                "on": "Lafayette St",
                "from": "Worth st",
                "to": "Leonard St",
                "auxseg": "Y",
                "mode_switch": "X",
            }
        )

        self.assertDictSubsetEqual(
            {
                "From Node": "0015487",
                "To Node": "0020353",
                "Left 2020 Community District Tabulation Area (CDTA)": "MN01",
            },
            result,
        )

        self.assertEqual(len(result["Segment IDs"]), 2)
        self.assertTrue("0023578" in result["Segment IDs"])
        self.assertTrue("0032059" in result["Segment IDs"])

    def test_3C(self):
        result = self.geosupport.call(
            {
                "function": "3c",
                "borough_code": "MN",
                "on": "Lafayette St",
                "from": "Worth st",
                "to": "Leonard St",
                "compass_direction": "E",
            }
        )

        self.assertDictSubsetEqual(
            {
                "From Node": "0015487",
                "To Node": "0020353",
                "Side-of-Street Indicator": "R",
            },
            result,
        )

        self.assertTrue("Segment IDs" not in result)

    def test_3C_auxseg(self):
        result = self.geosupport.call(
            {
                "function": "3c",
                "borough_code": "MN",
                "on": "Lafayette St",
                "from": "Worth st",
                "to": "Leonard St",
                "compass_direction": "E",
                "auxseg": "Y",
                "mode_switch": "X",
            }
        )

        self.assertDictSubsetEqual(
            {
                "From Node": "0015487",
                "To Node": "0020353",
                "Side-of-Street Indicator": "R",
            },
            result,
        )

        self.assertEqual(len(result["Segment IDs"]), 2)
        self.assertTrue("7800320" in result["Segment IDs"])
        self.assertTrue("59" in result["Segment IDs"])

    def test_3C_extended_auxseg(self):
        result = self.geosupport.call(
            {
                "function": "3c",
                "borough_code": "MN",
                "on": "Lafayette St",
                "from": "Worth st",
                "to": "Leonard St",
                "compass_direction": "E",
                "auxseg": "Y",
                "mode_switch": "X",
            }
        )

        self.assertDictSubsetEqual(
            {
                "From Node": "0015487",
                "To Node": "0020353",
                "Side-of-Street Indicator": "R",
                "Blockface ID": "0212262072",
            },
            result,
        )

        self.assertEqual(len(result["Segment IDs"]), 2)
        self.assertTrue("7800320" in result["Segment IDs"])
        self.assertTrue("59" in result["Segment IDs"])

    def test_3S(self):
        result = self.geosupport.call(
            {
                "function": "3S",
                "borough_code": "MN",
                "on": "Broadway",
                "from": "worth st",
                "to": "Liberty st",
            }
        )

        self.assertEqual(result["Number of Intersections"], "017")
        self.assertEqual(
            len(result["LIST OF INTERSECTIONS"]), int(result["Number of Intersections"])
        )

    def test_D(self):
        result = self.geosupport.call({"function": "D", "B7SC": "145490"})

        self.assertEqual(result["First Street Name Normalized"], "WORTH STREET")

    def test_DG(self):
        result = self.geosupport.call({"function": "DG", "b7sc": "14549001"})

        self.assertEqual(result["First Street Name Normalized"], "WORTH STREET")

    def test_DN(self):
        result = self.geosupport.call({"function": "DN", "B7SC": "14549001010"})

        self.assertEqual(result["First Street Name Normalized"], "WORTH STREET")

    def test_1N(self):
        result = self.geosupport.call(
            {"function": "1N", "borough_code": "MN", "street": "Worth str"}
        )

        self.assertEqual(result["First Street Name Normalized"], "WORTH STREET")

    def test_Nstar(self):
        result = self.geosupport.call({"function": "N*", "street": "fake cir"})

        self.assertEqual(result["First Street Name Normalized"], "FAKE CIRCLE")

    def test_BF(self):
        result = self.geosupport.call(
            {"func": "BF", "borough_code": "MN", "street": "WORTH"}
        )

        self.assertTrue("WORTH STREET" in result["List of Street Names"])

    def test_BB(self):
        result = self.geosupport.call(
            {"func": "BB", "borough_code": "MN", "street": "WORTH"}
        )

        self.assertTrue("WORLDWIDE PLAZA" in result["List of Street Names"])
