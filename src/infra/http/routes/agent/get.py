from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Depends

from typing import Annotated

from ...middleware.dependencie_admin import JWTTokenExceptionHandler

from ...repositories.agent_repository import AccountRepository




agent_get = APIRouter(
    prefix="/board-manager",
    tags=["agent"]
)


@agent_get.get("/datas/")
async def get_datas_account(
    account_logged: Annotated[
    dict, Depends(JWTTokenExceptionHandler.get_user_logged)]):
    response = AccountRepository.get_info_account(account_logged["id"])
    
    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=status.HTTP_200_OK
    )
