from app.dto import GeocodeResponse
from collections.abc import Iterable
from typing import Tuple, List, Any
import json
import requests


def flatten(l):
    for el in l:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


url = "https://www.google.com/search"


def remove_begining(res: str):
    # removing )]}'
    return res[4:]


def find_likely_following_coords(entry: List[Any]):
    lat = None
    long = None
    for item in entry:
        if isinstance(item, float):
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

class GoogleGeocoder:
    """
    This class imitates a google map search and is not based on the API
    It is likely to break in the future, use it with caution
    """
    def __init__(self) -> None:
        pass

    def geocode(self, q: str) -> Tuple[str, str]:
        query = {
            "q": q,
            "tbm": "map",
        }

        r = requests.get(url=url, params=query)

        if r.status_code == 200:
            print(r.status_code)
            s = remove_begining(r.text)
            res = flatten(json.loads(s))
            return find_likely_following_coords(res)

        # return lat, long
