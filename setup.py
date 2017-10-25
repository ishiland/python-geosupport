from os import path

try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )

here = path.abspath(path.dirname(__file__))

setup(
    name='python-geosupport',
    version='0.0.8',
    url='https://github.com/ishiland/python-geosupport',
    description='Python bindings for the NYC Geosupport Desktop application',
    long_description="""
Call NYC Planning's Geosupport Desktop functions from Python.

Ex:
    >>> import geosupport
    >>> g = geosupport.Geocode()
    >>> g.address("125 Worth st NY, NY, 10013")
    {'Latitude': '40.715428',
     'Longitude': '-74.002673',
    ...}
    """,
    author='Ian Shiland',
    author_email='ishiland@gmail.com',
    packages=['geosupport', 'geosupport/parsers'],
    license='MIT',
    keywords = ['NYC', 'geocoder', 'python-geosupport', 'geosupport'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite="tests",
    install_requires=['usaddress']
)
