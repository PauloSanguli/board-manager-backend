from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

from ...repositories.owner_repository import (
    OwnerRepository
)


router_get = APIRouter(prefix="/board-manager",tags=["owner"])

@router_get.get("/owner/")
async def get_owners():
    result = OwnerRepository.get_all()

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(result)
    )

@router_get.get("/owner/{id}/")
def get_owner_by_id(id: int):
    result = OwnerRepository.get_by_id(id)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(result)
    )

@router_get.get("/owner/driving_license/{ticket_number}/")
def get_driving_license_car(ticket_number: str):
    
    response = OwnerRepository.get_driving_license(ticket_number)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(response)
    )

# @router_get.get("/owner/veichles/{ticket_number}/")
# def get_veichles_by_ticket_num(ticket_number: str):

#     OwnerRepository.

#     return JSONResponse(
#         status_code=status.HTTP_200_OK,
#         content=jsonable_encoder({})
#     )
