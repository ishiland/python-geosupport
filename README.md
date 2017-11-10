# python-geosupport

A Python library for geocoding with NYC Planning's [Geosupport Desktop Edition](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page).
Developed using version `17C` of Geosupport Desktop Edition.


## Getting Started
### Prerequisites

Install Geosupport Desktop Edition:

   * [Geosupport Desktop Edition for Windows (32-bit)](http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gde_17c.zip)
   * [Geosupport Desktop Edition for Windows (64-bit)](http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gde64_17c.zip)
   * [Geosupport Desktop Edition for Linux](https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gdelx_17c.zip)

**Windows users:** Ensure you select the correct Geosupport installation that corresponds to the Python interpreter you are using. Ex., Python 32-bit will only work with Geosupport 32-bit.

Additionally, you should check that the following environmental variables are set:
* `GEOFILES` = the `fls` directory of your Geosupport installation. (ex. `C:\Program Files (x86)\Geosupport Desktop Edition\fls\`)
* The Geosupport `bin` directory is in the `PATH`. (ex. `C:\Program Files (x86)\Geosupport Desktop Edition\bin`)

**Linux users:** Extract the .zip to a folder of your choice and set the `GEOFILES` and `LD_LIBRARY_PATH` environmental variables of the `fls` and `lib` directories like so:

```shell
$ export GEOFILES=/var/geosupport/version-17c/fls
$ export LD_LIBRARY_PATH=/var/geosupport/version-17c/lib/
```

### How to use
1. Install via [pip](https://pip.readthedocs.io/en/latest/quickstart.html):
    ```python
    pip install python-geosupport
    ```

2. Import the library and create an instance:
    ```python
    from geosupport import Geocode

    g = Geocode()
    ```

3. Geocode with:

    **Single input street address**
    ```python
    result = g.address(address="125 Worth st, NY, NY")
    ```

    **Parsed street address** (Must provide zip code or borough)
    ```python
    result = g.address(house_number="125", street="Worth st", zip=10013)

    result = g.address(house_number="125", street="Worth st", boro='MANHATTAN')
     ```

    **Borough, Block, and Lot**
    ```python
    result = g.bbl(boro='1', block='00168', lot='0032')
    ```
    **BIN**
    ```python
    result = g.bin(bin='1001831')
    ```
    **Placename**
    ```python
    result = g.place(place='VAN CRTLANDT MANSION', boro='bronx')
    ```
    **Intersection**
    ```python
    result = g.intersection(street_1='ST NICHOLAS AVENUE', street_2='MENAHAN STREET', boro='QUEENS')
    ```
    **Street Segment**
    ```python
    result = g.street_segment(on_street='STORY AVENUE',
                              cross_street_1='EVERGREEN AVENUE',
                              cross_street_2='WHEELER AVENUE',
                              boro='BRONX')
    ```
    **Blockface**
    ```python
    result = g.blockface(on_street='STORY AVENUE',
                         cross_street_1='EVERGREEN AVENUE',
                         cross_street_2='WHEELER AVENUE',
                         boro='BRONX',
                         compass_direction='N')
    ```

    **Street Stretch**
    ```python
    result = g.street_stretch(on_street='CLIFTON PLACE',
                              cross_street_1='SAINT JAMES PLACE',
                              cross_street_2='GRAND AVENUE',
                              boro='BK',
                              compass_direction='N',
                              compass_direction_2='S')
    ```

    *The `boro` argument can be borough code, borough name or a common borough abbreviation.

### Running tests
```
>> python setup.py test
```

### Known Issues
* Single address inputs containing `Grand Concourse`  are not parsed correctly if they do not contain `NY` or `New York` in the string.
* Single address inputs with a space instead of a hyphen are not parsed correctly. Ex. `180 05 HILLSIDE AVE, QUEENS, 11432`

### TODO
* Improve single address input parsing
* Better data with compass direction for testing `blockface` and `street_stretch` methods.

## License

This project is licensed under the MIT License - see the [license.txt](license.txt) file for details

## Acknowledgments

* [Charles Wang](https://github.com/CharlesKWang/NYC-Geocoder) for his initial proof of concept in python
* [Chris Whong](https://gist.github.com/chriswhong/2e5f0f41fc5d366ec902613251445b30) and [Noah Veltman](https://github.com/veltman/node-geosupport) for their work using Node.js
* Datamade's [usaddress](https://github.com/datamade/usaddress)
