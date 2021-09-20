import os
from typing import Optional

from .base_coder import BaseGeocoder
from .dto import GeocodeResponse
from .google_custom_geocoder import GoogleGeocoder


class MultiGeocoder:
    def __init__(self, coders) -> None:
        self.coders = coders

    def geocode(self, q: str) -> Optional[GeocodeResponse]:
        resp = None
        for coder in self.coders:
            print('coder', coder)
            try:
                resp = coder.geocode(q)
                if resp is not None:
                    break
            except Exception as e:
                print(f'Failed to get res with {coder}')
        return resp


app_name = os.environ.get('APP_NAME', None)
if app_name is None:
    raise Exception('APP_NAME should be set')

custom_domain = os.environ.get('CUSTOM_DOMAIN', None)


google_geocoder = GoogleGeocoder()
base_coder = BaseGeocoder(app_name, custom_domain)

geocoder = MultiGeocoder([base_coder, google_geocoder])
