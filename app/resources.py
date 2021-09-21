import os

from .geocoder.base_coder import BaseGeocoder
from .geocoder.google_custom_geocoder import GoogleGeocoder
from .geocoder.interface import MultiGeocoder

app_name = os.environ.get('APP_NAME', None)
if app_name is None:
    raise Exception('APP_NAME should be set')

custom_domain = os.environ.get('CUSTOM_DOMAIN', None)


google_geocoder = GoogleGeocoder()
base_coder = BaseGeocoder(app_name, custom_domain)

geocoder = MultiGeocoder([base_coder, google_geocoder])
