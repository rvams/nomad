import httpx
from geopy.geocoders import ArcGIS

# Initialize geolocator once
geolocator = ArcGIS()

async def get_weather(query: str):
    # 1. Use geopy to get coordinates
    location = geolocator.geocode(query)
    
    if not location:
        return None

    # 2. Prepare Open-Meteo request
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "current": "temperature_2m",
        "timezone": "auto"
    }

    # 3. Fetch data asynchronously
    async with httpx.AsyncClient() as client:
        response = await client.get(WEATHER_URL, params=params)
        response.raise_for_status()
        data = response.json()

    # 4. Return clean dictionary
    return {
        "temp": f"{data['current']['temperature_2m']}°C"
    }

