"""class props of veichle"""

from pydantic import BaseModel

from .car_veichle_title import CarVeichleTitlleProps
from .blocket import BlocketProps
from .secure import SecureProps
from .license import LiecenseProps
from .inspection import InspectionProps



class VeichleProps(BaseModel):
    board: str
    state: str
    secure: SecureProps
    inspection: InspectionProps
    license: LiecenseProps
    blocket: BlocketProps
    car_veichle_title: CarVeichleTitlleProps
    owner_id: int

class FindBoard(BaseModel):
    path_image: str
