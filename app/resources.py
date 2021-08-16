import os
import geopy
import functools
from typing import Optional


def get_geocoder(app_name: str,  custom_domain: Optional[str] = None):
    if custom_domain is None:
        geocoder = geopy.Nominatim(user_agent=app_name)
    else:
        geocoder = geopy.Nominatim(user_agent=app_name, domain=custom_domain)
    geocode = functools.partial(geocoder.geocode, language="en")
    return geocode

app_name = os.environ.get('APP_NAME', None)
if app_name is None:
        raise Exception('APP_NAME should be set')

custom_domain = os.environ.get('CUSTOM_DOMAIN', None)

geocoder = get_geocoder(app_name, custom_domain)