from services.geocoding import geocode
from schema.geocoding import GeocodingResponse
from services.weather import get_weather
from schema.weather import WeatherResponse
from services.radio import get_radio_stations
from schema.radio import RadioResponse
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/locations", tags=["locations"])

@router.get("/{query}/geocoding", response_model=GeocodingResponse)
async def get_geocoding(query: str):
    result = await geocode(query)    
    if not result:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return result

@router.get("/{query}/weather", response_model=WeatherResponse)
async def get_weather_api(query:str):
    result = await get_weather(query)
    if not result:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return result

@router.get("/{query}/radio", response_model=list[RadioResponse])
async def radio_list(query:str):
    result = await get_radio_stations(query)
    if not result:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return result
