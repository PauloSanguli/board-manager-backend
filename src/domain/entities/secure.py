"""class props of secure"""

from pydantic import BaseModel

from datetime import date



class SecureProps(BaseModel):
    expiration_date: date
    cod: str
