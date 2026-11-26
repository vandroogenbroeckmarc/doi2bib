"""Conference dates and locations for OpenReview citations."""
from typing import Dict

ICML_METADATA_BY_YEAR: Dict[int, Dict[str, str]] = {
    # Historical conference locations follow the official ICML archive and
    # conference pages; PMLR's own BibTeX supplies each paper's month.
    1980: {"address": "city-pittsburgh"},
    1983: {"address": "city-monticello"},
    1985: {"address": "city-skytop"},
    1987: {"address": "city-irvine"},
    1988: {"address": "city-annarbor"},
    1989: {"address": "city-ithaca"},
    1990: {"address": "city-austin"},
    1991: {"address": "city-evanston"},
    1992: {"address": "city-aberdeen"},
    1993: {"address": "city-amherst"},
    1994: {"address": "city-newbrunswick"},
    1995: {"address": "city-laketahoe"},
    1996: {"address": "city-bari"},
    1997: {"address": "city-nashville"},
    1998: {"address": "city-madison"},
    1999: {"address": "city-bled"},
    2000: {"address": "city-stanford"},
    2001: {"address": "city-williamstown"},
    2002: {"address": "city-sydney"},
    2003: {"address": "city-washington"},
    2004: {"address": "city-banff"},
    2005: {"address": "city-bonn"},
    2006: {"address": "city-pittsburgh"},
    2007: {"address": "city-corvallis"},
    2008: {"address": "city-helsinki"},
    2009: {"address": "city-montreal"},
    2010: {"address": "city-haifa"},
    2011: {"address": "city-bellevue"},
    2012: {"address": "city-edinburgh"},
    2013: {"month": "jun", "address": "city-atlanta"},
    2014: {"month": "jun", "address": "city-beijing"},
    2015: {"month": "jul", "address": "city-lille"},
    2016: {"month": "jun", "address": "city-newyork"},
    2017: {"month": "aug", "address": "city-sydney"},
    2018: {"month": "jul", "address": "city-stockholm"},
    2019: {"month": "jun", "address": "city-longbeach"},
    2020: {"month": "jul", "address": "city-virtual"},
    2021: {"month": "jul", "address": "city-virtual"},
    2022: {"month": "jul", "address": "city-baltimore"},
    2023: {"month": "jul", "address": "city-honolulu"},
    2024: {"month": "jul", "address": "city-vienna"},
    2025: {"month": "jul", "address": "city-vancouver"},
    2026: {"month": "jul", "address": "city-seoul"},
}


ICLR_METADATA_BY_YEAR: Dict[int, Dict[str, str]] = {
    2013: {"month": "may", "address": "Scottsdale, Arizona, USA"},  # https://iclr.cc/archive/2013/
    2014: {"month": "apr", "address": "Banff, Alberta, Canada"},  # https://iclr.cc/archive/2014/old-site/
    2015: {"month": "may", "address": "city-sandiego"},  # https://iclr.cc/archive/www/2015.html
    2016: {"month": "may", "address": "San Juan, Puerto Rico"},  # https://iclr.cc/archive/www/2016.html
    2017: {"month": "apr", "address": "city-toulon"},  # https://iclr.cc/archive/www/doku.php?id=iclr2017:main.html
    2018: {"month": "apr", "address": "city-vancouver"},  # https://iclr.cc/Conferences/2018
    2019: {"month": "may", "address": "city-neworleans"},  # https://iclr.cc/Conferences/2019
    2020: {"month": "apr", "address": "Virtual"},  # https://iclr.cc/Conferences/2020/virtual
    2021: {"month": "may", "address": "Virtual"},  # https://iclr.cc/Conferences/2021/CallForPapers
    2022: {"month": "apr", "address": "Virtual"},  # https://iclr.cc/Conferences/2022/Dates
    2023: {"month": "may", "address": "Kigali, Rwanda"},  # https://iclr.cc/Conferences/2023
    2024: {"month": "may", "address": "city-vienna"},  # https://iclr.cc/Conferences/2024
    2025: {"month": "apr", "address": "city-singapore"},  # https://iclr.cc/Conferences/2025
    2026: {"month": "apr", "address": "city-rio"},  # https://iclr.cc/Conferences/2026
}
