from fastapi import APIRouter, HTTPException
from models.movie import MovieOut, MovieIn, MovieUpdate
from services.movie_service import (
    add_movie,
    get_all_movies,
    get_movie_by_id,
    update_movie_by_id,
    delete_movie_by_id,
)
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
    response_model=List[MovieOut],
    status_code=200,
)
async def get_movies() -> List[MovieOut]:
    movies = await get_all_movies()
    if movies:
        return movies
    raise HTTPException(status_code=404, detail="No movies found")


@movies.post(
    "/",
    description="Create a new movie",
    response_model=dict,
    status_code=201,
)
async def create_movie(movie: MovieIn) -> dict:
    new_movie = await add_movie(movie)
    if new_movie:
        return {"message": "Movie created successfully."}
    raise HTTPException(status_code=500, detail="Internal Server Error")


@movies.put(
    "/{movie_id}",
    description="Update a movie",
    response_model=dict,
    status_code=200,
)
async def update_movie(movie_id: int, movie: MovieUpdate) -> dict:
    updated_movie = await update_movie_by_id(movie_id,movie)
    if updated_movie:
        return {"message": "Movie updated successfully."}
    raise HTTPException(status_code=404, detail="Movie not found")


@movies.delete(
    "/{movie_id}",
    description="Delete a movie",
    response_model=dict,
    status_code=200,
)
async def delete_movie(movie_id: int) -> dict:
    deleted_movie = await delete_movie_by_id(movie_id)
    if deleted_movie:
        return {"message": "Movie deleted successfully."}
    raise HTTPException(status_code=404, detail="Movie not found")