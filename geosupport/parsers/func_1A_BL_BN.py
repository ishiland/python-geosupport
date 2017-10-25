

def parse_1A_BL_BN(wa2):
    # Work Area 2 (COW) - Functions 1A, BL, BN
    return{
        # "Internal Use": wa2[0:20],
        "Continuous Parity Indicator / Duplicate Address Indicator": wa2[21],
        "Low House Number of Defining Address Range": wa2[22:32],  # Sort Format
        "BOROUGH BLOCK LOT (BBL)": {  # Billing BBL if Condo
            "Borough Code": wa2[33],
            "Tax Block": wa2[34:38],
            "Tax Lot": wa2[39:42]},
        # "Filler for Tax Lot Version Number": wa2[43],  # Not Implemented
        "RPAD Self-Check Code (SCC) for BBL": wa2[44],
        # "Filler": wa2[45],
        "RPAD Building Classification Code": wa2[46:47],
        "Corner Code": wa2[48:49],
        "Number of Existing Structures on Lot": wa2[50:53],
        "Number of Street Frontages of Lot": wa2[54:55],
        "Interior Lot Flag": wa2[56],
        "Vacant Lot Flag": wa2[57],
        "Irregularly-Shaped Lot Flag": wa2[58],
        "Marble Hill/Rikers Island Alternate Borough Flag": wa2[59],
        "List of Geographic Identifiers (LGI) Overflow Flag": wa2[60],  # When = 'E', there are more than 21 addrs for Fns 1A and BL.
        # "STROLLING KEY": wa2[61:79],  # Not Implemented
        # "Borough": wa2[61],  # Not Implemented
        # "5-Digit Street Code of 'On' Street": wa2[62:66],  # Not Implemented
        # "Side of Street Indicator": wa2[67],  # Not Implemented
        # "High House Number - Sort Format": wa2[68:78],  # Not Implemented
        # "Filler": wa2[79],  # Not Implemented
        "Reserved for Internal Use": wa2[80],
        "Building Identification Number (BIN) of Input Address or NAP": wa2[81:87],
        "Condominium Flag": wa2[88],  # If condo, = 'C';
        # "Filler": wa2[89],
        "DOF Condominium Identification Number": wa2[90:93],
        # "Condominium Unit ID Number": wa2[94:100],  # Not Implemented
        "Condominium Billing BBL": wa2[101:110],
        # "Filler - Tax Lot Version No. for Billing BBL": wa2[111],  # Not Implemented
        "Self-Check Code (SCC) of Billing BBL": wa2[112],
        "LOW BBL OF THIS BUILDING'S CONDOMINIUM UNITS": {
            "Tax Block": wa2[114:118],
            "Tax Lot": wa2[119:122]},
        # "Filler for Tax Lot Version No. of Low BBL": wa2[123],  # Not Implemented
        "HIGH BBL OF THIS BUILDING'S CONDOMINIUM UNITS": {
            "Borough Code": wa2[124],  # Condo
            "Tax Block": wa2[125:129],
            "Tax Lot": wa2[130:133]},
        # "Filler for Tax Lot Version No. of High BBL": wa2[134],  # Not Implemented
        # "Filler": wa2[135:149],
        "Cooperative ID Number": wa2[150:153],
        "SBVP (SANBORN MAP IDENTIFIER)": {
            "Sanborn Borough Code": wa2[154],
            "Volume Number": wa2[155:156],
            "Volume Number Suffix": wa2[157],
            "Page Number": wa2[158:160],
            "Page Number Suffix": wa2[161]},
        "DCP Commercial Study Area": wa2[162:166],
        "Tax Map Number Section & Volume": wa2[167:171],
        # "Reserved for Tax Map Page Number": wa2[172:175],  # Not Implemented
        # "Filler": wa2[176:178],
        "Latitude": wa2[179:187],
        "Longitude": wa2[188:198],
        "X-Y Coordinates of Tax Lot Centroid (Internal to Lot)": wa2[199:212],  # Previously X-Y Coordinates of COGIS Annotation Point
        "Business Improvement District (BID)": wa2[213:218],
        "TPAD BIN Status (for DM job)": wa2[219],  # TPAD request
        "TPAD New BIN": wa2[220:226],  # TPAD request
        "TPAD New BIN Status": wa2[227],  # TPAD request
        "TPAD Conflict Flag": wa2[228],  # TPAD request
        # "Filler": wa2[229:237],
        # "List of 4 LGCs": wa2[238:245],  # Internal Use
        "Number of Entries in List of Geographic  Identifiers": wa2[246:249],  # Maximum of 21 entries

        "LIST OF GEOGRAPHIC IDENTIFIERS": wa2[250:1362],  # Maximum of 21 entries, each 53 bytes long: 21x53 = 1,113
        # Variable length list of up to 21 entries, each 53 - bytes long, structured as follows
        # "Low House Number": wa2[0:15],  # Display format
        # "High House Number": wa2[16:31],  # Display format
        # "Borough Code": wa2[32],  # Start of B7SC
        # "5-Digit Street Code": wa2[33:37],  # Part of B7SC
        # "DCP-Preferred Local Group Code (LGC)": wa2[38:39],  # End of B7SC
        # "Building Identification Number (BIN)": wa2[40:46],
        # "Side of Street Indicator": wa2[47],  # L - Left, R - Right
        # "Geographic Identifier Entry Type Code": wa2[48],  # N - NAP (Simplex)
        # G - Complex NAP
        # X - Constituent entity of Complex NAP
        # B - NAUB
        # F - Frontage
        # W - Blank Wall
        # Q - Pseudo Addr
        # T - Tunnel
        # U - Misc. Structure
        # V - Vanity Address
        # O - Out-of Sequence Address
        # Blank - Normal
        # "TPAD BIN Status": wa2[49],  # TPAD Request
        # "Filler": wa2[50:52]
    }

def parse_long(wa2):
    # Long Work Area 2 (COW) - Functions 1A, BL
    return {
        # "Same as Regular Work Area 2 - Functions 1A, BL, BN": wa2[0:245],
        "Number of Buildings on Tax Lot": wa2[246:249],  # Maximum of 2,500
        "LIST OF BUILDINGS ON TAX LOT": wa2[250:17749],
        # Variable length list of up to 2,500 entries; each is 7 bytes long structured as follows:
        # Maximum of 2,500 entries, each 7 bytes long. 7 x 2,500 = 17,500
        # "Building Identification Number (BIN)": wa2[-2:-8],
    }


def parse_long_tpad(wa2):
    # TPAD Long Work Area 2 (COW) - Functions 1A, BL
    return{
        # "Same as Regular Work Area 2 - Functions 1A, BL, BN": wa2[0:245],
        "Number of Buildings on Tax Lot": wa2[246:249],  # Maximum is 2,187
        "LIST OF BUILDINGS ON TAX LOT": wa2[250:17745],
        # Variable length list of up to 2,187 entries; each is 8 bytes long, structured as follows
        # Maximum of 2,187 entries, each 8 bytes long. 8 x 2,187 = 17,496
        # "TPAD BIN": wa2[0:6],
        # "TPAD BIN Status": wa2[7],
        # "Filler": wa2[17746:17749]
    }


def parse_ext(wa2):
    # Work Area 2 (COW) - Functions 1A, BL, BN Extended
    regular = parse_1A_BL_BN(wa2)
    return{
        # "Same as Regular Work Area 2 - Functions 1A, BL, BN": wa2[0:245],
        # "Reason Code": wa2[246],  # Same as Work Area 1
        # "Reason Code Qualifier": wa2[247],  # Same as Work Area 1
        # "Warning Code": wa2[248:249],  # Not used
        # "Return Code (GRC)": wa2[250:251],  # Same as Work Area 1
        # "Filler": wa2[252:359],
        "Number of Entries in List of Geographic Identifiers": wa2[360:363],  # Maximum number is 21
        "LIST OF GEOGRAPHIC IDENTIFIERS": wa2[364:2799],
        # Variable length list of up to 21 entries; each is 116 bytes long, structured as follows
        # Maximum of 21 entries, each 116 bytes long: 116 x 21 = 2,436
        # "Low House Number": wa2[0:15],  # Display format
        # "High House Number": wa2[16:31],  # Display format
        # "Borough Code": wa2[32],  # Start of B7SC
        # "5-Digit Street Code": wa2[33:37],  # Part of B7SC
        # "DCP-Preferred Local Group Code (LGC)": wa2[38:39],  # End of B7SC
        # "Building Identification Number (BIN)": wa2[40:46],
        # "Side of Street Indicator": wa2[47],  # L - Left, R - Right
        # "Geographic Identifier Entry Type Code": wa2[48],  # N - NAP (Simplex)
        #     G - Complex NAP
        #     X - Constituent Entity of Complex NAP
        #     B - NAUB
        #     F - Frontage
        #     W - Blank Wall
        #     Q - Pseudo Address
        #     T - Tunnel
        #     U - Misc Structure
        #     V - Vanity Address
        #     O - Out-of-Sequence Addr
        #     Blank - Normal
        # "TPAD BIN Status": wa2[49],  # TPAD Request
        # "Street Name (Principal Street Name)": wa2[50:81],  # Based on B7SCin Address List
        # "Filler": wa2[82:115]
    }