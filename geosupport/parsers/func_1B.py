
def parse_1B(wa2):
    return{
        # Work Area 2 (COW) - Function 1B
        # "Internal Use": wa2[0:20],
        "Continuous Parity Indicator/Duplicate Address Indicator": wa2[21],
        "Low House Number of Block Face": wa2[22:33],  # Sort Format
        "High House Number of Block Face": wa2[33:44],  # Sort Format
        "DCP Preferred LGC": wa2[44:46],
        "Number of Cross Streets at Low Address End": wa2[46],
        "List of Cross Streets at Low Address End (Up to 5 B5SCs)": wa2[47:77],  # B5SC - Blank-Filled
        "Number of Cross Streets at High Address End": wa2[77],
        "List of Cross Streets at High Address End (Up to 5 B5SCs)": wa2[78:108],  # B5SC - Blank-Filled
        "LION KEY": {
            "Borough Code": wa2[108],
            "Face Code": wa2[109:113],
            "Sequence Number": wa2[113:118]},
        "Special Address Generated Record Flag": wa2[118],
        "Side of Street Indicator": wa2[119],
        "Segment Length in Feet": wa2[120:125],
        "Spatial X-Y Coordinates of Address": wa2[125:139],
        "Reserved for Possible Z Coordinate": wa2[139:146],
        "Community Development Eligibility Indicator": wa2[146],
        "Marble Hill/Rikers Island Alternative Borough Flag": wa2[147],
        "DOT Street Light Contractor Area": wa2[148],
        "COMMUNITY DISTRICT": wa2[149:152],
        "Community District Borough Code": wa2[149],
        "Community District Number": wa2[150:152],
        "ZIP Code": wa2[152:157],
        "Election District": wa2[157:160],
        "Assembly District": wa2[160:161],
        "Split Election District Flag": wa2[162],
        "Congressional District": wa2[163:165],
        "State Senatorial District": wa2[165:167],
        "Civil Court District": wa2[167:169],
        "City Council District": wa2[169:171],
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
        # "Filler": wa2[202],  # Was Split Community School District Flag
        "Community School District": wa2[203:205],
        "Atomic Polygon": wa2[205:208],  # Was Dynamic Block
        "Police Patrol Borough": wa2[208:210],
        "Feature Type Code": wa2[210],
        "Segment Type Code": wa2[211],
        "Alley or Cross Street List Flag": wa2[212],
        "Coincidence Segment Count": wa2[213],
        # "Filler": wa2[214:216],
        "1990 Census Tract": wa2[217:223],
        "2010 Census Tract": wa2[223:229],
        "2010 Census Block": wa2[229:233],
        "2000 Census Tract": wa2[234:240],
        "2000 Census Block": wa2[240:244],
        "2000 Census Block Suffix": wa2[244],
        "Neighborhood Tabulation Area (NTA)": wa2[245:249],
        "DSNY Snow Priority Code": wa2[249],  # Dept. of Sanitation
        "DSNY Organic Recycling Schedule": wa2[250:255],  # Dept. of Sanitation
        "DSNY Bulk Pickup Schedule": wa2[255:260],  # Dept. of Sanitation
        "Hurricane Evacuation Zone (HEZ)": wa2[260:262],
        # "Filler": wa2[262:272],
        "Underlying Address Number for NAPs": wa2[273:284],  # Sort Format
        "Underlying B7SC": wa2[284:292],
        "Segment Identifier": wa2[292:299],
        "Curve Flag": wa2[299],
        "List of 4 LGC's": wa2[300:308],
        "BOE LGC Pointer": wa2[308],
        "Segment Azimuth": wa2[309:312],
        "Segment Orientation": wa2[312],
        "SPATIAL COORDINATES OF SEGMENT": wa2[313:355],
        "X Coordinate, Low Address End": wa2[313:320],
        "Y Coordinate, Low Address End": wa2[320:327],
        # "Z Coordinate, Low Address End": wa2[327:334],  # Not Implemented
        "X Coordinate, High Address End": wa2[334:341],
        "Y Coordinate, High Address End": wa2[341:348],
        # "Z Coordinate, High Address End": wa2[348:355],  # Not Implemented
        "SPATIAL COORDINATES OF CENTER OF CURVATURE": wa2[355:376],
        "X Coordinate": wa2[355:362],
        "Y Coordinate": wa2[362:369],
        # "Z Coordinate": wa2[369:376],  # Not Implemented
        "Radius of Circle": wa2[376:383],
        "Secant Location Related to Curve": wa2[383],  # L - Left, R - Right
        "Angle to From Node - Beta Value": wa2[384:389],  # Beta & Alpha Used to Calculate Coordinates
        "Angle to To Node - Alpha Value": wa2[389:394],
        "From LION Node ID": wa2[394:401],
        "To LION Node ID": wa2[401:408],
        "LION Key for Vanity Address": wa2[408:418],
        "Side of Street of Vanity Address": wa2[418],
        "Split Low House Number": wa2[419:430],
        "Traffic Direction": wa2[430],
        "Turn Restrictions": wa2[431:441],
        "Fraction for Curve Calculation": wa2[441:444],
        "Roadway Type": wa2[444:446],
        "Physical ID": wa2[446:453],
        "Generic ID": wa2[453:460],
        "NYPD ID": wa2[460:467],
        "FDNY ID": wa2[467:474],
        "Bike Lane 2": wa2[474:476],
        "Bike Traffic Direction": wa2[476:478],
        # "Filler": wa2[478:481],  # Was Blockface ID See bytes 730-739
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
        "No Cross Street Calculation Flag": wa2[548],
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
            "Z Coordinate, High Address End": wa2[722:729]},  # Not Implemented
        "Blockface ID": wa2[729:739],
        "Number of Travel Lanes on the Street": wa2[739:741],
        "Number of Parking Lanes on the Street": wa2[741:743],
        "Number of Total Lanes on the Street": wa2[743:745],
        "Street Width Maximum": wa2[745:748],
        # "Filler": wa2[748:999],
        "Reason Code": wa2[1000],
        "Reason Code Qualifier": wa2[1001],
        "Warning Code": wa2[1002:1004],
        "Return Code": wa2[1004:1006],
        # "Number of Cross Streets at Low Address End": wa2[1006], # duplicate key ??
        "List of Cross Streets at Low Address End (Up to 5 B7SCs)": wa2[1007:1047],  # B7SC - Blank Filled
        "No. of Cross Streets at High Address End": wa2[1048],
        "List of Cross Streets at High Address End (Up to 5 B7SCs)": wa2[1048:1088],  # B7SC - Blank Filled
        "List of Cross Street Names at Low Address End": wa2[1088:1248],  # 5 x 32 = 160 Up to 5 Street Names
        "List of Cross Street Names at High Address End": wa2[1248:1408],  # 5 x 32 = 160 Up to 5 Street Names
        "BOE Preferred B7SC": wa2[1408:1416],
        "BOE Preferred Street Name": wa2[1416:1448],
        # "Filler": wa2[1448:1499],

        # PROPERTY LEVEL INFORMATION
        # (Based On Functions 1A, BL, BN Extended)
        # "Internal Use": wa2[1500:1520],
        "Continuous Parity Indicator / Duplicate Address Indicator": wa2[1521],
        "Low House Number of Defining Address Range": wa2[1522:1533],  # Sort Format
        "BOROUGH BLOCK LOT (BBL)": {  # Billing BBL if Condo
        "Borough Code": wa2[1533],
        "Tax Block": wa2[1534:1539],
        "Tax Lot": wa2[1539:1543]},
        # "Filler for Tax Lot Version Number": wa2[1543],  # Not Implemented
        "RPAD Self-Check Code (SCC) for BBL": wa2[1544],
        # # "Filler": wa2[1545],
        "RPAD Building Classification Code": wa2[1546:1548],
        "Corner Code": wa2[1548:1550],
        "Number of Existing Structures on Lot": wa2[1550:1554],
        "Number of Street Frontages of Lot": wa2[1554:1556],
        "Interior Lot Flag": wa2[1556],
        "Vacant Lot Flag": wa2[1557],
        "Irregularly-Shaped Lot Flag": wa2[1558],
        "Marble Hill/Rikers Island Alternate Borough Flag": wa2[1559],
        "List of Geographic Identifiers Overflow Flag": wa2[1560],  # When = 'E', there are more than 21 addrs for Fn 1B (based on Fn 1A)
        # "STROLLING KEY": wa2[1561:1579],  # Not Implemented
        "Borough": wa2[1561],
        "5-Digit Street Code of ON- Street": wa2[1562:1567],
        # "Side of Street Indicator": wa2[1567], duplicate?
        "High House Number": wa2[1568:1580],  # Sort Format
        # "Filler": wa2[1579],
        "Reserved for Internal Use": wa2[1580],
        "Building Identification Number (BIN) of Input Address or NAP": wa2[1581:1588],
        # "Condominium Flag": wa2[1588],  # If condo, = 'C'
        # # "Filler": wa2[1589],
        "DOF Condominium Identification Number": wa2[1590:1594],
        "Condominium Unit ID Number": wa2[1594:1601],  # Not Implemented
        "Condominium Billing BBL": wa2[1601:1611],
        # "Filler - Tax Lot Version No. Billing BBL": wa2[1611],  # Not Implemented
        "Self-Check Code (SCC) of Billing BBL": wa2[1613],
        "Low BBL of this Building's Condominium Units": wa2[1613:1624],
        # "Filler - Tax Lot Version No. of Low BBL": wa2[1623],  # Not Implemented
        "High BBL of this Building's Condominium Units": wa2[1624:1634],
        # "Filler - Tax Log Version No. of High BBL": wa2[1634],  # Not Implemented
        # # "Filler": wa2[1635:1649],
        "Cooperative ID Number": wa2[1650:1653],
        "SBVP (SANBORN MAP IDENTIFIER)": wa2[1654:1662],
        "Sanborn Borough Code": wa2[1654],
        "Volume Number": wa2[1655:1657],
        "Volume Number Suffix": wa2[1657],
        "Page Number": wa2[1658:1661],
        "Page Number Suffix": wa2[1661],
        "DCP Commercial Study Area": wa2[1662:1667],
        "Tax Map Number Section & Volume": wa2[1667:1672],
        # "Reserved for Tax Map Page Number": wa2[1672:1675],  # Not Implemented
        # # "Filler": wa2[1676:1678],
        "Latitude - centroid": wa2[1679:1687],
        "Longitude - centroid": wa2[1688:1699],
        "XCoord - centroid": wa2[1699:1706],
        "YCoord - centroid": wa2[1706:1713],
        # "X-Y Coordinates of Lot Centroid": wa2[1699:1713],
        "Business Improvement District (BID)": wa2[1713:1719],
        "TPAD BIN Status": wa2[1719],  # TPAD Request
        "TPAD New BIN": wa2[1720:1727],  # TPAD Request
        "TPAD New BIN Status": wa2[1727],  # TPAD Request
        "TPAD Conflict Flag": wa2[1728],  # TPAD Request
        # # "Filler": wa2[1729:1737],
        # # "Internal Use": wa2[1738:1745],
        # "Reason Code": wa2[1746],
        # "Reason Code Qualifier": wa2[1747],
        # "Warning Code": wa2[1748:1749],
        # "Return Code": wa2[1750:1751],
        # # "Filler": wa2[1752:1859],
        "Number of Entries in List of Geographic Identifiers": wa2[1860:1864],  # Maximum is 21
        "LIST OF GEOGRAPHIC IDENTIFIERS": wa2[1864:4300],
        # Variable length list of up to 21 entries; each is 116 bytes long, structured as follows
        # Maximum is 21 entries. 21 x 116 = 2436
        # "Low House Number": wa2[0:15],  # Display format
        # "High House Number": wa2[16:31],  # Display format
        # "Borough Code": wa2[32],  # Start of B7SC
        # "5-Digit Street Code": wa2[33:38],
        # "DCP-Preferred Local Group Code (LGC)": wa2[38:39],
        # "Building Identification Number": wa2[40:47],
        # "Side of Street Indicator": wa2[47],  # L - Left, R - Right
        # "Geographic Identifier Entry Type Code": wa2[48],  # N - NAP (Simplex)
        # G - Complex NAP
        # X - Constituent Entity of
        #       Complex NAP
        # B - NAUB
        # F - Frontage
        # W - Blank Wall
        # Q - Pseudo Address
        # T - Tunnel
        # U - Misc. Structure
        # V - Vanity Address
        # O - Out-of-Sequence
        #       Address
        # Blank - Normal
        # "TPAD BIN Status": wa2[49],  # TPAD Request
        # "Street Name": wa2[50:81],
        # "Filler": wa2[82:115]
    }