from fastapi import HTTPException
from models.movie import MovieIn, MovieOut, MovieUpdate
from db.db import movies, database
from event.event import is_cast_present


async def add_movie(payload: MovieIn):
    try:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id=cast_id):
                raise HTTPException(status_code=404, detail=f"Cast with id {cast_id} not found")
        query = movies.insert().values(**payload.dict())
        return await database.execute(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def get_all_movies() -> dict:
    try:
        query = movies.select()
        return await database.fetch_all(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def get_movie_by_id(id: int) -> dict:
    try:
        query = movies.select(movies.c.id == id)
        return await database.fetch_one(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def update_movie_by_id(id: int, payload: MovieUpdate) -> dict:
    try:
        movie = movies.select().where(movies.c.id==id)
        if not movie:
            raise HTTPException(status_code=404,detail="Movie not found")
        update_data = payload.dict(exclude_unset=True)
        if 'cast_id' in update_data:
            for cast_id in payload.casts_id:
                if not is_cast_present(cast_id=cast_id):
                    raise HTTPException(status_code=404,detail=f"Cat with {cast_id} not found")
        movie_in_db = MovieIn(**movie)
        updated_movie = movie_in_db.copy(update=update_data)
        query = movies.update().where(movies.c.id == id).values(**updated_movie.dict())
        return await database.execute(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


async def delete_movie_by_id(id: int) -> dict:
    try:
        query = movies.delete().where(movies.c.id == id)
        return await database.execute(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
