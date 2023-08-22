from fastapi import FastAPI, HTTPException
from api.movies import movies as movies_router
from database.db import metadata, engine, database

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(movies_router, prefix="/api/v1/movies", tags=["Movies"])
