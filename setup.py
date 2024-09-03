
try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "setuptools module required, please go to "
        "https://pypi.python.org/pypi/setuptools and follow the instructions "
        "for installing setuptools"
    )


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-geosupport',
    version='1.0.10',
    url='https://github.com/ishiland/python-geosupport',
    description='Python bindings for NYC Geosupport Desktop Edition',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Ian Shiland, Jeremy Neiman',
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
