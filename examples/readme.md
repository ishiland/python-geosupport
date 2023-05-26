# Geosupport Examples

Some examples to demonstrate different usages of python-geosupport. 

## Using Docker
Use NYC Plannings [docker-geosupport](https://github.com/NYCPlanning/docker-geosupport) image to geocode your data.

> nycplanning/docker-geosupport image will be automatically updated whenever there's a new major release or upad release on Bytes of the Big Apple

### Build
```shell
docker build . -t geosupport-examples 
```

### Run
From this directory, you can run: 
```shell
docker run -it --rm --volume ${PWD}:/examples geosupport-examples pandas_simple.py 

docker run -it --rm --volume ${PWD}:/examples geosupport-examples pandas_multiprocessing.py 
```

The outputs will be in the *./data* directory. 