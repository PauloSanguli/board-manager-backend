from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import File

from ...repositories.veichle_repository import VeichleRepository

from src.domain.entities.veichle import FindBoard




veichle_get = APIRouter(prefix="/board-manager", tags=["veichle"])

@veichle_get.get("/veichle/{board}/")
async def get_veichle_by_board(board: str):
    
    __veichle, __owner = VeichleRepository.get_by_board(board)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "owner": __owner,
            "veichle": __veichle
        })
    )

@veichle_get.get("/infractions/")
async def get_infractions(board_car: str):
    datas = VeichleRepository.get_infractions(board_car)
    
    return JSONResponse(
        content=jsonable_encoder(datas),
        status_code=status.HTTP_200_OK
    )
