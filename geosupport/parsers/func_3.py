
def parse_3(wa2):
    # Work Area 2 (COW) - Function 3

    regular = {
        # "Internal Use": wa2[0:20],
        "Duplicate Key Flag or Continuous Parity": wa2[21],
        "Locational Status of Segment": wa2[22],
        "County Boundary Indicator": wa2[23],
        "DCP-Preferred LGC for Street 1": wa2[24:26],  # 'On' Street
        "DCP-Preferred LGC for Street 2": wa2[26:28],  # Input Cross Street with Lower B5SC value
        "DCP-Preferred LGC for Street 3": wa2[28:30],  # Input Cross Street with Higher B5SC value
        "Number of Cross Streets at Low Address End": wa2[30],
        "List of Cross Streets at Low Address End (Up to five B5SCs, 6 bytes each)": wa2[31:61],  # Blank Filled
        "Number of Cross Streets at High Address End": wa2[61],
        "List of Cross Streets at High Address End (Up to five B5SCs, 6 bytes each)": wa2[62:92],  # Blank Filled
        "Cross Street Reversal Flag": wa2[92],
        "LION KEY": wa2[93:103],
        "LION Borough Code": wa2[93],
        "LION Face Code": wa2[94:98],
        "LION Sequence Number": wa2[98:103],
        "Generated Record Flag": wa2[103],
        "Length of Segment in Feet": wa2[104:109],
        "Segment Azimuth": wa2[109:112],
        "Segment Orientation": wa2[112],
        "Marble Hill/Rikers Island Alternative Borough Flag": wa2[114],
        "From Node": wa2[114:121],
        "To Node": wa2[121:128],
        "DSNY Snow Priority Code": wa2[129],  # Dept. of Sanitation
        # "Filler": wa2[129:132],
        "Segment Identifier": wa2[133:140],
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
                "Community District Number": wa2[151:153]},
            "Low House Number": wa2[153:169],  # Display Format
            "High House Number": wa2[169:185],  # Display Format
            "Future Use": wa2[185:217],
            "Community Development Eligibility Indicator": wa2[217],
            "ZIP Code": wa2[218:223],
            "Health Area": wa2[223:227],
            "Police Patrol Borough Command": wa2[227],
            "Police Precinct": wa2[228:231],
            "Fire Division": wa2[231:233],
            "Fire Battalion": wa2[233:235],
            "Fire Company Type": wa2[235],
            "Fire Company Number": wa2[236:239],
            "Community School District": wa2[239:241],
            "Atomic Polygon": wa2[241:243],  # Was Dynamic Block
            "Election District (ED)": wa2[244:247],
            "Assembly District (AD)": wa2[247:249],
            "Police Patrol Borough": wa2[249:251],
            # "Filler": wa2[251],
            "Borough Code": wa2[252],
            "1990 Census Tract": wa2[253:259],
            "2010 Census Tract": wa2[259:265],
            "2010 Census Block": wa2[265:269],
            # "2010 Census Block Suffix": wa2[269],  # Not Implemented
            "2000 Census Tract": wa2[270:276],
            "2000 Census Block Suffix": wa2[281],
            # "Filler": wa2[281:287],  # Was Blockface ID. See Function 3 Extended
            "Neighborhood Tabulation Area (NTA)": wa2[288:292],
            # "Filler": wa2[292:299]
        },
        "RIGHT SIDE": {
            "COMMUNITY DISTRICT": {
                "Community District Borough Code": wa2[300],
                "Community District Number": wa2[301:303]},
            "Low House Number": wa2[303:319],  # Display Format
            "High House Number": wa2[319:335],  # Display Format
            "Future Use": wa2[335:367],
            "Community Development Eligibility Indicator": wa2[367],
            "ZIP Code": wa2[368:373],
            "Health Area": wa2[373:377],
            "Police Patrol Borough Command": wa2[377],
            "Police Precinct": wa2[378:381],
            "Fire Division": wa2[381:383],
            "Fire Battalion": wa2[383:385],
            "Fire Company Type": wa2[385],
            "Fire Company Number": wa2[386:389],
            "Community School District": wa2[389:391],
            "Atomic Polygon": wa2[391:394],  # Was Dynamic Block
            "Election District (ED)": wa2[394:397],
            "Assembly District (AD)": wa2[397:399],
            "Police Patrol Borough": wa2[399:401],
            # "Filler": wa2[401],
            # "Borough Code": wa2[402],  # Internal Use
            "1990 Census Tract": wa2[403:409],
            "2010 Census Tract": wa2[409:415],
            "2010 Census Block": wa2[415:419],
            # "2010 Census Block Suffix": wa2[419],  # Not Implemented
            "2000 Census Tract": wa2[420:426],
            "2000 Census Block": wa2[426:430],
            "2000 Census Block Suffix": wa2[430],
            # "Filler": wa2[431:437],  # Was Blockface ID See Function 3 Extended
            "Neighborhood Tabulation Area (NTA)": wa2[438:442],
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
        "Segment Count": wa2[456:460],  # Number of Segments
        "Segment IDs": wa2[460:950]  # Up to 70 Segment IDs 7 bytes each; 7 x 70 = 490
    }


def parse_3_ext(wa2):
    # Work Area 2 (COW) - Function 3 Extended
    return{
        # "Same as Regular Work Area 2 Function 3": wa2[0:449],
        "List of 4 LGCs for Street 1": wa2[450:458],  # 'On' Street
        "List of 4 LGCs for Street 2": wa2[458:466],  # Input Cross Street with Lower B5SC
        "List of 4 LGCs for Street 3": wa2[466:474],  # Input Cross Street with Higher B5SC
        "Left Health Center District": wa2[474:476],
        "Right Health Center District": wa2[476:478],
        "Filler": wa2[478],  # Was Split Comm Schl District Flag
        "Traffic Direction": wa2[479],
        "Roadway Type": wa2[480:482],
        "Physical ID": wa2[482:489],
        "Generic ID": wa2[489:496],
        "NYPD ID": wa2[496:501],
        "FDNY ID": wa2[503:510],
        "Street Status": wa2[510],
        "Street Width": wa2[511:514],
        # "Street Width Irregular": wa2[514],  # Not Implemented
        "Bike Lane": wa2[515],  # Will be retired. See Bike Lane 2
        # "Federal Classification Code": wa2[516:517],  # Not Implemented
        "Right of Way Type": wa2[518],
        # "List of 5 Additional LGCs for Street 1": wa2[519:528],  # Not Implemented
        "Legacy ID": wa2[529:536],
        "Left NTA Name": wa2[536:611],
        "Right NTA Name": wa2[611:686],
        "FROM SPATIAL COORDINATES": {  # From Node
            "From X Coordinate": wa2[686:693],
            "From Y Coordinate": wa2[693:700]},
        "TO SPATIAL COORDINATES": {  # To Node
            "To X Coordinate": wa2[700:707],
            "To Y Coordinate": wa2[707:714]},
        "Latitude of From Intersection": wa2[714:713],
        "Longitude of From Intersection": wa2[723:734],
        "Latitude of To Intersection": wa2[734:743],
        "Longitude of To Intersection": wa2[743:754],
        "Left Blockface ID": wa2[754:764],
        "Right Blockface ID": wa2[764:774],
        "Number of Travel Lanes on the Street": wa2[774:776],
        "Number of Parking Lanes on the Street": wa2[776:778],
        "Number of Total Lanes on the Street": wa2[778:780],
        "Bike Lane 2": wa2[780:782],
        "Street Width Maximum": wa2[782:785],
        "Bike Traffic Direction": wa2[785:787],
        # "Filler": wa2[787:999],
    }


def parse_3_ext_aux(wa2):
    # Work Area 2 (COW) - Function 3 Extended with Auxiliary Segment List
    return{
        # "Same as Work Area 2 for Function 3 Extended": wa2[0:999],
        # "Filler": wa2[1000:1005],
        "Segment Count": wa2[1006:1010],  # Number of Segments
        "Segment IDs": wa2[1010:1500],  # Up to 70 Segment IDs 7 bytes each; 7 x 70 = 490
    }
