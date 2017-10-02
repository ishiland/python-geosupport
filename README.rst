python-geosupport
=================

python-geosupport is a Python package for using NYC Planning's `Geosupport Desktop Edition™`_.

**Currently this package only supports Windows x86 and x64 environments.** Future support of Linux is possible.


Getting Started
---------------

1. Download and install Geosupport Desktop Edition for Windows:

   * `Geosupport Desktop Edition for Windows (32-bit)`_
   * `Geosupport Desktop Edition for Windows (64-bit)`_

   **Note:** Ensure you select the correct Geosupport installation that corresponds to the Python interpreter you are using. Ex., Python 32-bit will only work with Geosupport 32-bit.

2. Install the python package:

   ``pip install python-geosupport``

3. Import the package and create an instance:

   ``import geosupport``

   ``g = geosupport.Geocode()``

4. Geocode some addresses:

   **Geocode by borough code**

   ``r = g.address_borocode(house_number=‘125’, street_name=‘Worth St’, boro_code=1)``

   **Geocode by borough name**

   ``r = g.address_boroname(house_number=‘125’, street_name=‘Worth St’, boro_name=‘MANHATTAN’)``

   **Geocode by zip code**

   ``r = g.address_zipcode(house_number=‘125’, street_name=‘Worth St’, zip_code=‘10013’)``


5. A dictionary of results is returned:

::

    {'2010 Census Block': '1012',
     '2010 Census Block Suffix': '',
     '2010 Census Tract': '31',
     'Assembly District': '65',
     'Atomic Polygon': '112',
     'B10SC First Borough and Street Code': '14549001010',
     'Bike Lane': '',
     'Borough Block Lot (BBL)': {'Borough code': '1',
                                 'Tax Block': '00168',
                                 'Tax Lot': '0032'},
     'Building Identification Number (BIN) of Input Address or NAP': '1001831',
     'City Council District': '01',
     'Community District': '101',
     'Community School District': '02',
     'Congressional District': '10',
     'DSNY Snow Priority Code': 'P',
     'Election District': '017',
     'First Borough Name': 'MANHATTAN',
     'House Number Display Format': '125',
     'House Number Sort Format': '000125000AA',
     'Hurricane Evacuation Zone (HEZ)': '4',
     'Latitude': '40.715428',
     'Longitude': '-74.002673',
     'Message': '',
     'NTA Name': 'SoHo-TriBeCa-Civic Center-Little Italy',
     'Neighborhood Tabulation Area (NTA)': 'MN24',
     'Police Precinct': '005',
     'Roadway Type': '1',
     'Second Street Name Normalized': 'WORTH STREET',
     'Spatial Coordinates of Segment': {'X Coordinate, High Address End': '0983664',
                                        'X Coordinate, Low Address End': '0983410',
                                        'Y Coordinate, High Address End': '0199828',
                                        'Y Coordinate, Low Address End': '0199983',
                                        'Z Coordinate, High Address End': '',
                                        'Z Coordinate, Low Address End': ''},
     'State Senatorial District': '26',
     'USPS Preferred City Name': 'NEW YORK',
     'X-Y Coordinates of Lot Centroid': '09835980200014',
     'XCoord': '0983509',
     'YCoord': '0199926',
     'Zip Code': '10013'}

Acknowledgments
---------------

Credits to `Charles Wang`_ who developed an initial proof of concept in
python based on `Chris Whong`_ and `Noah Veltman’s`_ work using Node.js


TODO
----
* Add linux support
* Add single line address input
* Add more Geosupport functions
* More tests

.. _Geosupport Desktop Edition™: https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page
.. _Geosupport Desktop Edition for Windows (32-bit): https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gde16b.zip
.. _Geosupport Desktop Edition for Windows (64-bit): https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gde6416b.zip
.. _Charles Wang: https://github.com/CharlesKWang/NYC-Geocoder
.. _Chris Whong: https://gist.github.com/chriswhong/2e5f0f41fc5d366ec902613251445b30
.. _Noah Veltman’s: https://github.com/veltman/node-geosupport