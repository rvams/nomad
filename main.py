from fastapi import FastAPI
from routers.location import router

app = FastAPI(title="Nomad API")
app.include_router(router)


@app.get("/health")
async def root():
    return {"Status": "Running.. ⚡ 200 OK"}

