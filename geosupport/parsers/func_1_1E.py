

def parse_1_1E(wa2):
    # Work Area 2 (COW) - Functions 1, 1E
    return{
        # "Internal Use": wa2[0:20],
        "Continuous Parity Indicator/Duplicate Address Indicator": wa2[21],
        "Low House Number of Block Face": wa2[22:33],  # Sort Format
        "High House Number of Block Face": wa2[33:44],  # Sort Format
        "No. of Cross Streets at Low Address End": wa2[46],
        "List of Cross Streets at Low Address End (Up to 5 B5SCs)": wa2[47:77],  # B5SC - Blank-Filled
        "No. of Cross Streets at High Address End": wa2[77],
        "List of Cross Streets at High Address End (Up to 5 B5SCs)": wa2[78:108],  # B5SC - Blank-Filled
        "LION KEY":{"Borough Code": wa2[108],
                    "Face Code": wa2[109:113],
                    "Sequence Number": wa2[113:118]},
        "Special Address Generated Record Flag": wa2[118],
        "Side of Street Indicator": wa2[119],
        "Segment Length in Feet": wa2[120:125],
        "SPATIAL X-Y COORDINATES OF ADDRESS": wa2[125:138],
        "X Coordinate": wa2[125:132],
        "Y Coordinate": wa2[132:139],
        "Reserved for Possible Z Coordinate": wa2[139:146],
        "Community Development Eligibility Indicator": wa2[146],
        "Marble Hill/Rikers Island Alternative Borough Flag": wa2[147],
        "DOT Street Light Contractor Area": wa2[148],
        "COMMUNITY DISTRICT": {
            "Community District Borough Code": wa2[150],
            "Community District Number": wa2[150:152]},
        "ZIP Code": wa2[152:157],
        # "FUNCTION 1E ITEMS": wa2[157:170],  # Use ONLY for Function 1E
        "Election District": wa2[157:160],  # Invalid for Fn 1
        "Assembly District": wa2[160:162],  # Invalid for Fn 1
        "Split Election District Flag": wa2[162],  # Invalid for Fn 1
        "Congressional District": wa2[163:165],  # Invalid for Fn 1
        "State Senatorial District": wa2[165:167],  # Invalid for Fn 1
        "Civil Court District": wa2[167:169],  # Invalid for Fn 1
        "City Council District": wa2[169:171],  # Invalid for Fn 1
        "Health Center District": wa2[171:173],
        "Health Area": wa2[173:177],
        "Sanitation District": wa2[177:180],
        "Sanitation Collection Scheduling Section and Subsection": wa2[180:182],
        "Sanitation Regular Collection Schedule": wa2[182:187],
        "Sanitation Recycling Collection Schedule": wa2[187:190],
        "Police Patrol Borough Command": wa2[190],
        "Police Precinct": wa2[191:194],
        "Fire Division": wa2[194:196],
        "Fire Battalion": wa2[196:198],
        "Fire Company Type": wa2[198],
        "Fire Company Number": wa2[199:202],
        # "Filler": wa2[202],  # Was Split Comm School Dist Flag
        "Community School District": wa2[203:205],
        "Atomic Polygon": wa2[205:208],  # Was Dynamic Block
        "Police Patrol Borough": wa2[208:210],
        "Feature Type Code": wa2[210],
        "Segment Type Code": wa2[211],
        "Alley or Cross Street List Flag": wa2[212],  # A - Alley Split X - Cross Street List Modified
        "Coincidence Segment Count": wa2[213],
        # "Filler": wa2[214:215],
        "Borough of Census Tract": wa2[216],  # Internal
        "1990 Census Tract": wa2[217:223],
        "2010 Census Tract": wa2[223:229],
        "2010 Census Block": wa2[229:231],
        "2010 Census Block Suffix": wa2[233],  # Not Implemented
        "2000 Census Tract": wa2[234:240],
        "2000 Census Block": wa2[240:244],
        "2000 Census Block Suffix": wa2[244],
        "Neighborhood Tabulation Area (NTA)": wa2[245:249],
        "DSNY Snow Priority Code": wa2[249],  # Dept. of Sanitation
        "DSNY Organic Recycling Schedule": wa2[250:255],  # Dept. of Sanitation
        "DSNY Bulk Pickup Schedule": wa2[255:260],  # Dept. of Sanitation
        "Hurricane Evacuation Zone (HEZ)": wa2[260:262],
        # "Filler": wa2[262:272],
        "Underlying Address Number on True Street (for NAPs, Vanity, etc)": wa2[273:284],  # Sort Format
        "Underlying B7SC of True Street (NAPs etc)": wa2[284:292],
        "Segment Identifier": wa2[292:299],
        "Curve Flag": wa2[299],
    }


def parse_1_1E_ext(wa2):
    #  Work Area 2 (COW) - Functions 1, 1E Extended
    return { # "Same as Regular Work Area 2 for Functions 1, 1E": wa2[0:299],
        "List of 4 LGC's": wa2[300:308],
        "BOE LGC Pointer": wa2[308],
        "Segment Azimuth": wa2[309:312],
        "Segment Orientation": wa2[312],
        "SPATIAL COORDINATES OF SEGMENT": {
            "X Coordinate, Low Address End": wa2[313:320],  # From Node
            "Y Coordinate, Low Address End": wa2[320:327],
            "Z Coordinate, Low Address End": wa2[327:334],  # Not Implemented
            "X Coordinate, High Address End": wa2[334:341],  # To Node
            "Y Coordinate, High Address End": wa2[341:348],
            "Z Coordinate, High Address End": wa2[348:355]},  # Not Implemented
        "SPATIAL COORDINATES OF CENTER OF CURVATURE": {
            "X Coordinate": wa2[355:362],
            "Y Coordinate": wa2[362:369],
            "Z Coordinate": wa2[369:376]},  # Not Implemented
        "Radius of Circle": wa2[376:383],
        "Secant Location Related to Curve": wa2[383],  # L - Left, R - Right
        "Angle to From Node - Beta Value": wa2[384:389],  # Beta & Alpha Used to Calculate Coordinates
        "Angle to To Node – Alpha Value": wa2[389:394],
        "From LION Node ID": wa2[394:401],  # From Node
        "To LION Node ID": wa2[401:408],  # To Node
        "LION KEY FOR VANITY ADDRESS": {
            "Borough Code": wa2[408],
            "Face Code": wa2[409:413],
            "Sequence Number": wa2[413:418]},
        "Side of Street of Vanity Address": wa2[418],
        "Split Low House Number": wa2[419:430],
        "Traffic Direction": wa2[430],
        "Turn Restrictions": wa2[431:441],  # Not Implemented
        "Fraction for Curve Calculation": wa2[441:444],  # Internal Use
        "Roadway Type": wa2[444:446],
        "Physical ID": wa2[446:453],
        "Generic ID": wa2[453:460],
        "NYPD ID": wa2[460:467],
        "FDNY ID": wa2[467:474],
        "Bike Lane 2": wa2[474:476],
        "Bike Traffic Direction": wa2[476:478],
        "Filler": wa2[478:481],  # Was Blockface ID, See bytes 730-739
        "Street Status": wa2[481],
        "Street Width": wa2[482:485],
        "Street Width Irregular": wa2[485],
        "Bike Lane": wa2[486],  # Will be retired. See Bike Lane 2
        "Federal Classification Code": wa2[487:489],
        "Right Of Way Type": wa2[489],
        "List of Second Set of 5 LGCs": wa2[490:500],
        "Legacy Segment ID": wa2[500:507],
        "From Preferred LGCs First Set of 5": wa2[507:517],
        "To Preferred LGCs First Set of 5": wa2[517:527],
        "From Preferred LGCs Second Set of 5": wa2[527:537],
        "To Preferred LGCs Second Set of 5": wa2[537:547],
        "No Cross Street Calculation Flag": wa2[547],
        "Individual Segment Length": wa2[548:553],
        "NTA Name": wa2[553:628],
        "USPS Preferred City Name": wa2[628:653],
        "Latitude": wa2[653:662],
        "Longitude": wa2[662:673],
        "From Actual Segment Node ID": wa2[673:680],
        "To Actual Segment Node ID": wa2[680:687],
        "SPATIAL COORDINATES OF ACTUAL SEGMENT": {
        "X Coordinate, Low Address End": wa2[687:694],  # Actual From Node
        "Y Coordinate, Low Address End": wa2[694:701],
        "Z Coordinate, Low Address End": wa2[701:708],  # Not Implemented
        "X Coordinate, High Address End": wa2[708:715],  # Actual To Node
        "Y Coordinate, High Address End": wa2[715:722],
        "Z Coordinate, High Address End": wa2[722:729],  # Not Implemented
        },
        "Blockface ID": wa2[729:739],  # Previously 7 bytes
        "Number of Travel Lanes on the Street": wa2[739:741],
        "Number of Parking Lanes on the Street": wa2[741:743],
        "Number of Total Lanes on the Street": wa2[743:745],
        "Street Width Maximum": wa2[745:748],
        # "Filler": wa2[748:999],
        "Reason Code": wa2[1000],
        "Reason Code Qualifier": wa2[1001],
        "Warning Code Filler": wa2[1002:1004],
        "Return Code": wa2[1004:1006],
        "Number of Cross Streets at Low Address End": wa2[1006],
        "List of Cross Streets at Low Address End (Up to 5 B7SCs)": wa2[1007:1047],  # B7SC-Blank-Filled
        "Number of Cross Streets at High Address End": wa2[1047],
        "List of Cross Streets at High Address End (Up to 5 B7SCs)": wa2[1048:1088],  # B7SC-Blank-Filled
        "List of Cross Street Names at Low Address End": wa2[1088:1248],  # 5 x 32 = 160 Up to 5 Street Names
        "List of Cross Street Names at High Address End": wa2[1248:1408],  # 5 x 32 = 160 Up to 5 Street Names
        "BOE Preferred B7SC": wa2[1408:1416],
        "BOE Preferred Street Name": wa2[1416:1448],
        # "Filler": wa2[1448:1499]
    }