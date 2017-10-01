import os

try:
    from distutils.core import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    version='1.0',
    url='https://github.com/ishiland/python-geosupport',
    description='Python bindings for the NYC Geosupport Desktop application',
    name='python-geosupport',
    author='Ian Shiland',
    author_email='ishiland@gmail.com',
    packages=['geosupport'],
    license='MIT',
    long_description=read('README.rst'),
    keywords = ['NYC', 'geocoder', 'python-geosupport', 'geosupport'], # arbitrary keywords
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
