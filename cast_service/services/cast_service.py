from models.models import CastIn,CastOut,CastUpdate
from db.db import casts,database
from fastapi import HTTPException,status

async def add_cast(payload:CastIn)->dict:
    try:
        query = casts.insert().values(**payload.dict())
        return await database.execute(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Internal server error")
    

async def get_cast(id:int)->dict:
    try:
        query = casts.select(casts.c.id==id)
        return await database.fetch_one(query=query)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Internal server error")