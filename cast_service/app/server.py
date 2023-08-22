from fastapi import FastAPI
from api.cast import cast as cast_router

from db.db import metadata,database,engine

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/casts/openapi.json",docs_url="/api/v1/casts/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(cast_router,prefix="/api/v1/cast",tags=["Casts"])