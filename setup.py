from os import path

here = path.abspath(path.dirname(__file__))

try:
    from distutils.core import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-geosupport',
    version='0.0.2',
    url='https://github.com/ishiland/python-geosupport',
    description='Python bindings for the NYC Geosupport Desktop application',
    long_description=long_description,
    author='Ian Shiland',
    author_email='ishiland@gmail.com',
    packages=['geosupport'],
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
    ]
)
