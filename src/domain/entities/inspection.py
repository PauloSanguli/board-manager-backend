"""class props of inspection"""

from pydantic import BaseModel

from datetime import date



class InspectionProps(BaseModel):
    expiration_date: date
    cod: str
