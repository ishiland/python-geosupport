import sys
import usaddress
from usaddress import RepeatedLabelError, OrderedDict
from .parsers import *


class Geocode(object):
    def __init__(self):
        self.py_version = sys.version_info[0]
        try:
            self.platform = sys.platform
            if sys.maxsize > 2 ** 32:
                self.py_bit = '64'
            else:
                self.py_bit = '32'
            if self.platform == 'win32':
                if self.py_bit == '64':
                    from ctypes import cdll
                    self.geolib = cdll.LoadLibrary("NYCGEO.dll")
                else:
                    from ctypes import windll  # must use windll for 32-bit Windows binaries
                    self.geolib = windll.LoadLibrary("NYCGEO.dll")
            elif self.platform == 'linux' or self.platform == 'linux2':
                import os
                from ctypes import cdll
                self.geolib = cdll.LoadLibrary(os.path.join(os.environ['LD_LIBRARY_PATH'], "libgeo.so"))
            else:
                raise Exception('This Operating System is currently not supported.')
        except OSError as e:
            sys.exit(
                '{}\n'
                'You are currently using a {}-bit Python interpreter. Is the installed '
                'version of Geosupport {}-bit?'.format(e, self.py_bit, self.py_bit))

    def _call_geolib(self, wa1, wa2, func):
        """
        Calls the Geosupport libs & encodes/deocodes strings for Python 3.
        :param wa1: Work Area 1
        :param wa2: Work Area 2
        :param func: Function that determines the dictionary to return.
        :return: Dictionary of results
        """

        # encode
        if self.py_version == 3:
            wa1 = bytes(str(wa1), 'utf8')
            wa2 = bytes(str(wa2), 'utf8')

        # Call Geosupport libs
        if self.platform == 'win32':
            self.geolib.NYCgeo(wa1, wa2)  # windows
        else:
            self.geolib.geo(wa1, wa2)  # linux

        # decode
        if self.py_version == 3:
            wa1 = str(wa1, 'utf8')
            wa2 = str(wa2, 'utf8')

        return self._merge_wa(parse_WA1(wa1), globals()["parse_" + func](wa2))

    @staticmethod
    def _parse_sfs(ad):
        """
        Parses a single address input using the usaddress library. A work in progress.
        :param ad: usaddress parsed address
        :return: results
        """
        try:
            if ad[0]:
                house_number = ad[0].get('AddressNumber', None)
                street_name = ad[0].get('StreetName', None)
                if 'StreetNamePreDirectional' in ad[0]:
                    street_name = ad[0]['StreetNamePreDirectional'] + ' ' + street_name
                if 'StreetNamePreType' in ad[0]:
                    street_name = ad[0]['StreetNamePreType'] + ' ' + street_name
                if 'StreetNamePostType' in ad[0]:
                    street_name = street_name + ' ' + ad[0]['StreetNamePostType']
                zip_code = ad[0].get('ZipCode', None)
                city = ad[0].get('PlaceName', None)
                return {'houseNumber': house_number, 'streetName': street_name, 'zipCode': zip_code, 'city': city}
        except AttributeError as e:
            print(e)

    def address(self, address=None, house_number=None, street=None, zip=None, boro=None):
        """
        Function 1B processes an input address. Zip code, Boro code or Boro name must be provided in addition to a house
        number and street name.

        :param address: Input adddress to be parsed. Should include a house number and street name.
        :param house_number: Required if no address.
        :param street: Required if no address.
        :param zip: 5 digit postal code. Optional
        :param boro: borough name or borough code. Optional
        :return: dictionary of results
        """
        if address:
            try:
                usaddress_parsed = usaddress.tag(address)
            except RepeatedLabelError as r:
                usaddress_parsed = (OrderedDict([(t[1], t[0]) for t in r.parsed_string]), 'Street Address')
            parsed = self._parse_sfs(usaddress_parsed)
            if parsed:
                house_number = parsed.get('houseNumber', None)
                street = parsed.get('streetName', None)
                if boro:
                    if len(str(boro).strip()) > 1:
                        boro = self._borocode_from_boroname(boro)
                elif all(v is None for v in [zip, boro]):
                    zip = parsed.get('zipCode', None)
                    city = parsed.get('city', None)
                    if city:
                        boro = self._borocode_from_boroname(city)
        elif house_number and street:
            if boro:
                if len(str(boro).strip()) > 1:
                    boro = self._borocode_from_boroname(boro)
        func = '1B'
        wa1 = '{}{}{}{}{}{}'.format(func,
                                    self._rightpad(house_number, 54),
                                    self._rightpad(boro or ' ', 11),
                                    self._rightpad(street, 145),
                                    'C',
                                    zip)
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 4300
        return self._call_geolib(wa1, wa2, func)

    def place(self, place, boro):
        """
        Function 1B also processes a Non-Addressable Place name (NAP).
        :param boro: borough code or borough name
        :param place: A Non-Addressable Placename
        :return: a dictionary of results
        """
        if len(str(boro).strip()) > 1:
            boro = self._borocode_from_boroname(boro)
        func = '1B'
        wa1 = '{}{}{}{}'.format(self._rightpad(func, 56),
                                self._rightpad(boro, 11),
                                self._rightpad(place, 145),
                                'C')
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 4300
        return self._call_geolib(wa1, wa2, func)

    def bbl(self, boro, block, lot, tpad=True):
        """
        Function BL processes an input Borough, Block and Lot.
        :param boro: borough code or borough name
        :param block: tax block
        :param lot: tax lot
        :param tpad: tpad switch (optional)
        :return: a dictionary of results
        """
        if len(str(boro).strip()) > 1:
            boro = self._borocode_from_boroname(boro)
        if tpad:
            tpad = 'Y'
        else:
            tpad = 'N'
        func = 'BL'
        wa1 = '{}{}{}{}{}'.format(self._rightpad(func, 185),
                                  boro,
                                  self._rightpad(block, 5),
                                  self._rightpad(lot, 137),
                                  tpad)
        # Long Work Area 2 Flag - 315 'L'
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 1363
        return self._call_geolib(wa1, wa2, '1A_' + func + '_BN')

    def bin(self, bin, tpad=True):
        """
        Function BN processes an input Building Identification Number (BIN).
        :param bin: input BIN (required)
        :param tpad: TPAD Flag (optional)
        :return: results
        """
        if tpad:
            tpad = 'Y'
        else:
            tpad = 'N'
        func = 'BN'
        wa1 = '{}{}{}'.format(self._rightpad(func, 196),
                              self._rightpad(bin, 126),
                              tpad)
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 1363
        return self._call_geolib(wa1, wa2, '1A_BL_' + func)

    def intersection(self, street_1, street_2, boro, boro_2=None, compass_direction=None, node_number=None):
        """
        Function 2W processes input cross streets.
        :param street_1: Intersection Street 1
        :param street_2: Intersection Street 2
        :param boro: borough code or borough name
        :param boro_2: borough code or borough name of street_2 (optional)
        :param compass_direction: Used to request information about only one side of the
            street. Valid values are: N, S, E or W (optional)
        :param node_number: (optional)
        :param snl: Street Name Normalization Length Limit (optional)
        :return: Dict of results
        """
        if len(str(boro).strip()) > 1:
            boro = self._borocode_from_boroname(boro)
        func = '2W'
        wa1 = '{}{}{}{}{}{}{}{}'.format(self._rightpad(func, 56),
                                        self._rightpad(boro or ' ', 11),
                                        self._rightpad(street_1, 32),
                                        self._rightpad(boro_2 or ' ', 11),
                                        self._rightpad(street_2, 93),
                                        self._rightpad(compass_direction or ' ', 2),
                                        self._rightpad(node_number or ' ', 7),
                                        self._rightpad('C', 107)
                                        )
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 4000
        return self._call_geolib(wa1, wa2, func)

    def street_segment(self, on_street, cross_street_1, cross_street_2, boro, cross_street_1_boro=None,
                       cross_street_2_boro=None, compass_direction=None):
        """
        Function 3 processes Street Segment Defined by 'ON' Street and Two Cross Streets

        :param on_street: street name of target street segment
        :param cross_street_1: First cross street of street segment
        :param cross_street_2: Second cross street of street segment
        :param boro: borough code or borough name
        :param cross_street_1_boro: Borough of first cross street (optional)
        :param cross_street_2_boro: Borough of second cross street (optional)
        :param compass_direction: Used to request information about only one side of the
            street. Valid values are: N, S, E or W (optional)
        :return: Dictionary of results
        """
        if len(str(boro).strip()) > 1:
            boro = self._borocode_from_boroname(boro)

        if cross_street_1_boro and len(str(cross_street_1_boro).strip()) > 1:
            cross_street_1_boro = self._borocode_from_boroname(cross_street_1_boro)

        if cross_street_2_boro and len(str(cross_street_2_boro).strip()) > 1:
            cross_street_2_boro = self._borocode_from_boroname(cross_street_2_boro)
        func = '3'
        wa1 = '{}{}{}{}{}{}{}{}{}{}'.format(self._rightpad(func, 56),  # 1-2
                                            self._rightpad(boro or ' ', 11),  # 57
                                            self._rightpad(on_street, 32),  # 68-99
                                            self._rightpad(cross_street_1_boro or ' ', 11),  # 100
                                            self._rightpad(cross_street_1, 32),  # 111-142
                                            self._rightpad(cross_street_2_boro or ' ', 11),  # 143
                                            self._rightpad(cross_street_2, 50),  # 154-185
                                            self._rightpad(compass_direction or ' ', 9),  # 204
                                            self._rightpad('C', 117),  # 213 (Work Area Format Indicator)
                                            'X')  # extended mode
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 1000
        return self._call_geolib(wa1, wa2, func)

    def blockface(self, on_street, cross_street_1, cross_street_2, boro, compass_direction, cross_street_1_boro=None,
                  cross_street_2_boro=None):
        """
        Function 3C processes Blockface Defined by 'ON' Street, Two Cross Streets and Compass Direction

        :param on_street: street name of target blockface
        :param cross_street_1: First cross street of blockface
        :param cross_street_2: Second cross street of blockface
        :param boro: borough code or borough name
        :param cross_street_1_boro: Borough of first cross street (optional)
        :param cross_street_2_boro: Borough of second cross street (optional)
        :param compass_direction: Used to request information about only one side of the
            street. Valid values are: N, S, E or W (optional)
        :return: Dictionary of results
        """
        if len(str(boro).strip()) > 1:
            boro = self._borocode_from_boroname(boro)

        if cross_street_1_boro and len(str(cross_street_1_boro).strip()) > 1:
            cross_street_1_boro = self._borocode_from_boroname(cross_street_1_boro)

        if cross_street_2_boro and len(str(cross_street_2_boro).strip()) > 1:
            cross_street_2_boro = self._borocode_from_boroname(cross_street_2_boro)

        func = '3C'
        wa1 = '{}{}{}{}{}{}{}{}{}'.format(self._rightpad(func, 56),
                                          self._rightpad(boro or ' ', 11),
                                          self._rightpad(on_street, 32),
                                          self._rightpad(cross_street_1_boro or ' ', 11),
                                          self._rightpad(cross_street_1, 32),
                                          self._rightpad(cross_street_2_boro or ' ', 11),
                                          self._rightpad(cross_street_2, 50),
                                          self._rightpad(compass_direction or ' ', 9),
                                          self._rightpad('C', 117),  # 213 (Work Area Format Indicator)
                                          'X')  # extended mode
                                            # Cross Street Names Flag 323
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 850
        return self._call_geolib(wa1, wa2, func)

    def street_stretch(self, on_street, cross_street_1, cross_street_2, boro, compass_direction, compass_direction_2,
                       cross_street_1_boro=None, cross_street_2_boro=None):
        """
        Function 3S processes Street Stretch Defined by 'ON' Street and Optionally Two Cross Streets

        :param on_street: street name of target street stretch
        :param cross_street_1: First cross street of street stretch
        :param cross_street_2: Second cross street of street stretch
        :param boro: borough code or borough name
        :param cross_street_1_boro: Borough of first cross street (optional)
        :param cross_street_2_boro: Borough of second cross street (optional)
        :param compass_direction: Used to request information about only one side of the
            street. Valid values are: N, S, E or W (optional)
        :return: Dictionary of results
        """
        if len(str(boro).strip()) > 1:
            boro = self._borocode_from_boroname(boro)

        if cross_street_1_boro and len(str(cross_street_1_boro).strip()) > 1:
            cross_street_1_boro = self._borocode_from_boroname(cross_street_1_boro)

        if cross_street_2_boro and len(str(cross_street_2_boro).strip()) > 1:
            cross_street_2_boro = self._borocode_from_boroname(cross_street_2_boro)

        func = '3S'
        wa1 = '{}{}{}{}{}{}{}{}{}'.format(self._rightpad(func, 56),
                                          self._rightpad(boro or ' ', 11),
                                          self._rightpad(on_street, 32),
                                          self._rightpad(cross_street_1_boro or ' ', 11),
                                          self._rightpad(cross_street_1, 32),
                                          self._rightpad(cross_street_2_boro or ' ', 11),
                                          self._rightpad(cross_street_2, 50),
                                          compass_direction or ' ',
                                          self._rightpad(compass_direction_2 or ' ', 8),
                                          self._rightpad('C', 117),
                                          )
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 19274
        return self._call_geolib(wa1, wa2, func)

    def address_point(self, address=None, house_number=None, street=None, zip=None, boro=None):
        """
        Function AP processes an input address point. Must be a valid actual address.
        Zip code, Boro code or Boro name must be provided in addition to a house number and street name.
        :param address: Input adddress to be parsed. Should include a house number and street name.
        :param house_number: Required if no address.
        :param street: Required if no address.
        :param zip: 5 digit postal code. Optional
        :param boro: borough name or borough code. Optional
        :return: dictionary of results
        """
        if address:
            try:
                usaddress_parsed = usaddress.tag(address)
            except RepeatedLabelError as r:
                usaddress_parsed = (OrderedDict([(t[1], t[0]) for t in r.parsed_string]), 'Street Address')
            parsed = self._parse_sfs(usaddress_parsed)
            if parsed:
                house_number = parsed.get('houseNumber', None)
                street = parsed.get('streetName', None)
                if boro:
                    if len(str(boro).strip()) > 1:
                        boro = self._borocode_from_boroname(boro)
                elif all(v is None for v in [zip, boro]):
                    zip = parsed.get('zipCode', None)
                    city = parsed.get('city', None)
                    if city:
                        boro = self._borocode_from_boroname(city)
        elif house_number and street:
            if boro:
                if len(str(boro).strip()) > 1:
                    boro = self._borocode_from_boroname(boro)
        func = 'AP'
        wa1 = '{}{}{}{}{}{}{}'.format(func,
                                      self._rightpad(house_number, 54),
                                      self._rightpad(boro or ' ', 11),
                                      self._rightpad(street, 145),
                                      'C',
                                      self._rightpad(zip, 116),
                                      'X')
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 2800
        return self._call_geolib(wa1, wa2, func)

    @staticmethod
    def _borocode_from_boroname(name):
        """
        a dictionary to lookup boro codes.
        :param name: Borough name
        :return: Borough code
        """
        name = name.strip()
        boroughs = {'MANHATTAN': 1, 'MN': 1, 'NEW YORK': 1, 'NY': 1,
                    'BRONX': 2, 'THE BRONX': 2, 'BX': 2,
                    'BROOKLYN': 3, 'BK': 3, 'BKLYN': 3, 'KINGS': 3,
                    'QUEENS': 4, 'QN': 4, 'QU': 4,
                    'STATEN ISLAND': 5, 'SI': 5, 'STATEN IS': 5, 'RICHMOND': 5}
        if name.upper() in boroughs:
            boro_code = boroughs[name.upper()]
        else:
            boro_code = None
        return boro_code

    @staticmethod
    def _rightpad(field, length):
        """
        Creates a string of specified length by adding whitespace to the right
        """
        field = str(field) + (' ' * (length - len(str(field))))
        return field.upper()

    def _merge_wa(self, wa1, wa2):
        """
         Merge wa1, wa2 results
        :param wa1: Work Area 1 results
        :param wa2: Work Area 2 results
        :return: merged work area 1 & 2 results
        """
        wa = wa1.copy()
        wa.update(wa2)
        return {key: self.strip_dict(value)
        if isinstance(value, dict)
        else value.strip() for key, value in wa.items()}

    def strip_dict(self, d):
        """
        Strips white space from geosupport results
        :param d: dictionary
        :return: dictionary w/ white space striped
        """
        return {key: self.strip_dict(value)
        if isinstance(value, dict)
        else value.strip()
                for key, value in d.items()}
