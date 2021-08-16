from fastapi import FastAPI

from .dto import GeocodeResponse
from .resources import geocoder

app = FastAPI()


@app.get('/geocode', response_class=GeocodeResponse)
def geocode_path(q: str):
    res = geocoder(q)
    return GeocodeResponse(
        latitude=res.latitude,
        longitude=res.longitude,
    )

def reverse_geocode():
    # not implem for now
    pass
