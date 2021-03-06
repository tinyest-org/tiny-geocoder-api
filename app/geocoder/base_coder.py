import functools
from typing import Optional

import geopy

from .dto import GeocodeResponse
from .interface import IGeocoder


class BaseGeocoder(IGeocoder):
    """Based on geopy and Neomatim"""
    def __init__(self, app_name: str, custom_domain: Optional[str]) -> None:
        if custom_domain is None:
            geocoder = geopy.Nominatim(user_agent=app_name)
        else:
            geocoder = geopy.Nominatim(
                user_agent=app_name, domain=custom_domain
            )
        self.geocoder = functools.partial(geocoder.geocode, language="en")

    def geocode(self, q: str) -> Optional[GeocodeResponse]:
        res = self.geocoder(q)
        if res is not None:
            resp = GeocodeResponse(
                latitude=res.latitude,
                longitude=res.longitude,
            )
            return resp
        return None
