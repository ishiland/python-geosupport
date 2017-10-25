
def parse_AP(wa2):
    # Work Area 2 (COW) - Function AP
    regular =  {
        "Internal Use": wa2[0:20],
        "Low House Number of Defining Address Range": wa2[22:32],  # Sort Format
        "BOROUGH BLOCK LOT (BBL)": { # Billing BBL if Condo
            "Borough Code": wa2[33],
            "Tax Block": wa2[34:38],
            "Tax Lot": wa2[39:42]},
        # "Filler": wa2[43:49],
        "Number of Existing Structures on Lot": wa2[50:53],
        # "Filler": wa2[54:79],
        "Reserved for Internal Use": wa2[80],
        "Building Identification Number (BIN) of Input Address or NAP": wa2[81:87],
        "Condominium Flag": wa2[88],  # If condo, = 'C'
        # "Filler": wa2[89],
        "DOF Condominium Identification Number": wa2[90:93],
        # "Filler": wa2[94:100],
        "Condominium Billing BBL": wa2[101:110],
        # "Filler - Tax Lot Version No. for Billing BBL": wa2[111],  # Not Implemented
        # "Filler": wa2[112],
        "LOW BBL OF THIS BUILDING'S CONDOMINIUM UNITS": {
            "Borough Code": wa2[113],  # Condo
            "Tax Block": wa2[114:118],
            "Tax Lot": wa2[119:122]},
        # "Filler for Tax Lot Version No. of Low BBL": wa2[123],  # Not Implemented
        "HIGH BBL OF THIS BUILDING'S CONDOMINIUM UNITS": {
            "Borough Code": wa2[124],
            "Tax Block": wa2[125:129],
            "Tax Lot": wa2[130:133]},
        # "Filler for Tax Lot Version No. of High BBL": wa2[134],  # Not Implemented
        # "Filler": wa2[135:149],
        "Cooperative ID Number": wa2[150:153],
        # "Filler": wa2[154:175],
        # "Filler": wa2[176:178],
        "Latitude": wa2[179:187],
        "Longitude": wa2[188:198],
        "X-Y Coordinates of Address Point": wa2[199:212],
        # "Filler": wa2[213:228],
        "Address Point ID": wa2[229:237],
        "List of 4 LGCs - Internal Use": wa2[238:245],  # Internal Use
        "LIST OF GEOGRAPHIC IDENTIFIERS": wa2[250:1362],
        # For Function AP - there is only 1 entry. (Potential Max of 21) 21x53 = 1,113
        # "Low House Number": wa2[0:15],  # Display format
        # "High House Number": wa2[16:31],  # Display format
        # "Borough Code": wa2[32],  # Start of B7SC
        # "5-Digit Street Code": wa2[33:37],  # Part of B7SC
        # "DCP-Preferred Local Group Code (LGC)": wa2[38:39],  # End of B7SC
        # "Building Identification Number (BIN)": wa2[40:46],
        # "Side of Street Indicator": wa2[47],  # L - Left, R - Right
        # "Geographic Identifier Entry Type Code": wa2[48],  # V - Vanity Address Blank - Normal
        # "Filler": wa2[49:52]
    }
    # Include extended results
    regular = regular.copy()
    regular.update(parse_AP_ext(wa2))
    return regular

def parse_AP_ext(wa2):
    # Work Area 2 (COW) - Function AP Extended
    return{
        # "Same as Regular Work Area 2 - Function AP": wa2[0:245],
        # "Reason Code": wa2[246],  # Same as Work Area 1
        # "Reason Code Qualifier": wa2[247],  # Same as Work Area 1
        # "Warning Code": wa2[248:249],  # Not used
        # "Return Code (GRC)": wa2[250:251],  # Same as Work Area 1
        # "Filler": wa2[252:359],
        "Number of Entries in List of Geographic Identifiers": wa2[360:363],  # Fn APX # is '0001' Always '0001'
        "LIST OF GEOGRAPHIC IDENTIFIERS:": wa2[364:2799],
        # For Function APX, the list contains one entry Variable length list of up to 21 entries; there is only 1 entry.
        # each is 116 bytes long, structured as follows
        # For Function APX - 21 x 116 = 2,436
        # "Low House Number": wa2[0:15],  # Display format
        # "High House Number": wa2[16:31],  # Display format
        # "Borough Code": wa2[32],  # Start of B7SC
        # "5-Digit Street Code": wa2[33:37],  # Part of B7SC
        # "DCP-Preferred Local Group Code (LGC)": wa2[38:39],  # End of B7SC
        # "Building Identification Number (BIN)": wa2[40:46],
        # "Side of Street Indicator": wa2[47],  # L - Left, R - Right
        # "Geographic Identifier Entry Type Code": wa2[48],  # V - Vanity Address Blank - Normal
        # "Filler": wa2[49],
        # "Street Name (Principal Street Name)": wa2[50:81],  # Based on B7SC in Address List
        # "Filler": wa2[82:115]
    }