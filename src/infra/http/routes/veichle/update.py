from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

from ...controllers.veichles import Controller

from ....models import license, secure, inspection

from .....domain.entities.secure import SecureProps
from .....domain.entities.license import LiecenseProps
from .....domain.entities.inspection import InspectionProps





router_pacth = APIRouter(prefix="/board-manager",tags=["veichle"])

@router_pacth.patch("/veichle/secure/{id}/")
def update_secure(id: int,doc: SecureProps):
    Controller.update_doc(doc,id,secure)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "msg": "document updated"
        })
    )

@router_pacth.patch("/veichle/inspection/{id}/")
def update_inspection(id: int,doc: InspectionProps):
    Controller.update_doc(doc,id,inspection)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "msg": "document updated"
        })
    )

@router_pacth.patch("/veichle/license/{id}/")
def update_license(id: int,doc: LiecenseProps):
    Controller.update_doc(doc,id,license)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "msg": "document updated"
        })
    )
