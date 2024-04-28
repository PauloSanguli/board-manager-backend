from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from .....domain.entities.traffic_agent import AccountProps

from ...repositories.agent_repository import AccountRepository



router_post_agent = APIRouter(prefix="/board-manager",tags=["account"])

@router_post_agent.post("/account")
def create_account(account_fields: AccountProps):
    AccountRepository.create(account_fields)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder({
            "msg": "account created"
        })
    )
