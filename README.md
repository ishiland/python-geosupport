# python-geosupport [![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-2714/) [![Python 3+](https://img.shields.io/badge/python-3+-blue.svg)](https://www.python.org/downloads/release/python-360/) [![PyPI version](https://img.shields.io/pypi/v/python-geosupport.svg)](https://pypi.python.org/pypi/python-geosupport/)

Python bindings for NYC Planning's [Geosupport Desktop Edition](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page).


## Installation
### Prerequisites

Install Geosupport Desktop Edition (tested with version 18b):

   * [Geosupport Desktop Edition for Windows (32-bit)](http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gde_18b.zip)
   * [Geosupport Desktop Edition for Windows (64-bit)](http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gde64_18b.zip)
   * [Geosupport Desktop Edition for Linux](https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/gdelx_18b.zip)

#### Windows
**Important**: Ensure you select the correct Geosupport installation that corresponds to the Python interpreter you are using. Ex., Python 32-bit will only work with Geosupport 32-bit.

Additionally, you should check that the following environmental variables are set:
* `GEOFILES` = the `fls` directory of your Geosupport installation. (ex. `C:\Program Files (x86)\Geosupport Desktop Edition\fls\`)
* The Geosupport `bin` directory is in the `PATH`. (ex. `C:\Program Files (x86)\Geosupport Desktop Edition\bin`)

#### Linux
Extract the .zip to a folder of your choice and set the `GEOFILES` and `LD_LIBRARY_PATH` environmental variables of the `fls` and `lib` directories:

```shell
$ export GEOFILES=/var/geosupport/version-17c/fls
$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/var/geosupport/version-17c/lib/
```

### Install python-geosupport

Install via [pip](https://pip.readthedocs.io/en/latest/quickstart.html):

```shell
$ pip install python-geosupport
```

Or clone this repository and:

```shell
$ python setup.py install
```

## Usage

### Examples

#### Basic Usage

```python
# Import the library and create a `Geosupport` object.
from geosupport import Geosupport
g = Geosupport()

# Call the address processing function by name
result = g.address(house_number=125, street_name='Worth St', borough_code='Mn')
```

`result` is a dictionary with the output from Geosupport. For example:

```
{
    '2010 Census Block': '1012',
    '2010 Census Tract': '31',
    'Assembly District': '65',
    'Atomic Polygon': '112',
    'B10SC - First Borough and Street Code': '14549001010',
    'BOE Preferred B7SC': '14549001',
    'BOE Preferred Street Name': 'WORTH STREET',
    'BOROUGH BLOCK LOT (BBL)': {
        'BOROUGH BLOCK LOT (BBL)': '1001680032',
        'Borough Code': '1',
        'Tax Block': '00168',
        'Tax Lot': '0032'
    },
    'Blockface ID': '0212261942',
    ...
}
```

#### Calling Geosupport functions

python-geosupport is flexible with how you call functions. You can use either
Geosupport function codes or human readable alternate names, and access them
either through python object attribute notation or dictionary item notation:

```python
# Different ways of calling function 3S which processes street stretches
g.street_stretch(...)
g['street_stretch'](...)
g['3S'](...)
g.call({'function': '3S', ...})
g.call(function='3S', ...)
```

You can pass arguments as a dictionary, keyword arguments.

```python
# Use a dictionary with short names
g.street_stretch({'borough_code': 'MN', 'on': '1 Av', 'from': '1 st', 'to': '2 st'})
# Use keyword arguments with short names
g.street_stretch(
    borough_code='MN', street_name_1='1 Av',
    street_name_2='1 st', street_name_3='9 st'
)
# Use dictionary with full names
g.street_stretch({
    'Borough Code-1': 'MN',
    'Street Name-1': '1 Av',
    'Street Name-2': '1 st',
    'Street Name-3': '9 st'
})
```

#### Mode

A number of Geosupport functions support several modes: Exetended, Long, and
TPAD Long. You can set the flags individually as you would with using Geosupport
directly, but python-geosupport makes it easier with the `mode` argument. `mode`
can be one of `regular` (default), `extended`, `long` and `long+tpad`.

```python
# Call BL (Block and Lot) function in long mode
g.BL(mode='long', ...)
g.BL(mode='long+tpad', ...) # With TPAD

# Call 3 (Street Segment) function in extended mode
g.street_segment(mode='extended', ...)
```

#### Interactive Help

Full function help can be viewed by calling `g.help()`.

```python
# View an overview of all the functions available:
g.help()

# View help for an individual function including a description, inputs, outputs,
# and valid modes.
g.address.help()
g.help('address')

# View a list of all possible inputs to Geosupport
g.help('input')
```

#### Error Handling

python-geosupport will raise a `GeosupportError` when Geosupport returns an
error code.  Sometimes there is more information returned, in which case the
exception will have a `result` dictionary.

```python
from geosupport import GeosupportError

try:
    g.get_street_code(borough='MN', street='Wort Street')
except GeosupportError as e:
    print(e) # 'WORT STREET' NOT RECOGNIZED. THERE ARE 010 SIMILAR NAMES.
    print(e.result['List of Street Names']) # List of suggested alternate names
```

#### Switching Between Multiple Versions of Geosupport

:heavy_exclamation_mark: *This feature is Windows only.  Linux doesn't support 
library path modifications during runtime.*

If you have multiple versions of geosupport and want to switch between them,
you can either pass the installation path to `Geosupport`:

```python
g = Geosupport(geosupport_path="C:\\Program Files\\Geosupport 18C")
```

or create a `.python-geosupport.cfg` in your home directory that specifies
the names and installation paths of the different versions.

The `.python-geosupport.cfg` file looks like:

```txt
[versions]
18b=C:\Program Files\Geosupport Desktop Edition
18c=C:\Program Files\Geosupport 18C
18c_32=C:\Program Files (x86)\Geosupport 18C
```

Then you can select the version by name:

```python
g = Geosupport(geosupport_version="18c")
```

## Development

### Running tests
```shell
$ python setup.py test
```

Installing the dev dependencies (`nosetests` and `invoke`) will give you more
control over running tests. Install in develop mode with dev dependencies with:

```shell
$ pip install -e .[dev]
```

And then run tests with:

```shell
$ invoke test unit
$ invoke test functional
$ invoke test all
```



## License

This project is licensed under the MIT License - see the [license.txt](license.txt) file for details

## Contributors
Thanks to [Jeremy Neiman](https://github.com/docmarionum1) for a major revision incorporating all Geosupport functions and parameters.

If you see an issue or would like to contribute, pull requests are welcome.
