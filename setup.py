import re
import os
from setuptools import setup, find_packages

# Read the version from the __init__.py file
with open(os.path.join("geosupport", "__init__.py"), "r", encoding="utf-8") as f:
    content = f.read()
    version_match = re.search(
        r"^__version__\s*=\s*['\"]([^'\"]+)['\"]", content, re.MULTILINE
    )
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-geosupport",
    version=version,
    url="https://github.com/ishiland/python-geosupport",
    description="Python bindings for NYC Geosupport Desktop Edition",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/ishiland/python-geosupport/issues",
        "Documentation": "https://python-geosupport.readthedocs.io/en/latest/",
        "Source Code": "https://github.com/ishiland/python-geosupport",
    },
    author="Ian Shiland, Jeremy Neiman",
    author_email="ishiland@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    keywords=["NYC", "geocoder", "python-geosupport", "geosupport"],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    test_suite="tests",
    extras_require={
        "dev": [
            "coverage",
            "black==25.1.0",
        ]
    },
)
