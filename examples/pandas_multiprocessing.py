"""
Example of how to use python-geosupport, Pandas and Multiprocessing to speed up geocoding workflows. 
"""

import os
import pandas as pd
from typing import Callable
from multiprocessing import Pool, cpu_count
from functools import partial
from tqdm import tqdm  # Progress bar

from geosupport import Geosupport, GeosupportError
from nycparser import Parser

# Determine reasonable CPU count (avoid memory issues)
cpus = min(cpu_count(), 8)

# Proper path handling relative to script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_CSV = os.path.join(SCRIPT_DIR, "data/input.csv")
OUTPUT_CSV = os.path.join(SCRIPT_DIR, "data/output-pandas-multiprocessing.csv")


# Create a single global instance
g = Geosupport()
p = Parser()


def geo_by_address(row: pd.Series) -> pd.Series:
    """
    Geocodes a pandas row containing address attributes.

    Args:
        row: Pandas Series with 'Address' and 'Borough' columns

    Returns:
        Pandas Series with lat, lon & Geosupport message.
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
        msg = result.get("Message", "")
    except GeosupportError as ge:
        lat = ""
        lon = ""
        msg = str(ge)
    except Exception as e:
        lat = ""
        lon = ""
        msg = f"Error: {str(e)}"

    return pd.Series([lat, lon, msg])


def run_on_subset(func: Callable, data_subset: pd.DataFrame) -> pd.DataFrame:
    """Apply a function to each row of a dataframe subset"""
    return data_subset.apply(func, axis=1)


def parallelize(
    data: pd.DataFrame, func: Callable, num_of_processes: int = cpus
) -> pd.DataFrame:
    """
    Split dataframe and apply function in parallel

    Args:
        data: Input DataFrame
        func: Function to apply to each chunk
        num_of_processes: Number of parallel processes

    Returns:
        DataFrame with results
    """
    # Create roughly equal sized chunks using pandas methods
    splits = []
    chunk_size = max(1, len(data) // num_of_processes)

    # Create chunks without using numpy arrays
    for i in range(0, len(data), chunk_size):
        splits.append(data.iloc[i : min(i + chunk_size, len(data))].copy())

    # Use tqdm for progress tracking
    with Pool(num_of_processes) as pool:
        results = list(
            tqdm(pool.imap(func, splits), total=len(splits), desc="Geocoding")
        )

    return pd.concat(results)


if __name__ == "__main__":
    print(f"Starting geocoding with {cpus} processes")

    # Process in batches for large datasets
    batch_size = 100000

    # Check if input file exists
    if not os.path.exists(INPUT_CSV):
        print(f"Error: Input file not found: {INPUT_CSV}")
        exit(1)

    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

    # Read the input csv
    df = pd.read_csv(INPUT_CSV)
    total_rows = len(df)
    print(f"Processing {total_rows} addresses")

    # Process in batches if large dataset
    if total_rows > batch_size:
        for i in range(0, total_rows, batch_size):
            print(
                f"Processing batch {i//batch_size + 1}/{(total_rows-1)//batch_size + 1}"
            )
            batch = df.iloc[i : i + batch_size].copy()

            # Geocode the batch
            batch[["lat", "lon", "msg"]] = parallelize(
                batch, partial(run_on_subset, geo_by_address), num_of_processes=cpus
            )

            # Write each batch (append mode after first batch)
            mode = "w" if i == 0 else "a"
            header = i == 0
            batch.to_csv(OUTPUT_CSV, mode=mode, header=header, index=False)
            print(f"Batch {i//batch_size + 1} complete")
    else:
        # For small datasets, process all at once
        df[["lat", "lon", "msg"]] = parallelize(
            df, partial(run_on_subset, geo_by_address), num_of_processes=cpus
        )
        df.to_csv(OUTPUT_CSV, index=False)

    print(f"Geocoding complete! Results saved to {OUTPUT_CSV}")
