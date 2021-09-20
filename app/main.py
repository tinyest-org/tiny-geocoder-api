import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .dto import GeocodeResponse
from .resources import geocoder

app = FastAPI()

origins = os.environ.get('origins', '').split(',')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/geocode', response_model=GeocodeResponse)
def geocode_path(q: str):
    res = geocoder(q)
    return GeocodeResponse(
        latitude=res.latitude,
        longitude=res.longitude,
    )

def reverse_geocode():
    # not implem for now
    pass
