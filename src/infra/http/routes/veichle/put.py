from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse



from ...repositories.veichle_repository import VeichleRepository






router_put = APIRouter(prefix="/board-manager", tags=["veichle"])

@router_put.put("/payment_infraction/")
def payment_infraction(id_infraction: int, payment: float):
    VeichleRepository.payment(id_infraction, payment)
    
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "infraction payed with sucess"
        }),
        status_code=status.HTTP_200_OK
    )
