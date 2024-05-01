from datetime import timedelta, datetime

import os

import jwt

from fastapi import HTTPException


class TokenHandler:
    """encode and decode tokens"""

    def create(id: int):
        """create token"""
        try:
            payload = {
                "id": id,
                "exp": datetime.utcnow() + timedelta(days=1),
            }
            token = jwt.encode(payload, os.getenv("SECRET_KEY"))
        except Exception as error:
            print(error)
            raise HTTPException(status_code=400, detail="error creating the token")
        return token
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZXhwIjoxNzE0NDE0OTQ0fQ.YSLfWu4_YCjNLSiRbb_f8gxJF0MSWikDdpvh3UNyAKA
