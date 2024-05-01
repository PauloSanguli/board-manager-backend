from fastapi import Header
from fastapi import HTTPException

from typing import Annotated

import jwt

import os



class JWTTokenExceptionHandler:
    
    @classmethod
    def get_user_logged(cls, x_acess_token: Annotated[str, Header()]):
        """metod for get user logged form token"""
        try:
            print(x_acess_token, str(os.getenv("SECRET_KEY")))
            FIELDS_ACCOUNT_LOGGED = jwt.decode(x_acess_token, str(os.getenv("SECRET_KEY")), ["HS256"])
        except Exception as error:
            print(error)
            cls.set_exception_http("your signature was expired", 401)
        return FIELDS_ACCOUNT_LOGGED
    
    @classmethod
    def set_exception_http(cls, detail_exception: str, status_code: int):
        """padronize http exceptions"""
        raise HTTPException(
            detail=detail_exception,
            status_code=status_code
        )
