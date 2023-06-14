# from: https://gist.github.com/ishiland/824ddd386fcd0b90fc55aea573a28b22
# written by ishiland: https://github.com/ishiland
# derived from: https://stackoverflow.com/a/53135031/3641153
# minor edits by torreyma: https://github.com/torreyma
#
from geosupport import Geosupport, GeosupportError
import pandas as pd
from multiprocessing import Pool, cpu_count
from functools import partial
import numpy as np

"""
Example of how to use python-geosupport, Pandas and Multiprocessing to speed up geocoding workflows. 
"""

# For Windows:
g = Geosupport(geosupport_path="C:\\Program Files (x86)\\Geosupport Desktop Edition")
# On linux: comment above line and uncomment line below. Set environment variables GEOFILES and LD_LIBRARY_PATH to indicate location of the fls/ and lib/ directories.
# g = Geosupport()

cpus = cpu_count()


def geo_by_address(row):
    """
    Geocodes a pandas row containing address atributes.

    :param row: Pandas Series
    :return: Pandas Series with lat, lon & Geosupport message.
    """
    try:
        result = g.address(house_number=row['PHN'], street_name=row['STREET'], zip=row['ZIP_CODE']) # Adjust these to match your data column names
        lat = result.get("Latitude")
        lon = result.get('Longitude')
        msg = result.get('Message')
    except GeosupportError as ge:
        lat = "Error"
        lon = "Error"
        msg = str(ge)
        pass
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


if __name__ == '__main__':
  
    # read in csv
    df = pd.read_csv('INPUT.csv')
    
    # add 3 Geosupport columns - Latitude, Longitude and Geosupport message
    df[['lat', 'lon', 'msg']] = parallelize(df, partial(run_on_subset, geo_by_address))

    # output to csv with the 3 new columns.
    df.to_csv('OUTPUT.csv')




