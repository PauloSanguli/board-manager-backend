from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import File, UploadFile, Depends

from .....domain.entities.veichle import VeichleProps

from ...repositories.veichle_repository import VeichleRepository



router_post = APIRouter(prefix="/board-manager", tags=["admin"])

@router_post.post("/veichle")
async def create_veichle(Veichle: VeichleProps):
    resullt = VeichleRepository.create(Veichle)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder({
            "msg": "veichle inserted"
        })
    )
