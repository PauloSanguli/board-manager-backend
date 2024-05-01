from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import File, UploadFile, Depends

from .....domain.entities.veichle import VeichleProps

from ...repositories.veichle_repository import VeichleRepository

from src.files.__path__ import PATH

from .....domain.entities.infractions import InfractionsProps

from typing import Annotated

from ...middleware.dependencie_admin import JWTTokenExceptionHandler

router_post = APIRouter(prefix="/board-manager", tags=["veichle"])


@router_post.post("/infraction/")
def regist_infraction(account_logged: Annotated[
    dict, Depends(JWTTokenExceptionHandler.get_user_logged)],
    Object: InfractionsProps):
    rs = VeichleRepository.\
        regist_infraction_veichle(Object)
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "infraction registed"
        }),
        status_code=status.HTTP_201_CREATED
    )

@router_post.post("/veichle")
async def create_veichle(Veichle: VeichleProps):
    resullt = VeichleRepository.create(Veichle)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder({
            "msg": "veichle inserted"
        })
    )

@router_post.post("/veichle/")
async def get_veichle_by_image(account_logged: Annotated[
    dict, Depends(JWTTokenExceptionHandler.get_user_logged)],image: UploadFile = File()):
    path_image = f"{PATH}\\boards_temporarys\{image.filename}"
    with open(path_image, "wb+") as fb:
        """save image temporary"""
        fb.write(image.file.read())
        
    datas = VeichleRepository.get_datas_by_board_picture(path_image)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(datas)
    )
