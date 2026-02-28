import httpx
from geopy.geocoders import ArcGIS

RADIO_BROWSER_URL = "https://all.api.radio-browser.info/json"

geolocator = ArcGIS()

async def get_radio_stations(query: str, limit: int = 10):
    location = geolocator.geocode(query)

    if not location:
        return None

    params = {
        "geo_lat": location.latitude,
        "geo_long": location.longitude,
        "geo_distance": 500000,
        "hidebroken": "true",
        "order": "clickcount",
        "reverse": "true",
        "limit": limit
    }

    headers = {
        "User-Agent": "nomad-api"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{RADIO_BROWSER_URL}/stations/search",
            params=params,
            headers=headers
        )
        response.raise_for_status()
        data = response.json()

    if not data:
        return None

    stations = []
    for station in data:
        stations.append({
            "name": station["name"],
            "stream_url": station["url_resolved"],
            "homepage": station["homepage"],
            "favicon": station["favicon"],
            "tags": station["tags"],
            "language": station["language"],
            "bitrate": station["bitrate"],
            "codec": station["codec"],
        })

    return stations