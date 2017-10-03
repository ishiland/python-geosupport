from os import path
import unittest



try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "Unable to import setup tools. "
    )
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

def test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite

setup(
    name='python-geosupport',
    version='0.0.3',
    url='https://github.com/ishiland/python-geosupport',
    description='Python bindings for the NYC Geosupport Desktop application',
    long_description=long_description,
    author='Ian Shiland',
    author_email='ishiland@gmail.com',
    packages=['geosupport'],
    license='MIT',
    keywords = ['NYC', 'geocoder', 'python-geosupport', 'geosupport'],
    test_suite='tests',
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
    ]
)
