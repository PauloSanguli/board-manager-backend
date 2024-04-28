from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import Annotated

from fastapi import Form

from .....domain.entities.traffic_agent import Login

from ...repositories.agent_repository import AccountRepository





router_login = APIRouter(prefix="/board-manager", tags=["agent"])

@router_login.post("/login")
def login_agent(model: Login):
    token = AccountRepository.login(model)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=jsonable_encoder({
            "token": token
        })
    )
