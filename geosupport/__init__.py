import sys
from .wa_parsers import _parseWA1, _parseWA2_1A_BL_BN, _parseWA2_1B
import usaddress
from usaddress import RepeatedLabelError, OrderedDict


class Geocode(object):
    """
    All geocoding methods require House Number and Street Name. In addition, Boro Code, Boro Name or Zip code
    must be provided. Currently only function 1B is supported. See the Geosupport User Programming Guide for
    more information.
    All geocoding methods return a dictionary of results.
    """

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
        Calls the Geosupport libs. Encodes and deocodes strings for Python 3.
        :param wa1: Work Area 1
        :param wa2: Work Area 2
        :param func: Function that determines the dictionary to return.
        :return: Dictionary of results
        """

        # encode
        if self.py_version == 3:
            wa1 = bytes(str(wa1), 'ascii')
            wa2 = bytes(str(wa2), 'ascii')

        # Call Geosupport libs
        if self.platform == 'win32':
            self.geolib.NYCgeo(wa1, wa2)  # windows
        else:
            self.geolib.geo(wa1, wa2)  # linux

        # decode
        if self.py_version == 3:
            wa1 = str(wa1, 'ascii')
            wa2 = str(wa2, 'ascii')

        return self._merge_wa(_parseWA1(wa1), globals()["_parseWA2_" + func](wa2))


    @staticmethod
    def _parse_sfs(ad):
        """
        Parses a single address input from the usaddress package. A work in progress.
        :param ad: usaddress parsed address
        :return: results
        """
        try:
            if ad[0]:
                if 'AddressNumber' in ad[0]:
                    house_number = ad[0]['AddressNumber']
                else:
                    raise Exception('No address number detected in single field search string')
                if 'StreetName' in ad[0]:
                    street_name = ad[0]['StreetName']
                else:
                    raise Exception('No street name detected in single field search string')
                if 'StreetNamePreDirectional' in ad[0]:
                    street_name = ad[0]['StreetNamePreDirectional'] + ' ' + street_name
                if 'StreetNamePreType' in ad[0]:
                    street_name = ad[0]['StreetNamePreType'] + ' ' + street_name
                if 'StreetNamePostType' in ad[0]:
                    street_name = street_name + ' ' + ad[0]['StreetNamePostType']
                if 'ZipCode' in ad[0]:
                    zip_code = ad[0]['ZipCode']
                else:
                    zip_code = None
                if 'PlaceName' in ad[0]:
                    city = ad[0]['PlaceName']
                else:
                    city = None
                return {'houseNumber': house_number, 'streetName': street_name, 'zipCode': zip_code, 'city': city}
            else:
                raise Exception('No data')
        except AttributeError as e:
            print(e)

    def address(self, address=None, house_number=None, street_name=None, zip_code=None, boro=None):
        """
        Function 1B processes an input address or input Non-Addressable Place name (NAP).
        Zip code, Boro code or Boro name must be provided in addition to a house number and street name.
        :param address: Input adddress to be parsed. Should include a house number and street name.
        :param house_number: Required if no address
        :param street_name: Required if no address
        :param zip_code:  Optional
        :param boro_code: Optional
        :param boro_name: Optional
        :return: results
        """
        if address:
            try:
                usaddress_parsed = usaddress.tag(address)
            except RepeatedLabelError as r:
                usaddress_parsed = (OrderedDict([(t[1], t[0]) for t in r.parsed_string]), 'Street Address')
            parsed = self._parse_sfs(usaddress_parsed)
            if parsed:
                if 'houseNumber' in parsed:
                    house_number = parsed['houseNumber']
                else:
                    raise Exception('No house number detected in:\n' + address)
                street_name = parsed['streetName']
                if boro:
                    if len(str(boro).strip()) > 1:
                        boro = self._borocode_from_boroname(boro)
                    # boro_code = self._borocode_from_boroname(boro_name)
                elif all(v is None for v in [zip_code, boro]):
                    if 'zipCode' in parsed:
                        zip_code = parsed['zipCode']
                    elif 'city' in parsed:
                        boro = self._borocode_from_boroname(parsed['city'])
                    else:
                        raise Exception('Must provide a valid zip code, boro code or boro name.')
        elif house_number and street_name:
            if boro:
                if len(str(boro).strip()) > 1:
                    boro = self._borocode_from_boroname(boro)
            elif all(v is None for v in [zip_code, boro]):
                raise Exception('Must provide a valid zip code, boro code or boro name.')
        else:
            raise Exception('Must provide an address or house number and street name.')
        func = '1B'
        wa1 = '1B{}{}{}{}{}C{}{}'.format(self._rightpad(house_number, 16),
                                         ' ' * 38,
                                         boro or ' ',
                                         ' ' * 10,
                                         self._rightpad(street_name, 32),
                                         ' ' * 113,
                                         self._rightpad(zip_code, 5))
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 4300
        return self._call_geolib(wa1, wa2, func)

    def bbl(self, boro, block, lot, tpad=True):
        """
        Function BL processes an input Borough, Block and Lot.
        :param boro: input boro code (required)
        :param block: input block (required)
        :param lot: input lot (required)
        :param tpad: tpad switch (optional)
        :return: results
        """

        if len(str(boro).strip()) > 1:
            boro = self._borocode_from_boroname(boro)

        if tpad:
            tpad = 'Y'
        else:
            tpad = 'N'
        wa1 = '{}{}{}{}{}'.format(self._rightpad('BL', 185),
                                  str(boro),
                                  self._rightpad(block, 5),
                                  self._rightpad(lot, 137),
                                  tpad)
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 1363
        return self._call_geolib(wa1, wa2, '1A_BL_BN')

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
        wa1 = '{}{}{}'.format(self._rightpad('BN', 196),
                              self._rightpad(bin, 126),
                              tpad)
        # wa1 = self._rightpad(wa1, 1200)
        wa1 = self._rightpad(wa1, 1200)
        wa2 = ' ' * 1363
        return self._call_geolib(wa1, wa2, '1A_BL_BN')

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
                    'QUEENS': 4, 'QN': 4,
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
        field = str(field)
        field = field + (' ' * (length - len(field)))
        return field.upper()

    @staticmethod
    def _merge_wa(wa1, wa2):
        """ Merge wa1 and wa2 results as a shallow copy. """
        wa = wa1.copy()
        wa.update(wa2)
        return wa
