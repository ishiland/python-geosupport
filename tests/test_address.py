from geosupport import Geocode
import unittest
import csv

g = Geocode()


class TestAddressObject(unittest.TestCase):

    def test_address_borocode(self):
        with open(r'data/addresses.txt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address_borocode(house_number=row['HouseNumber'], street_name=row['StreetName'], boro_code=row['BoroCode'])
                print(r['Latitude'], r['Longitude'], r['Message'])

    def test_address_boroname(self):
        with open(r'data/addresses.txt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address_boroname(house_number=row['HouseNumber'], street_name=row['StreetName'], boro_name=row['BoroName'])
                print(r['Latitude'], r['Longitude'], r['Message'])

    def test_address_zipcode(self):
        with open(r'data/addresses.txt') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                r = g.address_zipcode(house_number=row['HouseNumber'], street_name=row['StreetName'], zip_code=row['ZipCode'])
                print(r['Latitude'], r['Longitude'], r['Message'])


if __name__ == "__main__":
    unittest.main()
