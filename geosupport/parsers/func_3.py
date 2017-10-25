
def parse_3(wa2):
    # Work Area 2 (COW) - Function 3

    regular = {
        # "Internal Use": wa2[0:20],
        "Duplicate Key Flag or Continuous Parity": wa2[21],
        "Locational Status of Segment": wa2[22],
        "County Boundary Indicator": wa2[23],
        "DCP-Preferred LGC for Street 1": wa2[24:25],  # 'On' Street
        "DCP-Preferred LGC for Street 2": wa2[26:27],  # Input Cross Street with Lower B5SC value
        "DCP-Preferred LGC for Street 3": wa2[28:29],  # Input Cross Street with Higher B5SC value
        "Number of Cross Streets at Low Address End": wa2[30],
        "List of Cross Streets at Low Address End (Up to five B5SCs, 6 bytes each)": wa2[31:60],  # Blank Filled
        "Number of Cross Streets at High Address End": wa2[61],
        "List of Cross Streets at High Address End (Up to five B5SCs, 6 bytes each)": wa2[62:91],  # Blank Filled
        "Cross Street Reversal Flag": wa2[92],
        "LION KEY": wa2[93:102],
        "LION Borough Code": wa2[93],
        "LION Face Code": wa2[94:97],
        "LION Sequence Number": wa2[98:102],
        "Generated Record Flag": wa2[103],
        "Length of Segment in Feet": wa2[104:108],
        "Segment Azimuth": wa2[109:111],
        "Segment Orientation": wa2[112],
        "Marble Hill/Rikers Island Alternative Borough Flag": wa2[113],
        "From Node": wa2[114:120],
        "To Node": wa2[121:127],
        "DSNY Snow Priority Code": wa2[128],  # Dept. of Sanitation
        # "Filler": wa2[129:132],
        "Segment Identifier": wa2[133:139],
        "DOT Street Light Contractor Area": wa2[140],
        "Curve Flag": wa2[141],
        "Dog Leg Flag": wa2[142],
        "Feature Type Code": wa2[143],
        "Segment Type Code": wa2[144],
        "Coincident Segment Count": wa2[145],
        # "Filler": wa2[146:149],
        "LEFT SIDE": {
            "COMMUNITY DISTRICT": {
                "Community District Borough  Code": wa2[150],
                "Community District Number": wa2[151:152]},
            "Low House Number": wa2[153:168],  # Display Format
            "High House Number": wa2[169:184],  # Display Format
            "Future Use": wa2[185:216],
            "Community Development Eligibility Indicator": wa2[217],
            "ZIP Code": wa2[218:222],
            "Health Area": wa2[223:226],
            "Police Patrol Borough Command": wa2[227],
            "Police Precinct": wa2[228:230],
            "Fire Division": wa2[231:232],
            "Fire Battalion": wa2[233:234],
            "Fire Company Type": wa2[235],
            "Fire Company Number": wa2[236:238],
            "Community School District": wa2[239:240],
            "Atomic Polygon": wa2[241:243],  # Was Dynamic Block
            "Election District (ED)": wa2[244:246],
            "Assembly District (AD)": wa2[247:248],
            "Police Patrol Borough": wa2[249:250],
            # "Filler": wa2[251],
            "Borough Code": wa2[252],
            "1990 Census Tract": wa2[253:258],
            "2010 Census Tract": wa2[259:264],
            "2010 Census Block": wa2[265:268],
            # "2010 Census Block Suffix": wa2[269],  # Not Implemented
            "2000 Census Tract": wa2[270:275],
            "2000 Census Block Suffix": wa2[280],
            # "Filler": wa2[281:287],  # Was Blockface ID. See Function 3 Extended
            "Neighborhood Tabulation Area (NTA)": wa2[288:291],
            # "Filler": wa2[292:299]
        },
        "RIGHT SIDE": {
            "COMMUNITY DISTRICT": {
                "Community District Borough Code": wa2[300],
                "Community District Number": wa2[301:302]},
            "Low House Number": wa2[303:318],  # Display Format
            "High House Number": wa2[319:334],  # Display Format
            "Future Use": wa2[335:366],
            "Community Development Eligibility Indicator": wa2[367],
            "ZIP Code": wa2[368:372],
            "Health Area": wa2[373:376],
            "Police Patrol Borough Command": wa2[377],
            "Police Precinct": wa2[378:380],
            "Fire Division": wa2[381:382],
            "Fire Battalion": wa2[383:384],
            "Fire Company Type": wa2[385],
            "Fire Company Number": wa2[386:388],
            "Community School District": wa2[389:390],
            "Atomic Polygon": wa2[391:393],  # Was Dynamic Block
            "Election District (ED)": wa2[394:396],
            "Assembly District (AD)": wa2[397:398],
            "Police Patrol Borough": wa2[399:400],
            # "Filler": wa2[401],
            # "Borough Code": wa2[402],  # Internal Use
            "1990 Census Tract": wa2[403:408],
            "2010 Census Tract": wa2[409:414],
            "2010 Census Block": wa2[415:418],
            # "2010 Census Block Suffix": wa2[419],  # Not Implemented
            "2000 Census Tract": wa2[420:425],
            "2000 Census Block": wa2[426:429],
            "2000 Census Block Suffix": wa2[430],
            # "Filler": wa2[431:437],  # Was Blockface ID See Function 3 Extended
            "Neighborhood Tabulation Area (NTA)": wa2[438:441],
            # "Filler": wa2[442:449]
        }
    }
    # Get extended results
    regular = regular.copy()
    regular.update(parse_3_ext(wa2))
    return regular


def parse_3_aux_seg(wa2):
    # Work Area 2 (COW) - Function 3 with Auxiliary Segment List
    return{
        # "Same as Regular Work Area 2 for Function 3": wa2[0:449],
        # "Filler": wa2[450:455],
        "Segment Count": wa2[456:459],  # Number of Segments
        "Segment IDs": wa2[460:949]  # Up to 70 Segment IDs 7 bytes each; 7 x 70 = 490
    }


def parse_3_ext(wa2):
    # Work Area 2 (COW) - Function 3 Extended
    return{
        # "Same as Regular Work Area 2 Function 3": wa2[0:449],
        "List of 4 LGCs for Street 1": wa2[450:457],  # 'On' Street
        "List of 4 LGCs for Street 2": wa2[458:465],  # Input Cross Street with Lower B5SC
        "List of 4 LGCs for Street 3": wa2[466:473],  # Input Cross Street with Higher B5SC
        "Left Health Center District": wa2[474:475],
        "Right Health Center District": wa2[476:477],
        "Filler": wa2[478],  # Was Split Comm Schl District Flag
        "Traffic Direction": wa2[479],
        "Roadway Type": wa2[480:481],
        "Physical ID": wa2[482:488],
        "Generic ID": wa2[489:495],
        "NYPD ID": wa2[496:502],
        "FDNY ID": wa2[503:509],
        "Street Status": wa2[510],
        "Street Width": wa2[511:513],
        # "Street Width Irregular": wa2[514],  # Not Implemented
        "Bike Lane": wa2[515],  # Will be retired. See Bike Lane 2
        # "Federal Classification Code": wa2[516:517],  # Not Implemented
        "Right of Way Type": wa2[518],
        # "List of 5 Additional LGCs for Street 1": wa2[519:528],  # Not Implemented
        "Legacy ID": wa2[529:535],
        "Left NTA Name": wa2[536:610],
        "Right NTA Name": wa2[611:685],
        "FROM SPATIAL COORDINATES": {  # From Node
            "From X Coordinate": wa2[686:692],
            "From Y Coordinate": wa2[693:699]},
        "TO SPATIAL COORDINATES": {  # To Node
            "To X Coordinate": wa2[700:706],
            "To Y Coordinate": wa2[707:713]},
        "Latitude of From Intersection": wa2[714:712],
        "Longitude of From Intersection": wa2[723:733],
        "Latitude of To Intersection": wa2[734:742],
        "Longitude of To Intersection": wa2[743:753],
        "Left Blockface ID": wa2[754:763],
        "Right Blockface ID": wa2[764:773],
        "Number of Travel Lanes on the Street": wa2[774:775],
        "Number of Parking Lanes on the Street": wa2[776:777],
        "Number of Total Lanes on the Street": wa2[778:779],
        "Bike Lane 2": wa2[780:781],
        "Street Width Maximum": wa2[782:784],
        "Bike Traffic Direction": wa2[785:786],
        # "Filler": wa2[787:999],
    }


def parse_3_ext_aux(wa2):
    # Work Area 2 (COW) - Function 3 Extended with Auxiliary Segment List
    return{
        # "Same as Work Area 2 for Function 3 Extended": wa2[0:999],
        # "Filler": wa2[1000:1005],
        "Segment Count": wa2[1006:1009],  # Number of Segments
        "Segment IDs": wa2[1010:1499],  # Up to 70 Segment IDs 7 bytes each; 7 x 70 = 490
    }
