#!/usr/bin/env python
"""
Example: Accessing similar street names from Geosupport errors

When Geosupport can't find a street name, it returns up to 10 similar names
in the error response. This example shows how to extract them.
"""

from geosupport import Geosupport, GeosupportError


def get_similar_streets(error):
    """Extract similar street names from a GeosupportError."""
    result = error.result

    # Get count of similar names (may be string or int)
    count = result.get("Number of Street Codes and Street Names in List", 0)
    if isinstance(count, str):
        count = int(count.strip() or "0")
    if count == 0:
        return []

    # Get list of street names (already parsed into a list by the library)
    similar_names = result.get("List of Street Names", [])

    # Filter out empty strings and return
    return [name for name in similar_names if name and name.strip()]


# Example usage
if __name__ == "__main__":
    g = Geosupport()

    # Example 1: Misspelled street name
    print("Example: Searching for 'wycoff street' in Brooklyn")
    print("-" * 50)

    try:
        # This will fail because it should be 'wyckoff'
        result = g["1N"](borough_code="BK", street_name="wycoff street")
    except GeosupportError as e:
        print(f"Error: {e}\n")

        # Extract and display similar names
        similar = get_similar_streets(e)
        if similar:
            print(f"Found {len(similar)} similar street(s):")
            for i, name in enumerate(similar, 1):
                print(f"  {i}. {name}")

            # You could now retry with similar[0] or let user choose
            print(f"\nRetrying with first match: '{similar[0]}'")
            result = g["1N"](borough_code="BK", street_name=similar[0])
            print(
                f"Success! Street code: {result.get('B10SC - First Borough and Street Code')}"
            )
