from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

from .....domain.entities.owner import OwnerProps

from ...repositories.owner_repository import OwnerRepository



api = APIRouter(prefix="/board-manager", tags=["owner"])


@api.post("/owner")
def create_owner(Owner: OwnerProps):
    response = OwnerRepository.create(Owner)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder({
            "msg": response
        })
    )
    