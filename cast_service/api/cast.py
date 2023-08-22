from fastapi import APIRouter, HTTPException, status
from typing import List
from models.models import CastIn, CastOut, CastUpdate
from services.cast_service import add_cast, get_cast

cast = APIRouter()


@cast.post("/", response_model=dict, description="Creates casts in db", status_code=200)
async def create_cast(payload: CastIn) -> dict:
    cast_id = await add_cast(payload=payload)
    return cast_id


@cast.get(
    "/{id}",
    response_model=CastOut,
    description="Returns cast with parsed id",
    status_code=200,
)
async def get_cast(id: int) -> CastOut:
    cast = await get_cast(id=id)
    if not cast:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Cast with {id} not found"
        )
    return cast
