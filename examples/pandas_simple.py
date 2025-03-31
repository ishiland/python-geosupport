from geosupport import Geosupport, GeosupportError
from nycparser import Parser
import pandas as pd
from multiprocessing import Pool, cpu_count
from functools import partial
import numpy as np

"""
Example of how to use python-geosupport and pandas dataframes. 
"""

g = Geosupport()
p = Parser()

INPUT_CSV = "/examples/data/input.csv"
OUTPUT_CSV = "/examples/data/output-pandas-simple.csv"


def geo_by_address(row):
    """
    Geocodes a pandas row containing address attributes.
    :param row: Pandas Series
    :return: Pandas Series with lat, lng & Geosupport message.
    """
    try:
        # parse the address to separate PHN and street
        parsed = p.address(row["Address"])
        # geocode
        result = g.address(
            house_number=parsed["PHN"],
            street_name=parsed["STREET"],
            borough=row["Borough"],
        )
        lat = result.get("Latitude")
        lon = result.get("Longitude")
        msg = result.get("Message")
    except GeosupportError as ge:
        lat = ""
        lon = ""
        msg = str(ge)
    return pd.Series([lat, lon, msg])


if __name__ == "__main__":
    # read in csv
    df = pd.read_csv(INPUT_CSV)

    # add 3 Geosupport columns - Latitude, Longitude and Geosupport message
    df[["lat", "lon", "msg"]] = df.apply(geo_by_address, axis=1)

    # output the new dataframe to a csv
    df.to_csv(OUTPUT_CSV, index=False)
