from geosupport import Geocode
import unittest
import csv
from os import path

g = Geocode()

here = path.abspath(path.dirname(__file__))

address_parsed = path.join(here, 'data', 'addresses_parsed.csv')

address_unparsed = path.join(here, 'data', 'addresses_unparsed.csv')

bbl_bin = path.join(here, 'data', 'BBL_BIN.csv')

placenames = path.join(here, 'data', 'placenames.csv')

# cross_streets = path.join(here, 'data', 'cross_streets.csv')


class TestGeocodeObject(unittest.TestCase):

    def test_place(self):
        with open(placenames) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.place(row['Landmark'], row['Borough'])
                self.assertTrue(len(r['Latitude']) > 1 or len(r['Longitude']))

    def test_bin(self):
        with open(bbl_bin) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.bin(row['BIN'])
                self.assertTrue(len(r['Latitude']) > 1 or len(r['Longitude']))

    def test_bbl(self):
        with open(bbl_bin) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.bbl(row['BORO CODE'], row['BLOCK'], row['LOT'])
                print(r['Message'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_parser(self):
        with open(address_unparsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                in_data = row['ADDRESS'] + ', ' + row['CITY'] + ', ' + row['ZIPCODE']
                r = g.address(address=in_data)
                print(r['Message'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_parser_with_boroname(self):
        with open(address_unparsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(address=row['ADDRESS'], boro=row['BORO NAME'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_parser_with_zipcode(self):
        with open(address_unparsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(address=row['ADDRESS'], zip_code=row['ZIPCODE'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_with_borocode(self):
        with open(address_parsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(house_number=row['BUILDING'], street_name=row['STREET'], boro=row['BORO CODE'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_with_boroname(self):
        with open(address_parsed) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(house_number=row['BUILDING'], street_name=row['STREET'], boro=row['BORO'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_with_zipcode(self):
        with open(address_parsed) as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                r = g.address(house_number=row['BUILDING'], street_name=row['STREET'], zip_code=row['ZIPCODE'])
                print(r['Message'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)


if __name__ == "__main__":
    unittest.main()
