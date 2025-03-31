import re
import os
from setuptools import setup, find_packages

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
    ],
    python_requires=">=3.8",
    test_suite="tests",
    extras_require={
        "dev": [
            "coverage",
            "black",
        ]
    },
)
