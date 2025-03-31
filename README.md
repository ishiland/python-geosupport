# python-geosupport 

![Build status](https://github.com/ishiland/python-geosupport/actions/workflows/ci.yml/badge.svg) [![PyPI version](https://img.shields.io/pypi/v/python-geosupport.svg)](https://pypi.python.org/pypi/python-geosupport/) [![3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/release/python-360/) 


Geocode NYC addresses locally using Python bindings for NYC Planning's [Geosupport Desktop Edition](https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-gde-home.page).

## Documentation 

Check out documentation for installing and usage [here](https://python-geosupport.readthedocs.io/en/latest/).

## Features

- Pythonic interface to all Geosupport functions
- Support for both Windows and Linux platforms
- Secure and fast using local geocoding - no API calls required 
- Built-in error handling for Geosupport return codes
- Interactive help menu

## Compatibility

- Python 3.8+
- Tested on Geosupport Desktop Edition 25a
- Windows (64-bit & 32-bit) and Linux operating systems

## Quickstart

```bash
pip install python-geosupport
```

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

## Examples

See the examples directory and accompanying [readme.md](examples/readme.md).


## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`python -m unittest discover`)
5. Run Black formatting (`black .`)
6. Commit your changes (`git commit -m 'Add some amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is licensed under the MIT License - see the [license.txt](license.txt) file for details
