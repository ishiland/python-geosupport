# Geosupport Examples

Example scripts demonstrating python-geosupport usage.

## Running Examples

### Basic Usage

```bash
# Run any example directly
python handle_similar_street_names.py
python pandas_simple.py
python pandas_multiprocessing.py
```

### Available Examples

| Example | Description |
|---------|-------------|
| `handle_similar_street_names.py` | Extract similar street names when Geosupport returns a "NOT RECOGNIZED" error |
| `pandas_simple.py` | Geocode addresses in a pandas DataFrame |
| `pandas_multiprocessing.py` | Parallel geocoding using multiprocessing for large datasets |

## Using Docker

NYC Planning's [docker-geosupport](https://github.com/NYCPlanning/docker-geosupport) image includes python-geosupport pre-installed.

```bash
# Build the examples container
docker build . -t geosupport-examples 

# Run examples
docker run -it --rm --volume ${PWD}:/examples geosupport-examples pandas_simple.py 
docker run -it --rm --volume ${PWD}:/examples geosupport-examples pandas_multiprocessing.py 
```

Output files will be saved to `./data/` directory.