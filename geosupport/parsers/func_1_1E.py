

def parse_1_1E(wa2):
    # Work Area 2 (COW) - Functions 1, 1E
    return{
        # "Internal Use": wa2[0:20],
        "Continuous Parity Indicator/Duplicate Address Indicator": wa2[21],
        "Low House Number of Block Face": wa2[22:32],  # Sort Format
        "High House Number of Block Face": wa2[33:43],  # Sort Format
        "No. of Cross Streets at Low Address End": wa2[46],
        "List of Cross Streets at Low Address End (Up to 5 B5SCs)": wa2[47:76],  # B5SC - Blank-Filled
        "No. of Cross Streets at High Address End": wa2[77],
        "List of Cross Streets at High Address End (Up to 5 B5SCs)": wa2[78:107],  # B5SC - Blank-Filled
        "LION KEY":{"Borough Code": wa2[108],
                    "Face Code": wa2[109:112],
                    "Sequence Number": wa2[113:117]},
        "Special Address Generated Record Flag": wa2[118],
        "Side of Street Indicator": wa2[119],
        "Segment Length in Feet": wa2[120:124],
        "SPATIAL X-Y COORDINATES OF ADDRESS": wa2[125:138],
        "X Coordinate": wa2[125:131],
        "Y Coordinate": wa2[132:138],
        "Reserved for Possible Z Coordinate": wa2[139:145],
        "Community Development Eligibility Indicator": wa2[146],
        "Marble Hill/Rikers Island Alternative Borough Flag": wa2[147],
        "DOT Street Light Contractor Area": wa2[148],
        "COMMUNITY DISTRICT": {
            "Community District Borough Code": wa2[149],
            "Community District Number": wa2[150:151]},
        "ZIP Code": wa2[152:156],
        "FUNCTION 1E ITEMS": wa2[157:170],  # Use ONLY for Function 1E
        "Election District": wa2[157:159],  # Invalid for Fn 1
        "Assembly District": wa2[160:161],  # Invalid for Fn 1
        "Split Election District Flag": wa2[162],  # Invalid for Fn 1
        "Congressional District": wa2[163:164],  # Invalid for Fn 1
        "State Senatorial District": wa2[165:166],  # Invalid for Fn 1
        "Civil Court District": wa2[167:168],  # Invalid for Fn 1
        "City Council District": wa2[169:170],  # Invalid for Fn 1
        "Health Center District": wa2[171:172],
        "Health Area": wa2[173:176],
        "Sanitation District": wa2[177:179],
        "Sanitation Collection Scheduling Section and Subsection": wa2[180:181],
        "Sanitation Regular Collection Schedule": wa2[182:186],
        "Sanitation Recycling Collection Schedule": wa2[187:189],
        "Police Patrol Borough Command": wa2[190],
        "Police Precinct": wa2[191:193],
        "Fire Division": wa2[194:195],
        "Fire Battalion": wa2[196:197],
        "Fire Company Type": wa2[198],
        "Fire Company Number": wa2[199:201],
        # "Filler": wa2[202],  # Was Split Comm School Dist Flag
        "Community School District": wa2[203:204],
        "Atomic Polygon": wa2[205:207],  # Was Dynamic Block
        "Police Patrol Borough": wa2[208:209],
        "Feature Type Code": wa2[210],
        "Segment Type Code": wa2[211],
        "Alley or Cross Street List Flag": wa2[212],  # A - Alley Split X - Cross Street List Modified
        "Coincidence Segment Count": wa2[213],
        # "Filler": wa2[214:215],
        "Borough of Census Tract": wa2[216],  # Internal
        "1990 Census Tract": wa2[217:222],
        "2010 Census Tract": wa2[223:228],
        "2010 Census Block": wa2[229:232],
        "2010 Census Block Suffix": wa2[233],  # Not Implemented
        "2000 Census Tract": wa2[234:239],
        "2000 Census Block": wa2[240:243],
        "2000 Census Block Suffix": wa2[244],
        "Neighborhood Tabulation Area (NTA)": wa2[245:248],
        "DSNY Snow Priority Code": wa2[249],  # Dept. of Sanitation
        "DSNY Organic Recycling Schedule": wa2[250:254],  # Dept. of Sanitation
        "DSNY Bulk Pickup Schedule": wa2[255:259],  # Dept. of Sanitation
        "Hurricane Evacuation Zone (HEZ)": wa2[260:261],
        # "Filler": wa2[262:272],
        "Underlying Address Number on True Street (for NAPs, Vanity, etc)": wa2[273:283],  # Sort Format
        "Underlying B7SC of True Street (NAPs etc)": wa2[284:291],
        "Segment Identifier": wa2[292:298],
        "Curve Flag": wa2[299],
    }


def parse_1_1E_ext(wa2):
    #  Work Area 2 (COW) - Functions 1, 1E Extended
    return { # "Same as Regular Work Area 2 for Functions 1, 1E": wa2[0:299],
        "List of 4 LGC's": wa2[300:307],
        "BOE LGC Pointer": wa2[308],
        "Segment Azimuth": wa2[309:311],
        "Segment Orientation": wa2[312],
        "SPATIAL COORDINATES OF SEGMENT": {
            "X Coordinate, Low Address End": wa2[313:319],  # From Node
            "Y Coordinate, Low Address End": wa2[320:326],
            "Z Coordinate, Low Address End": wa2[327:333],  # Not Implemented
            "X Coordinate, High Address End": wa2[334:340],  # To Node
            "Y Coordinate, High Address End": wa2[341:347],
            "Z Coordinate, High Address End": wa2[348:354]},  # Not Implemented
        "SPATIAL COORDINATES OF CENTER OF CURVATURE": {
            "X Coordinate": wa2[355:361],
            "Y Coordinate": wa2[362:368],
            "Z Coordinate": wa2[369:375]},  # Not Implemented
        "Radius of Circle": wa2[376:382],
        "Secant Location Related to Curve": wa2[383],  # L - Left, R - Right
        "Angle to From Node - Beta Value": wa2[384:388],  # Beta & Alpha Used to Calculate Coordinates
        "From LION Node ID": wa2[394:400],  # From Node
        "To LION Node ID": wa2[401:407],  # To Node
        "LION KEY FOR VANITY ADDRESS": {
            "Borough Code": wa2[408],
            "Face Code": wa2[409:412],
            "Sequence Number": wa2[413:417]},
        "Side of Street of Vanity Address": wa2[418],
        "Split Low House Number": wa2[419:429],
        "Traffic Direction": wa2[430],
        "Turn Restrictions": wa2[431:440],  # Not Implemented
        "Fraction for Curve Calculation": wa2[441:443],  # Internal Use
        "Roadway Type": wa2[444:445],
        "Physical ID": wa2[446:452],
        "Generic ID": wa2[453:459],
        "NYPD ID": wa2[460:466],
        "FDNY ID": wa2[467:473],
        "Bike Lane 2": wa2[474:475],
        "Bike Traffic Direction": wa2[476:477],
        "Filler": wa2[478:480],  # Was Blockface ID, See bytes 730-739
        "Street Status": wa2[481],
        "Street Width": wa2[482:484],
        "Street Width Irregular": wa2[485],
        "Bike Lane": wa2[486],  # Will be retired. See Bike Lane 2
        "Federal Classification Code": wa2[487:488],
        "Right Of Way Type": wa2[489],
        "List of Second Set of 5 LGCs": wa2[490:499],
        "Legacy Segment ID": wa2[500:506],
        "From Preferred LGCs First Set of 5": wa2[507:516],
        "To Preferred LGCs First Set of 5": wa2[517:526],
        "From Preferred LGCs Second Set of 5": wa2[527:536],
        "To Preferred LGCs Second Set of 5": wa2[537:546],
        "No Cross Street Calculation Flag": wa2[547],
        "Individual Segment Length": wa2[548:552],
        "NTA Name": wa2[553:627],
        "USPS Preferred City Name": wa2[628:652],
        "Latitude": wa2[653:661],
        "Longitude": wa2[662:672],
        "From Actual Segment Node ID": wa2[673:679],
        "To Actual Segment Node ID": wa2[680:686],
        "SPATIAL COORDINATES OF ACTUAL SEGMENT": wa2[687:728],
        "X Coordinate, Low Address End": wa2[687:693],  # Actual From Node
        "Y Coordinate, Low Address End": wa2[694:700],
        "Z Coordinate, Low Address End": wa2[701:707],  # Not Implemented
        "X Coordinate, High Address End": wa2[708:714],  # Actual To Node
        "Y Coordinate, High Address End": wa2[715:721],
        "Z Coordinate, High Address End": wa2[722:728],  # Not Implemented
        "Blockface ID": wa2[729:738],  # Previously 7 bytes
        "Number of Travel Lanes on the Street": wa2[739:740],
        "Number of Parking Lanes on the Street": wa2[741:742],
        "Number of Total Lanes on the Street": wa2[743:744],
        "Street Width Maximum": wa2[745:747],
        # "Filler": wa2[748:999],
        "Reason Code": wa2[1000],
        "Reason Code Qualifier": wa2[1001],
        "Warning Code Filler": wa2[1002:1003],
        "Return Code": wa2[1004:1005],
        "Number of Cross Streets at Low Address End": wa2[1006],
        "List of Cross Streets at Low Address End (Up to 5 B7SCs)": wa2[1007:1046],  # B7SC-Blank-Filled
        "Number of Cross Streets at High Address End": wa2[1047],
        "List of Cross Streets at High Address End (Up to 5 B7SCs)": wa2[1048:1087],  # B7SC-Blank-Filled
        "List of Cross Street Names at Low Address End": wa2[1088:1247],  # 5 x 32 = 160 Up to 5 Street Names
        "List of Cross Street Names at High Address End": wa2[1248:1407],  # 5 x 32 = 160 Up to 5 Street Names
        "BOE Preferred B7SC": wa2[1408:1415],
        "BOE Preferred Street Name": wa2[1416:1447],
        # "Filler": wa2[1448:1499]
    }