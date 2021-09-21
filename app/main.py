import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from .geocoder.dto import GeocodeResponse
from .resources import geocoder

app = FastAPI()

origins = os.environ.get('origins', '').split(',')

# very simple cache for now
cache = {}


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/geocode', response_model=GeocodeResponse)
def geocode_path(q: str):
    if q in cache:
        return cache[q]
    res = geocoder.geocode(q)
    if res is not None:
        resp = GeocodeResponse(
            latitude=res.latitude,
            longitude=res.longitude,
        )
        cache[q] = resp
        return resp        
    else:
        return JSONResponse({"error": "not found"}, status_code=404)


def reverse_geocode():
    # not implem for now
    pass
