from services.geocoding import geocode
from schema.geocoding import GeocodingResponse
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/v1/locations", tags=["locations"])

@router.get("/{query}/geocoding", response_model=GeocodingResponse)
async def get_geocoding(query: str):
    result = await geocode(query)    
    if not result:
        raise HTTPException(status_code=404, detail="Location not found")
    
    return result