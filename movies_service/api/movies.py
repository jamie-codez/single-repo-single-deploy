from fastapi import APIRouter, HTTPException
from models.movie import Movie
from typing import List

fake_movie_db = [
    {
        "name": "Star Wars: Episode IX - The Rise of Skywalker",
        "plot": "The surviving members of the resistance face the First Order once again, and the legendary conflict between the Jedi and the Sith reaches its peak bringing the Skywalker saga to its end.",
        "genres": ["Action", "Adventure", "Fantasy", "Sci-Fi"],
        "casts": ["Carrie Fisher", "Mark Hamill", "Adam Driver", "Daisy Ridley"],
    }
]

movies = APIRouter()

@movies.get(
    "/",
    description="Root of the API",
    response_model=List[Movie],
    status_code=200,
)
def get_movies() -> List[Movie]:
    return fake_movie_db


@movies.post(
    "/",
    description="Create a new movie",
    response_model=dict,
    status_code=201,
)
def create_movie(movie: Movie) -> dict:
    movie = movie.dict()
    fake_movie_db.append(movie)
    return {"id": len(fake_movie_db) - 1}


@movies.put(
    "/{movie_id}",
    description="Update a movie",
    response_model=dict,
    status_code=200,
)
def update_movie(movie_id: int, movie: Movie) -> dict:
    movie = movie.dict()
    if 0 <= movie_id <= len(fake_movie_db):
        fake_movie_db[movie_id] = movie
        return {"message": "Movie has been updated successfully."}
    raise HTTPException(status_code=404, detail="Movie not found")


@movies.delete(
    "/{movie_id}",
    description="Delete a movie",
    response_model=dict,
    status_code=200,
)
def delete_movie(movie_id: int) -> dict:
    movie_length = len(fake_movie_db)
    if 0 <= movie_id <= movie_length:
        del fake_movie_db[movie_id]
        return {"message": "Movie deleted successfully"}
    raise HTTPException(status_code=404, detail="Movie not found")
