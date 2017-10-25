def parse_2(wa2):
    # Work Area 2 (COW) - Function 2
    return{
        "Internal Use": wa2[0:20],
        "Intersection Replication Counter": wa2[21],
        "DCP-Preferred LGC for Street 1": wa2[22:23],
        "DCP-Preferred LGC for Street 2": wa2[24:25],
        "Number of Intersecting Streets": wa2[26],
        "List of Intersecting Streets (Up to five B5SCs, 6 bytes each)": wa2[27:56],
        "Compass Direction for Intersection Key or Counter for Multiple Intersections": wa2[57],
        "Atomic Polygon": wa2[58:60],  # Was Dynamic Block
        # "Filler": wa2[61:62],
        "LION Node Number": wa2[63:69],
        "SPATIAL COORDINATES": wa2[70:90],
        "X Coordinate": wa2[70:76],
        "Y Coordinate": wa2[77:83],
        "Reserved for possible Z Coordinate": wa2[84:90],
        "SBVP1 (SANBORN MAP IDENTIFIER)": {
            "Borough Code": wa2[91],
            "Volume Number": wa2[92:93],
            "Volume Number Suffix": wa2[94],
            "Page Number": wa2[95:97],
            "Page Number Suffix": wa2[98]},
        "SBVP2 (SANBORN MAP IDENTIFIER)": {
            "Borough Code": wa2[99],
            "Volume Number": wa2[100:101],
            "Volume Number Suffix": wa2[102],
            "Page Number": wa2[103:105],
            "Page Number Suffix": wa2[106]},
        "Marble Hill/Rikers Island Alternative Borough Flag": wa2[107],
        "DOT Street Light Contractor Area": wa2[108],
        "COMMUNITY DISTRICT": {
            "Community District Borough Code": wa2[109],
            "Community District Number": wa2[110:111]},
        "ZIP Code": wa2[112:116],
        "Health Area": wa2[117:120],
        "Police Patrol Borough Command": wa2[121],
        "Police Precinct": wa2[122:124],
        "Fire Division": wa2[125:126],
        "Fire Battalion": wa2[127:128],
        "Fire Company Type": wa2[129],
        "Fire Company Number": wa2[130:132],
        "Community School District": wa2[133:134],
        "2010 Census Tract": wa2[135:140],
        "1990 Census Tract": wa2[141:146],
        # "List of Pairs of Level Codes": wa2[147:156],  # Not Implemented
        "Police Patrol Borough": wa2[157:158],
        "Assembly District": wa2[159:160],
        "Congressional District": wa2[161:162],
        "State Senatorial District": wa2[163:164],
        "Civil Court District": wa2[165:166],
        "City Council District": wa2[167:168],
        "CD Eligibility": wa2[169],
        "Distance Between Duplicate Intersections": wa2[170:174],
        "2000 Census Tract": wa2[175:180],
        "Health Center District": wa2[181:182],
        "Sanitation District": wa2[183:185],
        "Sanitation Section/Subsection": wa2[186:187],
        # "Filler": wa2[188:199],
    }

def parse_2W(wa2):
    return {
    # Work Area 2 (COW) - Function 2W (Wide)
    # "Same as regular work area 2 for Function 2": wa2[0:199],
    # "Filler": wa2[200:221],
    "LGC List for Street 1": wa2[222:229],
    "LGC List for Street 2": wa2[230:237],
    "Turn Restrictions": wa2[238:247],
    "Preferred LGCs for Intersecting B5SCs": wa2[248:257],
    "True Replication Counter": wa2[258:259],
    "List of Up To 20 7-Byte Nodes": wa2[260:399],  # GRC 03 / Reason B
    "B7SCs For The Above 20 Nodes -List of intersecting streets(B7SCs) for node list": wa2[400:3599],
        # (8byte street code * 4 LGCs * 5 streets * 20 nodes)  - See table below for detail
        # GRC 03/ B See detail layout below.
        # See https://nycplanning.github.io/Geosupport-UPG/appendices/appendix13/#work-area-2-cow-function-2w-wide
    "Reason Code": wa2[3600],
    "Reason Code Qualifier": wa2[3601],
    "Warning Code": wa2[3602:3603],
    "Return Code": wa2[3604:3605],
    "Latitude": wa2[3606:3614],
    "Longitude": wa2[3615:3625],
    # "Filler": wa2[3626:3999],
    }