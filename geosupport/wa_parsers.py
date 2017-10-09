"""
For parsing geosupport results. See the Character-Only Work Area Layouts section starting on page 566
of the Geosupport User Programming Guide for more information.
"""


def _parseWA1(wa1):
    """
    :param wa1: Processed from all functions
    :return: Dictionary of results
    """
    output = {
        'First Borough Name': wa1[360:369].strip(),
        'House Number - Display Format': wa1[369: 385].strip(),
        'House Number - Sort Format': wa1[385: 396].strip(),
        'B10SC - First Borough and Street Code': wa1[396: 407].strip(),
        'First Street Name Normalized': wa1[407:439].strip(),
        'B10SC - Second Borough and Street Code': wa1[439:449].strip(),
        'Second Street Name Normalized': wa1[450:481].strip(),
        'B10SC - Third Borough and Street Code': wa1[482:492].strip(),
        'Third Street Name Normalized': wa1[493:524].strip(),
        'BOROUGH BLOCK LOT': {'Borough Code': wa1[525:525].strip(),  # BOROUGH BLOCK LOT
                'Tax Block': wa1[526:530].strip(),
                'Tax Lot': wa1[531:534].strip()},
        # 'Filler for Tax Lot Version Number': wa1[535:535].strip(),
        'Low House Number - Display Format': wa1[536:551].strip(),
        'Low House Number - Sort Format': wa1[552:562].strip(),
        'BIN': wa1[563:569].strip(),  # Building Identification Number
        'Street Attribute Indicators': wa1[570:572].strip(),
        'Reason Code 2': wa1[573:573].strip(),
        'Reason Code Qualifier 2': wa1[574:574].strip(),
        'Warning Code 2': wa1[575:576].strip(),
        'GRC 2': wa1[577:578].strip(),  # Geosupport Return Code 2
        'Message 2': wa1[579:658].strip(),
        'Node Number': wa1[659:665].strip(),
        # 'Filler': wa1[666:704].strip(),
        'NIN': wa1[705:710].strip(),  # NAP Identification Number
        'Street Attribute Indicator': wa1[711:711].strip(),
        'Reason Code': wa1[712:712].strip(),
        'Reason Code Qualifier': wa1[713:713].strip(),
        'Warning Code': wa1[714:715].strip(),
        'GRC': wa1[716:717].strip(),  # Geosupport Return Code
        'Message': wa1[718:797].strip(),
        'Number of Street Codes and Street Names in List': wa1[798:799].strip(),
        'List of Street Codes': wa1[800:879].strip(),
        'List of Street Names': wa1[880:1199].strip(),
    }
    return output


def _parseWA2_1B(wa2):
    """
    Parses results of WA2 from function 1B (Street Address)

    "Block Face Information Defined by Address Range Along a Street &
    Property Level Information Defined by Address"

    See page 586 of the Geosupport User Programming Guide for more information.

    :param wa2: Work Area 2 from GeoSupport function 1B results
    :return: Dictionary of results
    """
    output = {
        'Continuous Parity Indicator/Duplicate Address Indicator': wa2[21:21].strip(),
        'Low House Number of Block Face': wa2[22:32].strip(),
        'High House Number of Block Face': wa2[33:43].strip(),
        'DCP Preferred LGC': wa2[44:45].strip(),
        'Number of Cross Streets at Low Address End': wa2[46:46].strip(),
        'List of Cross Streets at Low Address End (Up to 5 B5SCs)': wa2[47:76].strip(),
        'Number of Cross Streets at High Address End': wa2[77:77].strip(),
        'List of Cross Streets at High Address End (Up to 5 B5SCs)': wa2[78:107].strip(),
        'LION KEY': {'Borough Code': wa2[108:108].strip(),
                     'Face Code': wa2[109:112].strip(),
                     'Sequence Number': wa2[113:117].strip(),
                     },
        'Special Address Generated Record Flag': wa2[118:118].strip(),
        'Side of Street Indicator': wa2[119:119].strip(),
        'Segment Length in Feet': wa2[120:124].strip(),
        'XCoord': wa2[125:131].strip(),
        'YCoord': wa2[132:138].strip(),
        'Reserved for Possible Z Coordinate': wa2[139:145].strip(),
        'Community Development Eligibility Indicator': wa2[146:146].strip(),
        'Marble Hill/Rikers Island Alternative Borough Flag': wa2[147:147].strip(),
        'DOT Street Light Contractor Area': wa2[148:148].strip(),
        'COMMUNITY DISTRICT': {'Community District Borough Code': wa2[149:149].strip(),
                               'Community District Number': wa2[150:151].strip()},
        'Zip Code': wa2[152:156].strip(),
        'Election District': wa2[157:159].strip(),
        'Assembly District': wa2[160:161].strip(),
        'Split Election District Flag': wa2[162:162].strip(),
        'Congressional District': wa2[163:164].strip(),
        'State Senatorial District': wa2[165:166].strip(),
        'Civil Court District': wa2[167:168].strip(),
        'City Council District': wa2[169:170].strip(),
        'Health Center District': wa2[171:172].strip(),
        'Health Area': wa2[173:176].strip(),
        'Sanitation District': wa2[177:179].strip(),
        'Sanitation Collection Scheduling Section and Subsection': wa2[180:181].strip(),
        'Sanitation Regular Collection Schedule': wa2[182:186].strip(),
        'Sanitation Recycling Collection Schedule': wa2[187:189].strip(),
        'Police Patrol Borough Command': wa2[190:190].strip(),
        'Police Precinct': wa2[191:194].strip(),
        'Fire Division': wa2[195:195].strip(),
        'Fire Battalion': wa2[196:197].strip(),
        'Fire Company Type': wa2[198:198].strip(),
        'Fire Company Number': wa2[199:201].strip(),
        # 'Filler': wa2[202:202].strip(),
        
        'Community School District': wa2[203:204].strip(),
        'Atomic Polygon': wa2[205:207].strip(),
        'Police Patrol Borough': wa2[208:209].strip(),
        'Feature Type Code': wa2[210:210].strip(),
        'Segment Type Code': wa2[211:211].strip(),
        'Alley or Cross Street List Flag': wa2[212:212].strip(),
        'Coincidence Segment Count': wa2[213:213].strip(),
        # 'Filler': wa2[214:216].strip(),
        '1990 Census Tract': wa2[217:222].strip(),
        '2010 Census Tract': wa2[223:228].strip(),
        '2010 Census Block': wa2[229:232].strip(),
        '2010 Census Block Suffix': wa2[233:233].strip(),
        '2000 Census Tract': wa2[234:239].strip(),
        '2000 Census Block': wa2[240:243].strip(),
        '2000 Census Block Suffix': wa2[244:244].strip(),
        'Neighborhood Tabulation Area (NTA)': wa2[245:248].strip(),
        'DSNY Snow Priority Code': wa2[249].strip(),
        'DSNY Organic Recycling Schedule': wa2[250:254].strip(),
        'DSNY Reserved': wa2[255:259].strip(),
        'Hurricane Evacuation Zone (HEZ)': wa2[260:261].strip(),
        # 'Filler': wa2[262:272].strip(),
        'Underlying Address Number for NAPs': wa2[273:283].strip(),
        'Underlying B7SC': wa2[284:291].strip(),
        'Segment Identifier': wa2[292:298].strip(),
        'Curve Flag': wa2[299:299].strip(),

        "List of 4 LGC's": wa2[299:299].strip(),
        'BOE LGC Pointer': wa2[308:308].strip(),
        'Segment Azimuth': wa2[309:311].strip(),
        'Segment Orientation': wa2[312:312].strip(),




        'Spatial Coordinates of Segment': {'X Coordinate, Low Address End': wa2[313:319].strip(),
                                           'Y Coordinate, Low Address End': wa2[320:326].strip(),
                                           'Z Coordinate, Low Address End': wa2[327:333].strip(),
                                           'X Coordinate, High Address End': wa2[334:340].strip(),
                                           'Y Coordinate, High Address End': wa2[341:347].strip(),
                                           'Z Coordinate, High Address End': wa2[348:351].strip(),
                                           },
        'Roadway Type': wa2[444:446].strip(),
        'Bike Lane': wa2[486].strip(),
        'NTA Name': wa2[553: 628].strip(),
        'USPS Preferred City Name': wa2[628:653].strip(),
        'Latitude': wa2[653:662].strip(),
        'Longitude': wa2[662:672].strip(),
        'Borough Block Lot (BBL)': {'Borough code': wa2[1533].strip(),
                                    'Tax Block': wa2[1534:1539].strip(),
                                    'Tax Lot': wa2[1539:1543].strip(),
                                    },
        'Building Identification Number (BIN) of Input Address or NAP': wa2[1581:1588].strip(),
        'X-Y Coordinates of Lot Centroid': wa2[1699:1713].strip(),

    }
    return output


def _parseWA2_1A_BL_BN(wa2):
    """
    Parses results of WA2 from function 1A, BL, BN.
    Property Level Information Defined by Address, BBL or BIN.
    See page 579 of Geosupport User Programming Guide for more info.

    :param wa1: Work Area 1 from GeoSupport function BL results
    :param wa2: Work Area 2 from GeoSupport function BL results
    :return: Dictionary of results
    """

    output = {
        'Continuous Parity Indicator /Duplicate Address Indicator': wa2[21:21].strip(),
        'Low House Number of Defining Address Range': wa2[22:32].strip(),
        'Borough Block Lot (BBL)': {'Borough code': wa2[33:33].strip(),
                                    'Tax Block': wa2[34:38].strip(),
                                    'Tax Lot': wa2[36:42].strip(),
                                    },

        # 'Filler for Tax Lot Version Number': wa2[43:43].strip(),
        'RPAD Self-Check Code (SCC) for BBL': wa2[44:44].strip(),
        # 'Filler': wa2[45:45].strip(),
        'RPAD Building Classification Code': wa2[46:47].strip(),
        'Corner Code': wa2[48:49].strip(),
        'Number of Existing Structures on Lot': wa2[50:53].strip(),
        'Number of Street Frontages of Lot': wa2[54:55].strip(),
        'Interior Lot Flag': wa2[56:56].strip(),
        'Vacant Lot Flag': wa2[57:57].strip(),
        'Irregularly-Shaped Lot Flag': wa2[58:58].strip(),
        'Marble Hill/Rikers Island Alternate Borough Flag': wa2[59:59].strip(),
        'List of Geographic Identifiers (LGI) Overflow Flag': wa2[60:60].strip(),
        'STROLLING KEY': {'Borough': wa2[61:61].strip(),
                          "5-Digit Street Code of 'On' Street": wa2[62:66].strip(),
                          'Side of Street Indicator': wa2[67:67].strip(),
                          "High House Number - Sort Format": wa2[68:78].strip(),
                          # 'Filler': wa2[79:79].strip(),
                          },
        'Reserved for Internal Use': wa2[80:80].strip(),
        'Building Identification Number (BIN) of Input Address or NAP': wa2[81:87].strip(),
        'Condominium Flag': wa2[88:88].strip(),
        # 'Filler': wa2[89:89].strip(),
        'DOF Condominium Identification Number': wa2[90:93].strip(),
        'Condominium Unit ID Number': wa2[94:100].strip(),
        'Condominium Billing BBL': wa2[101:110].strip(),
        # 'Filler - Tax Lot Version No. for Billing BBL': wa2[111:11].strip(),
        'Self-Check Code (SCC) of Billing BBL': wa2[112:112].strip(),
        "LOW BBL OF THIS BUILDING'S CONDOMINIUM UNITS": {'Borough Code': wa2[113:113].strip(),
                                                         'Tax Block': wa2[114:118].strip(),
                                                         'Tax Lot': wa2[119:122].strip()
                                                         },
        # 'Filler for Tax Lot Version No. of Low BBL': wa2[123:123].strip(),
        "HIGH BBL OF THIS BUILDING'S CONDOMINIUM UNITS": {'Borough Code': wa2[124:124].strip(),
                                                          'Tax Block': wa2[125:129].strip(),
                                                          'Tax Lot': wa2[130:133].strip(),
                                                          },
        # "Filler for Tax Lot Version No. of High BBL": wa2[134:134].strip(),
        # "Filler": wa2[135:149].strip(),
        "Cooperative ID Number": wa2[150:153].strip(),
        "SBVP (SANBORN MAP IDENTIFIER)": {"Sanborn Borough Code": wa2[154:154].strip(),
                                          "Volume Number": wa2[155:156].strip(),
                                          "Volume Number Suffix": wa2[157:157].strip(),
                                          "Page Number": wa2[158:160].strip(),
                                          "Page Number Suffix": wa2[161:161].strip()
                                          },
        "DCP Commercial Study Area": wa2[162:166].strip(),
        "Tax Map Number Section & Volume": wa2[167:171].strip(),
        "Reserved for Tax Map Page Number": wa2[172:175].strip(),
        # "Filler": wa2[176:178].strip(),
        "Latitude": wa2[179:187].strip(),
        "Longitude": wa2[188:198].strip(),
        "X-Y Coordinates of Tax Lot Centroid (Internal to Lot)": wa2[199:212].strip(),
        "Business Improvement District (BID)": wa2[213:218].strip(),
        "TPAD BIN Status (for DM job)": wa2[219:219].strip(),
        "TPAD New BIN": wa2[220:226].strip(),
        "TPAD New BIN Status": wa2[227:227].strip(),
        "TPAD Conflict Flag": wa2[228:228].strip(),
        # "Filler": wa2[229:237].strip(),
        "List of 4 LGCs": wa2[238:245].strip(),
        "Number of Entries in List of Geographic Identifiers": wa2[246:249].strip(),
        "LIST OF GEOGRAPHIC IDENTIFIERS": wa2[250:1362].strip(),
        # {
        # "Low House Number":
        # "High House Number":
        # "Borough Code":
        # "5-Digit Street Code":
        # "DCP-Preferred Local Group Code (LGC)":
        # "Building Identification Number (BIN)":
        # "Side of Street Indicator":
        # "Geographic Identifier Entry Type Code":
        # "TPAD BIN Status":
        # "Filler":
        # }

    }
    return output
