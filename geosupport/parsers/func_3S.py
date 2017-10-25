

def parse_3S(wa2):
    # Work Area 2 (COW) - Function 3S
    return{
        # "Internal Use": wa2[0:1],
        "Generic/Roadbed Street Name Indicator": wa2[2],  # G - Generic R - Roadbed
        "Borough Code": wa2[3],
        "5-Digit Street Code of 'On' Street": wa2[4:8],
        "LGC": wa2[9:10],
        # "Filler": wa2[11:20],  # Always Blank
        "Number of Intersections": wa2[21:23],  # Maximum of 350
        "LIST OF INTERSECTIONS": wa2[24:19273],
        # Variable length list of up to 350 entries; each is 55 bytes long, structured as follows
        # Max. of 350 entries, each 55 bytes long: 350 x 55 = 19,250
        # "Marble Hill/Rikers Island Flag": wa2[0],
        # "Distance from previous intersection in list": wa2[1:59],
        # "Gap Flag": wa2[6],
        # "Node Number": wa2[7:13],
        # "Number of streets at this intersection": wa2[14],
        # "List of Cross Streets at this Intersection (Up to 5 B7SCs)": wa2[15:54],  # B7SC = B5SC + DCP Preferred LGC
    }