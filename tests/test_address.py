from geosupport import Geocode
import unittest
import csv
from os import path

g = Geocode()

here = path.abspath(path.dirname(__file__))

address_data = path.join(here,'data','addresses.csv')


class TestGeocodeObject(unittest.TestCase):

    def test_bin(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.bin(row['Bin'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_bbl(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.bbl(row['BoroCode'], row['Block'], row['Lot'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_parser(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                in_data = row['SingleAddress'] + ', ' + row['City'] + ', ' + row['ZipCode']
                r = g.address(address=in_data)
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_parser_with_borocode(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(address=row['SingleAddress'], boro=row['BoroCode'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)


    def test_address_parser_with_boroname(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(address=row['SingleAddress'], boro=row['BoroName'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_parser_with_zipcode(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(address=row['SingleAddress'], zip_code=row['ZipCode'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_with_borocode(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(house_number=row['BuildingNumber'], street_name=row['Street'], boro=row['BoroCode'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_with_boroname(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(house_number=row['BuildingNumber'], street_name=row['Street'], boro=row['BoroName'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)

    def test_address_with_zipcode(self):
        with open(address_data) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address(house_number=row['BuildingNumber'], street_name=row['Street'], zip_code=row['ZipCode'])
                self.assertFalse(len(r['Latitude']) < 1 or len(r['Longitude']) < 1)


if __name__ == "__main__":
    unittest.main()
