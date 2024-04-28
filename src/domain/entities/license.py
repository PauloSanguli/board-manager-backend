"""class props of liecense"""

from pydantic import BaseModel

from typing import Type

from datetime import date



class LiecenseProps(BaseModel):
    expiration_date: date
    cod: str