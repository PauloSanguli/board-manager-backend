from ...controllers.owner import ControllerOwner

from fastapi import APIRouter
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .....domain.entities.driving_license import DrivingLicenseProps
from .....domain.entities.identity_card import IdentityCardProps



update_router = APIRouter(prefix="/board-manager",tags=["owner"])

@update_router.patch("/owner/identity_card/{id}")
def update_identity_card(doc: IdentityCardProps, id: int):
    ControllerOwner.update_identity_card(doc, id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "msg": "document updated"
        })
    )

@update_router.patch("/owner/driving_license/{id}")
def update_driving_license(doc: DrivingLicenseProps, id: int):
    ControllerOwner.update_driving_license(doc, id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "msg": "document updated"
        })
    )
