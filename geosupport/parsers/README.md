

| Function Code |  python-geosupport method |
|---------------|-----------------------------|
| 1E Extended   |  not yet supported          |
| 1A            |  not yet supported          |
| BL            |  `bbl`                      |
| BN            |  `bin`                      |
| 1B            |  `address` | `place`        |
| AP Extended   |  `address_point`            |
| 2W            |  `intersection`             |
| 3 Extended    |  `street_segment`           |
| 3C Extended   |  `blockface`                |
| 3S            |  `street_stretch`           |



All geocoding functions return the items in `all_wa1.py`. Additionally, each function returns the items in its associated filename.

For more information on NYC Planning Geosupport COW's, see *APPENDIX 13: CHARACTER-ONLY WORK AREA LAYOUTS (COW)*:
https://nycplanning.github.io/Geosupport-UPG/appendices/appendix13/. The documentation from this url was parsed using [bs4](https://www.crummy.com/software/BeautifulSoup/) to create all `python-geosupport` dictionaries w/comments.


