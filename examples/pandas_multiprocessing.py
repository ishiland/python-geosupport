# from: https://gist.github.com/ishiland/824ddd386fcd0b90fc55aea573a28b22
# written by ishiland: https://github.com/ishiland
# Minor edits by torreyma: https://github.com/torreyma
#
from geosupport import Geosupport, GeosupportError
from nycparser import Parser
import pandas as pd
from multiprocessing import Pool, cpu_count
from functools import partial
import numpy as np

"""
Example of how to use python-geosupport, Pandas and Multiprocessing to speed up geocoding workflows. 
"""

g = Geosupport()
p = Parser()

cpus = cpu_count()

INPUT_CSV = '/examples/data/input.csv'
OUTPUT_CSV = '/examples/data/output-pandas-multiprocessing.csv'


def geo_by_address(row):
    """
    Geocodes a pandas row containing address atributes.

    :param row: Pandas Series
    :return: Pandas Series with lat, lon & Geosupport message.
    """
    try:
        # parse the address to separate PHN and street
        parsed = p.address(row['Address'])
        # geocode
        result = g.address(house_number=parsed['PHN'], street_name=parsed['STREET'], borough=row['Borough'])
        lat = result.get("Latitude")
        lon = result.get('Longitude')
        msg = result.get('Message')
    except GeosupportError as ge:
        lat = ""
        lon = ""
        msg = str(ge)
    return pd.Series([lat, lon, msg])
  
  
def parallelize(data, func, num_of_processes=cpus):
    data_split = np.array_split(data, num_of_processes)
    pool = Pool(num_of_processes)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data


def run_on_subset(func, data_subset):
    return data_subset.apply(func, axis=1)


def parallelize_on_rows(data, func, num_of_processes=cpus):
    return parallelize(data, partial(run_on_subset, func), num_of_processes)


if __name__ == '__main__':
  
    # read in csv
    df = pd.read_csv(INPUT_CSV)
    
    # add 3 Geosupport columns - Latitude, Longitude and Geosupport message
    df[['lat', 'lon', 'msg']] = parallelize_on_rows(df, geo_by_address)

    # output to csv with the 3 new columns.
    df.to_csv(OUTPUT_CSV)




