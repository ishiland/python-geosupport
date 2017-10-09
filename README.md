# python-geosupport

A Python package for using NYC Planning's [Geosupport Desktop Edition](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page).



## Getting Started
### Prerequisites

Install Geosupport Desktop Edition:

   * [Geosupport Desktop Edition for Windows (32-bit)](https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gde16b.zip)
   * [Geosupport Desktop Edition for Windows (64-bit)](https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gde6416b.zip)
   * [Geosupport Desktop Edition for Linux](https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gdelx16b.zip)

**Windows users:** Ensure you select the correct Geosupport installation that corresponds to the Python interpreter you are using. Ex., Python 32-bit will only work with Geosupport 32-bit.

**Linux users:** Extract the .zip to a folder of your choice and set the ``GEOFILES`` and ``LD_LIBRARY_PATH`` environmental variables of the ``fls`` and ``lib`` directories like so:

```shell
$ export GEOFILES=/var/geosupport/version-16c_16.3/fls
$ export LD_LIBRARY_PATH=/var/geosupport/version-16c_16.3/lib/
```

### How to use
1. Install via [pip](https://pip.readthedocs.io/en/latest/quickstart.html):
    ```python
    pip install python-geosupport
    ```

2. Import the package and create an instance:
    ```python
    import geosupport
    g = geosupport.Geocode()
    ```

3. Geocode with:

    **Single input street address**
    ```python
    r = g.address("125 Worth st NY, NY, 10013")
    print(r['Latitude'], r['Longitude'])  # ('40.715428', '-74.002673')
    ```

    **Parsed street address** (Must provide zip code, borough name or borough code)
    ```python
    r = g.address(house_number="125", street_name="Worth st", zip_code=10013)
    print(r['Latitude'], r['Longitude'])  # ('40.715428', '-74.002673')
    r = g.address(house_number="125", street_name="Worth st", boro=1)
    print(r['Latitude'], r['Longitude'])  # ('40.715428', '-74.002673')
    r = g.address(house_number="125", street_name="Worth st", boro='Manhattan')
    print(r['Latitude'], r['Longitude'])  # ('40.715428', '-74.002673')
    ```

    **Borough, Block, and Lot**
    ```python
    r = g.bbl('1','00168','0032')
    print(r['Latitude'], r['Longitude'])  # ('40.71566', '-74.002352')
    r = g.bbl('Manhattan','00168','0032')
    print(r['Latitude'], r['Longitude'])  # ('40.71566', '-74.002352')
    ```
    **BIN (Building Identification Number)**
    ```python
    r = g.bin('1001831')
    print(r['Latitude'], r['Longitude'])  # ('40.71566', '-74.002352')
    ```

4. For all available outputs, see [geosupport/wa_parsers.py](https://github.com/ishiland/python-geosupport/tree/master/geosupport/wa_parsers.py).

### Running tests
```
>> python setup.py test
```

### Known Issues
* Single address inputs containing `Grand Concourse`  are not parsed correctly if they do not contain `NY` or `New York` in the string.
* Single address inputs with a space instead of a hyphen are not parsed correctly. Ex. `180 05 HILLSIDE AVE, QUEENS, 11432`

### TODO
* Improve single address input parsing
* Verify all WA outputs are correct and complete
* Add more Geosupport functions
* More tests, unique test data

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Charles Wang](https://github.com/CharlesKWang/NYC-Geocoder) for his initial proof of concept in python
* [Chris Whong](https://gist.github.com/chriswhong/2e5f0f41fc5d366ec902613251445b30) and [Noah Veltman](https://github.com/veltman/node-geosupport) for their work using Node.js
* Datamade's [usaddress](https://github.com/datamade/usaddress)
