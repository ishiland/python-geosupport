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
    version='1.0.1',
    url='https://github.com/ishiland/python-geosupport',
    description='Python bindings for NYC Geosupport Desktop Edition',
    long_description="""
        # Import the library and create a `Geosupport` object.
        from geosupport import Geosupport
        g = Geosupport()
        
        # Call the address processing function by name
        result = g.address(house_number=125, street_name='Worth St', borough_code='Mn')
        """,
    author='Ian Shiland',
    author_email='ishiland@gmail.com',
    packages=['geosupport'],
    include_package_data=True,
    license='MIT',
    keywords=['NYC', 'geocoder', 'python-geosupport', 'geosupport'],
    classifiers=[
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite="tests",
    extras_require={
        'dev': [
            'coverage',
            'invoke>=1.1.1',
            'nose'
        ]
    }
)
