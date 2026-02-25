from pydantic import BaseModel

class GeocodingResponse(BaseModel):
    name: str
    lat: float
    lon: float