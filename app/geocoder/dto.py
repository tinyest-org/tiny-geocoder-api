from pydantic import BaseModel


class GeocodeResponse(BaseModel):
    latitude: float
    longitude: float


class ReverseGeocodeResponse(BaseModel):
    pass