from fastapi import FastAPI, HTTPException
from api.movies import movies as movies_router

app = FastAPI()
app.include_router(movies_router, prefix="/movies", tags=["Movies"])


