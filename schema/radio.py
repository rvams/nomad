from pydantic import BaseModel

class RadioResponse(BaseModel):
    name: str
    stream_url: str
    homepage: str
    favicon: str
    tags: str
    language: str
    bitrate: int
    codec: str