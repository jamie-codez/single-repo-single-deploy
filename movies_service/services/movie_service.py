from fastapi import HTTPException
from models.movie import MovieIn, MovieOut, MovieUpdate
from database.db import movies, database


async def add_movie(payload: MovieIn):
    try:
        query = movies.insert().values(**payload.dict())
        return await database.execute(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        await database.disconnect()


async def get_all_movies() -> dict:
    try:
        query = movies.select()
        return await database.fetch_all(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        await database.disconnect()


async def get_movie_by_id(id: int) -> dict:
    try:
        query = movies.select(movies.c.id == id)
        return await database.fetch_one(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        await database.disconnect()


async def update_movie_by_id(id: int, payload: MovieUpdate) -> dict:
    try:
        query = movies.update().where(movies.c.id == id).values(**payload.dict())
        return await database.execute(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        await database.disconnect()


async def delete_movie_by_id(id: int) -> dict:
    try:
        query = movies.delete().where(movies.c.id == id)
        return await database.execute(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    finally:
        await database.disconnect()
