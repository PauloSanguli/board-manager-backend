from datetime import timedelta, datetime

import os

import jwt

from fastapi import HTTPException


class TokenHandler:
    """"""

    def create(id: int):
        """create token"""
        try:
            key_app = "secret-key"
            payload = {
                "id": id,
                "exp": datetime.utcnow() + timedelta(days=1),
            }
            token = jwt.encode(payload, key_app)
        except:
            raise HTTPException(status_code=400, detail="error creating the token")
        return token
