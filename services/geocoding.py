import httpx

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"

async def geocode(query: str):
    params = {
        "q": query,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "nomad-api"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(NOMINATIM_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()

    if not data:
        return None

    result = data[0]

    return {
        "name": result["display_name"],
        "lat": float(result["lat"]),
        "lon": float(result["lon"])
    }