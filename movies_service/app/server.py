from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

fake_movie_db = [
    {
        "name": "Star Wars: Episode IX - The Rise of Skywalker",
        "plot": "The surviving members of the resistance face the First Order once again, and the legendary conflict between the Jedi and the Sith reaches its peak bringing the Skywalker saga to its end.",
        "genres": ["Action", "Adventure", "Fantasy", "Sci-Fi"],
        "casts": ["Carrie Fisher", "Mark Hamill", "Adam Driver", "Daisy Ridley"],
    }
]


class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]


@app.get(
    "/",
    description="Root of the API",
    tags=["Root"],
    response_model=List[Movie],
    status_code=200,
)
def read_root() -> List[Movie]:
    return fake_movie_db


@app.post(
    "/",
    description="Create a new movie",
    tags=["Create"],
    response_model=dict,
    status_code=201,
)
def create_movie(movie: Movie) -> dict:
    movie = movie.dict()
    fake_movie_db.append(movie)
    return {"id": len(fake_movie_db) - 1}


@app.put(
    "/{movie_id}",
    description="Update a movie",
    tags=["Update"],
    response_model=dict,
    status_code=200,
)
def update_movie(movie_id: int, movie: Movie)->dict:
    movie = movie.dict()
    if 0 <= movie_id<=len(fake_movie_db):
        fake_movie_db[movie_id] = movie
        return {"message": "Movie has been updated successfully."}
    raise HTTPException(status_code=404,detail="Movie not found")
