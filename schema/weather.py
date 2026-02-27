from pydantic import BaseModel

class WeatherResponse(BaseModel):
    temp: str
