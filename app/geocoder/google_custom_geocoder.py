import logging
import json
import time
from collections.abc import Iterable
from typing import Any, List, Optional

import requests

from .dto import GeocodeResponse
from .interface import IGeocoder


def flatten(l: Iterable) -> List[Any]:
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


url = "https://www.google.com/search"


def remove_begining(res: str):
    # removing )]}'
    return res[4:]


def is_likely_long_lat(item: Any):
    if isinstance(item, float):
        if -90 < item < 90:
            return True
    return False


def find_likely_following_coords(entry: List[Any]) -> Optional[GeocodeResponse]:
    lat = None
    long = None
    for item in entry:
        if is_likely_long_lat(item):
            if lat is None:
                lat = item
            else:
                long = item
                break
        else:
            lat = None
            long = None
    if lat is not None and long is not None:
        return GeocodeResponse(latitude=lat, longitude=long)
    else:
        return None


MAX_RETRIES = 5


class GoogleGeocoder(IGeocoder):
    """
    This class imitates a google map search and is not based on the API

    It is likely to break in the future, use it with caution
    """

    def __init__(self) -> None:
        self.logger = logging.getLogger()

    def geocode(self, q: str):
        query = {
            "q": q,
            "tbm": "map",
        }
        retries = 0
        r = requests.get(url=url, params=query)
        while r.status_code != 200 and retries < MAX_RETRIES:
            r = requests.get(url=url, params=query)
            retries += 1
            # handling 429
            self.logger.warn(
                f'[status: {r.status_code}]unable to find result for {q}')
            time.sleep(1)

        if r.status_code:
            s = remove_begining(r.text)
            res = flatten(json.loads(s))
            return find_likely_following_coords(res)
        else:
            return None
