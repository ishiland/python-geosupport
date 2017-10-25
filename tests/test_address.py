from geosupport import Geocode
import unittest
import csv
from os import path

"""
All test data sourced from NYC Open Data 
https://opendata.cityofnewyork.us/
"""

g = Geocode()

here = path.abspath(path.dirname(__file__))

address_parsed = path.join(here, 'data', 'addresses_parsed.csv')

address_unparsed = path.join(here, 'data', 'addresses_unparsed.csv')

bbl_bin = path.join(here, 'data', 'BBL_BIN.csv')

placenames = path.join(here, 'data', 'placenames.csv')

cross_streets = path.join(here, 'data', 'cross_streets.csv')

street_stretch = path.join(here, 'data', 'street_stretch.csv')

blockface = path.join(here, 'data', 'blockface.csv')


class TestGeocodeObject(unittest.TestCase):
    def test_address_point(self):
        with open(address_parsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address_point(house_number=row['BUILDING'], street=row['STREET'], zip=row['ZIPCODE'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_street_stretch(self):
        with open(street_stretch) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.street_stretch(row['Street Name'], row['Cross Street 1'], row['Cross Street 2'], row['Borough'],
                                     compass_direction=row['Compass 1'],
                                     compass_direction_2=row['Compass 2'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_blockface(self):
        with open(blockface) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.blockface(row['Street Name'], row['Cross Street 1'], row['Cross Street 2'], row['Borough'],
                                compass_direction=row['Compass 1'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_street_segment(self):
        with open(blockface) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.street_segment(row['Street Name'], row['Cross Street 1'], row['Cross Street 2'], row['Borough'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_intersection(self):
        with open(cross_streets) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.intersection(row['Intersection Street 1'], row['Intersection Street 2'], row['Borough'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_place(self):
        with open(placenames) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.place(row['Landmark'], row['Borough'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_bin(self):
        with open(bbl_bin) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.bin(row['BIN'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_bbl(self):
        with open(bbl_bin) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.bbl(row['BORO CODE'], row['BLOCK'], row['LOT'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_address_parser(self):
        with open(address_unparsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                in_data = row['ADDRESS'] + ', ' + row['CITY'] + ', ' + row['ZIPCODE']
                r = g.address(address=in_data)
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_address_parser_with_boroname(self):
        with open(address_unparsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(address=row['ADDRESS'], boro=row['BORO NAME'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_address_parser_with_zipcode(self):
        with open(address_unparsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(address=row['ADDRESS'], zip=row['ZIPCODE'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_address_with_borocode(self):
        with open(address_parsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(house_number=row['BUILDING'], street=row['STREET'], boro=row['BORO CODE'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_address_with_boroname(self):
        with open(address_parsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(house_number=row['BUILDING'], street=row['STREET'], boro=row['BORO'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)

    def test_address_with_zipcode(self):
        with open(address_parsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(house_number=row['BUILDING'], street=row['STREET'], zip=row['ZIPCODE'])
                self.assertTrue(int(r['Geosupport Return Code']) == 0)


if __name__ == "__main__":
    unittest.main()
