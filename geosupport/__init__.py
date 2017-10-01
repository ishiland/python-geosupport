import sys
from ctypes import cdll


class Geosupport(object):
    """
    All geocoding methods require House Number and Street Name. In addition, Boro Code, Boro Name or Zip code
    must be provided. Currently only function 1B is supported. See the Geosupport User Programming Guide for
    more information on function 1B.

    All geocoding methods return a dict of results.

    NOTE: Only Windows is supported at this time. Future support of Linux is possible.
    """

    def __init__(self):
        self.py_version = sys.version_info[0]
        if sys.platform == 'win32':
            self.geolib = cdll.LoadLibrary("NYCGEO.dll")
        # elif sys.platform == 'linux' or sys.platform == 'linux2':
        #     self.geolib = cdll.LoadLibrary("libgeo.so")
        else:
            raise Exception('This Operating System is currently not supported.')

    def _geocode(self, **kwargs):
        """
        :param func: Current only function 1B is supported. Function 1B processes an input address or input
        Non-Addressable Place name (NAP).
        :param kwargs: house_number and street_name are required. Additionally, Either boro_code or zip_code is required.
        :return: Returns
        """
        house_number = self._xstr(kwargs.get('house_number'))
        street_name = self._xstr(kwargs.get('street_name'))
        boro_code = self._xstr(kwargs.get('boro_code'))
        if len(boro_code) < 1:
            boro_code = ' '
        zip_code = self._xstr(kwargs.get('zip_code'))
        wa1 = '1B{}{}{}{}{}C{}{}'.format(self._rightpad(house_number, 16),
                                         self._rightpad('', 38),
                                         boro_code,
                                         self._rightpad('', 10),
                                         self._rightpad(street_name, 32),
                                         self._rightpad('', 113),
                                         self._rightpad(zip_code, 5))
        wa1 = self._rightpad(wa1, 1200)
        wa2 = self._rightpad('', 4300)
        if self.py_version == 3:
            wa1 = bytes(str(wa1), 'ascii')
            wa2 = bytes(str(wa2), 'ascii')
        self.geolib.NYCgeo(wa1, wa2)
        return self._parse(str(wa1), str(wa2))

    @staticmethod
    def _xstr(s):
        """
        :param s: String to be processed by Geosupport WA1 or WA2
        :return: Empty string if s is None.
        """
        if s is None:
            return ''
        return str(s).strip()

    def address_zipcode(self, house_number, street_name, zip_code):
        return self._geocode(house_number=house_number, street_name=street_name, zip_code=zip_code)

    def address_boroname(self, house_number, street_name, boro_name):
        """
        a dict to lookup a boro code if a boro name is provided.
        """
        boroughs = {'MANHATTAN': 1, 'MN': 1, 'NEW YORK': 1, 'NY': 1,
                    'BRONX': 2, 'THE BRONX': 2, 'BX': 2,
                    'BROOKLYN': 3, 'BK': 3, 'BKLYN': 3,
                    'QUEENS': 4, 'QN': 4,
                    'STATEN ISLAND': 5, 'SI': 5, 'STATEN IS': 5}

        if boro_name.upper() in boroughs:
            boro_code = boroughs[boro_name.upper()]
        else:
            boro_code = 0
        return self._geocode(house_number=house_number, street_name=street_name, boro_code=boro_code)

    def address_borocode(self, house_number, street_name, boro_code):
        return self._geocode(house_number=house_number, street_name=street_name, boro_code=boro_code)

    @staticmethod
    def _rightpad(field, length):
        """
        Creates a string of specified length, either by adding whitespace to the right, or concatenating
        """
        field = str(field)
        field_length = len(field)
        if field_length > length:
            field = field[:length]
        if field_length < length:
            while len(field) < length:
                field += ' '
        return field.upper()

    @staticmethod
    def _parse(wa1, wa2):
        """
        :param wa1: Work Area 1 from GeoSupport results
        :param wa2: Work Area 2 from GeoSupport results
        :return: Dictionary of results
        """
        output = {
            'First Borough Name': wa1[360:369].strip(),
            'House Number Display Format': wa1[369: 385].strip(),
            'House Number Sort Format': wa1[385: 396].strip(),
            'B10SC First Borough and Street Code': wa1[396: 407].strip(),
            'Second Street Name Normalized': wa1[407:439].strip(),
            'Community District': wa2[149:152].strip(),
            'Zip Code': wa2[152:157].strip(),
            'Election District': wa2[157:160].strip(),
            'Assembly District': wa2[160:162].strip(),
            'Congressional District': wa2[163:165].strip(),
            'State Senatorial District': wa2[165:167].strip(),
            'City Council District': wa2[169:171].strip(),
            'Police Precinct': wa2[191:194].strip(),
            'Community School District': wa2[203:205].strip(),
            'Atomic Polygon': wa2[205: 208].strip(),
            '2010 Census Tract': wa2[223: 229].strip(),
            '2010 Census Block': wa2[229:233].strip(),
            '2010 Census Block Suffix': wa2[233].strip(),
            'Neighborhood Tabulation Area (NTA)': wa2[245:249].strip(),
            'DSNY Snow Priority Code': wa2[249].strip(),
            'Hurricane Evacuation Zone (HEZ)': wa2[260:262].strip(),
            'Spatial Coordinates of Segment': {'X Coordinate, Low Address End': wa2[313:320].strip(),
                                               'Y Coordinate, Low Address End': wa2[320:327].strip(),
                                               'Z Coordinate, Low Address End': wa2[327:334].strip(),
                                               'X Coordinate, High Address End': wa2[334:341].strip(),
                                               'Y Coordinate, High Address End': wa2[341:348].strip(),
                                               'Z Coordinate, High Address End': wa2[348:355].strip(),
                                               },
            'Roadway Type': wa2[444:446].strip(),
            'Bike Lane': wa2[486].strip(),
            'NTA Name': wa2[553: 628].strip(),
            'USPS Preferred City Name': wa2[628:653].strip(),
            'Latitude': wa2[653:662].strip(),
            'Longitude': wa2[662: 673].strip(),
            'Borough Block Lot (BBL)': {'Borough code': wa2[1533].strip(),
                                        'Tax Block': wa2[1534:1539].strip(),
                                        'Tax Lot': wa2[1539:1543].strip(),
                                        },
            'Building Identification Number (BIN) of Input Address or NAP': wa2[1581:1588].strip(),
            'X-Y Coordinates of Lot Centroid': wa2[1699:1713].strip(),
            'XCoord': wa2[125:132].strip(),
            'YCoord': wa2[132:139].strip(),
            'Message': wa1[579:659].strip(),
        }
        return output
