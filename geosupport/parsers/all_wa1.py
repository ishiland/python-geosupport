def parse_WA1(wa1):
    # Character-Only Work Area 1 (COW) - All Functions
    return {
        # INPUT FIELDS
        # "Geosupport Function Code": wa1[0:1],  # All
        # "House Number - Display Format": wa1[2:17],  # 1, 1A, 1B, 1E, AP
        # "House Number - Sort Format": wa1[18:28],  # 1, 1A, 1B, 1E, AP, D*
        # "Low House Number - Display Format20": wa1[29:44],  # Internal Use
        # "Low House Number - Sort Format": wa1[45:55],  # D*, Internal Use
        # "B10SC-1 (includes Borough Code 1, B5SC-1 and B7SC-1)": wa1[56:66],  # See next 2 entries
        # "Borough Code-1": wa1[56],  # Required for All Functions but BL, BN. Ignored if Fn 2 has Node Number input
        # "10SC21-1": wa1[57:66],  # All but 1N, B*
        # "Street Name-1": wa1[67:98],  # All but BL, BN, D*
        # "B10SC-2 (includes Borough Code 2, B5SC-2 and B7SC-2)": wa1[99:109],  # 2, 3*, D*
        # "Borough Code22-2": wa1[99],  # 2, 3*, D*
        # "10SC-2": wa1[100:109],  # 2, 3*, D*
        # "Street Name-2": wa1[110:141],  # 2, 3*
        # "B10SC-3 (includes Borough Code 3, B5SC-3 and B7SC-3)": wa1[142:152],  # 3*, D*
        # "Borough Code-3": wa1[142],  # 3*, D*
        # "10SC-3": wa1[143:152],  # 3*, D*
        # "Street Name-3": wa1[153:184],  # 3*
        # "BOROUGH BLOCK LOT (BBL)": wa1[185:194],  # BL
        # "Borough Code": wa1[185],  # BL
        # "Tax Block": wa1[186:190],  # BL
        # "Tax Lot": wa1[191:194],  # BL
        # "Filler for Tax Lot Version Number": wa1[195],  # Not Implemented
        # "Building Identification Number (BIN)": wa1[196:202],  # BN
        # "Compass Direction": wa1[203],  # 2, 3C, 3S
        # "Compass Direction for 2nd Intersection": wa1[204],  # 3S
        # "Node Number": wa1[205:211],  # 2, 2W
        # "Work Area Format Indicator23": wa1[212],  # All
        # "ZIP Code Input": wa1[213:217],  # 1*, AP
        # "Unit Input": wa1[218:231],  # 1*
        # "Filler": wa1[232:313],
        # "Long Work Area 2 Flag": wa1[314],  # 1A, BL
        # "House Number Justification Flag24": wa1[315],  # Not Implemented
        # "House Number Normalization Length25": wa1[316:317],  # Not Implemented
        # "House Number Normalization Override Flag": wa1[318],  # Internal Use
        # "Street Name Normalization Length Limit (SNL)": wa1[319:320],  # All but B*
        # "Street Name Normalization Format Flag26": wa1[321],  # All but B*
        # "Cross Street Names Flag27 a.k.a. Expanded Format Flag": wa1[322],  # 1, 1A, 1B, 1E, 2, 3, 3C
        # "Roadbed Request Switch": wa1[323],  # 1, 1B, 1E, 3S (Limited)
        # "Reserved for Internal Use": wa1[324],  # Internal GRC Flag
        # "Auxiliary Segment Switch": wa1[325],  # 3, 3C
        # "Browse Flag": wa1[326],  # 1*, 2, 3, 3C, BB, BF
        # "Real Streets Only Flag": wa1[327],  # 3S
        # "TPAD Switch": wa1[328],  # 1A, 1B, BL, BN
        # "Mode Switch": wa1[329],  # 1, 1E, 1A, 3, 3C, AP
        # "WTO Switch": wa1[330],  # All
        # "Filler": wa1[331:359],

        # OUTPUT Fields:
        "First Borough Name": wa1[360:369],  # All but D*
        "House Number - Display Format": wa1[369:385],  # 1, 1A, 1B, 1E, AP, D*
        "House Number - Sort Format": wa1[385:396],  # 1, 1A, 1B, 1E, AP, D*
        "B10SC - First Borough and Street Code": wa1[396:407],  # All but BL, BN
        "First Street Name Normalized": wa1[407:439],  # 439
        "B10SC - Second Borough and Street Code": wa1[439:450],  # 2, 3*, D*
        "Second Street Name Normalized": wa1[450:482],  # 2, 3*, D*
        "B10SC - Third Borough and Street Code": wa1[482:493],  # 3*, D*
        "Third Street Name Normalized": wa1[493:525],  # 3*, D*
        "BOROUGH BLOCK LOT": {# BL (Also 1, 1A, 1B, 1E if Cross Street Names Flag is 'E'; Also 1, 1E if Mode Switch is 'X')
        "Borough Code": wa1[526],  # BL (see BL comment above)
        "Tax Block": wa1[526:531],  # BL (see BL comment above)
        "Tax Lot": wa1[531:535]},  # BL (see BL comment above)
        "Filler for Tax Lot Version Number": wa1[535],  # Not Implemented
        "Low House Number - Display Format": wa1[536:552],  # Internal Use, D*
        "Low House Number - Sort Format": wa1[552:563],  # Internal Use, D*
        "Building Identification Number (BIN)": wa1[563:570],  # BN (see BBL functions list above)
        "Street Attribute Indicators": wa1[570:573],  # Internal Use
        "Reason Code 2": wa1[573],  # 1B - reflects 1A Extended
        "Reason Code Qualifier 2": wa1[574],  # 1B (See Reason Code 2)
        "Warning Code 2": wa1[575:577],  # 1B (not used)
        "Geosupport Return Code 2": wa1[577:579],  # 1B (See Reason Code 2)
        "Message 2": wa1[579:659],  # 1B (See Reason Code 2)
        "Node Number": wa1[659:666],  # 2, 2W
        "UNIT - SORT FORMAT": {  # 1*
            "Unit - Type": wa1[666:670],  # 1*
            "Unit - Identifier": wa1[670:680],  # 1*
            "Unit - Display Format": wa1[680:694]},  # 1*
        "Filler": wa1[694:705],
        "NIN28": wa1[705:711],  # Not Implemented
        "Street Attribute Indicator": wa1[712],  # Internal Use
        "Reason Code": wa1[713],  # All
        "Reason Code Qualifier": wa1[714],  # 1A, BL, BN
        "Warning Code": wa1[714:716],  # All (not used)
        "Geosupport Return Code": wa1[716:718],  # All
        "Message": wa1[718:798],  # All
        "Number of Street Codes and Street Names in List": wa1[798:800],  # 1*, 2, 3*, BB, BF - (up to 10)
        "List of Street Codes": wa1[800:880],  # 1*, 2, 3*, BB, BF - (10 B7SC's)
        "List of Street Names": wa1[880:1200],  # 1*, 2, 3*, BB, BF - (10 Street Name Fields, 32 Bytes Each)
    }