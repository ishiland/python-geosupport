def parse_2(wa2):
    # Work Area 2 (COW) - Function 2
    return {
        "Internal Use": wa2[0:21],
        "Intersection Replication Counter": wa2[21],
        "DCP-Preferred LGC for Street 1": wa2[22:24],
        "DCP-Preferred LGC for Street 2": wa2[24:26],
        "Number of Intersecting Streets": wa2[26],
        "List of Intersecting Streets (Up to five B5SCs, 6 bytes each)": wa2[27:57],
        "Compass Direction for Intersection Key or Counter for Multiple Intersections": wa2[57],
        "Atomic Polygon": wa2[58:61],  # Was Dynamic Block
        # "Filler": wa2[61:62],
        "LION Node Number": wa2[63:70],
        "SPATIAL COORDINATES": wa2[70:91],
        "X Coordinate": wa2[70:77],
        "Y Coordinate": wa2[77:84],
        "Reserved for possible Z Coordinate": wa2[84:91],
        "SBVP1 (SANBORN MAP IDENTIFIER)": {
            "Borough Code": wa2[91],
            "Volume Number": wa2[92:94],
            "Volume Number Suffix": wa2[94],
            "Page Number": wa2[95:98],
            "Page Number Suffix": wa2[98]},
        "SBVP2 (SANBORN MAP IDENTIFIER)": {
            "Borough Code": wa2[99],
            "Volume Number": wa2[100:102],
            "Volume Number Suffix": wa2[102],
            "Page Number": wa2[103:106],
            "Page Number Suffix": wa2[106]},
        "Marble Hill/Rikers Island Alternative Borough Flag": wa2[107],
        "DOT Street Light Contractor Area": wa2[108],
        "COMMUNITY DISTRICT": {
            "Community District Borough Code": wa2[109],
            "Community District Number": wa2[110:112]},
        "ZIP Code": wa2[112:117],
        "Health Area": wa2[117:121],
        "Police Patrol Borough Command": wa2[121],
        "Police Precinct": wa2[122:125],
        "Fire Division": wa2[125:127],
        "Fire Battalion": wa2[127:129],
        "Fire Company Type": wa2[129],
        "Fire Company Number": wa2[130:133],
        "Community School District": wa2[133:135],
        "2010 Census Tract": wa2[135:141],
        "1990 Census Tract": wa2[141:147],
        # "List of Pairs of Level Codes": wa2[147:156],  # Not Implemented
        "Police Patrol Borough": wa2[157:159],
        "Assembly District": wa2[159:161],
        "Congressional District": wa2[161:163],
        "State Senatorial District": wa2[163:165],
        "Civil Court District": wa2[165:167],
        "City Council District": wa2[167:1689],
        "CD Eligibility": wa2[169],
        "Distance Between Duplicate Intersections": wa2[170:175],
        "2000 Census Tract": wa2[175:181],
        "Health Center District": wa2[181:183],
        "Sanitation District": wa2[183:186],
        "Sanitation Section/Subsection": wa2[186:188],
        # "Filler": wa2[188:199],
    }

def parse_2W(wa2):
    wide =  {
    # Work Area 2 (COW) - Function 2W (Wide)
    # "Same as regular work area 2 for Function 2": wa2[0:199],
    # "Filler": wa2[200:221],
    "LGC List for Street 1": wa2[222:230],
    "LGC List for Street 2": wa2[230:238],
    "Turn Restrictions": wa2[238:248],
    "Preferred LGCs for Intersecting B5SCs": wa2[248:258],
    "True Replication Counter": wa2[258:260],
    "List of Up To 20 7-Byte Nodes": wa2[260:400],  # GRC 03 / Reason B
    "B7SCs For The Above 20 Nodes -List of intersecting streets(B7SCs) for node list": wa2[400:3600],
        # (8byte street code * 4 LGCs * 5 streets * 20 nodes)  - See table below for detail
        # GRC 03/ B See detail layout below.
        # See https://nycplanning.github.io/Geosupport-UPG/appendices/appendix13/#work-area-2-cow-function-2w-wide
    "Reason Code": wa2[3600],
    "Reason Code Qualifier": wa2[3601],
    "Warning Code": wa2[3602:3604],
    "Return Code": wa2[3604:3606],
    "Latitude": wa2[3606:3615],
    "Longitude": wa2[3615:3626],
    # "Filler": wa2[3626:3999],
    }
    wide = wide.copy()
    wide.update(parse_2(wa2))
    return wide