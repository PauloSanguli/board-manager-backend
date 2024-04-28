from pydantic import BaseModel

from typing import Type
from datetime import date




class CarVeichleTitlleProps(BaseModel):
    """veichle fields"""
    name_owner: str
    home_adress_owner: str
    board: str
    chassis: str
    mark: str
    model: str
    color: str
    type_fuel: str
    number_places: int
    issue_date: date
    registration_date: date
    manufacture_date: date
    engine_number: str
    engine_power: str



class CarVeichleTitleMap:
    """"""
    def __init__(self,model_entitie: CarVeichleTitlleProps):
        """create the schema of car veichle title"""
        self.__fields_doc = {
            "name_owner": model_entitie.name_owner,
            "home_adress_owner": model_entitie.home_adress_owner,
            "board": model_entitie.board,
            "chassis": model_entitie.chassis,
            "mark": model_entitie.mark,
            "model": model_entitie.model,
            "color": model_entitie.color,
            "type_fuel": model_entitie.type_fuel,
            "number_places": model_entitie.number_places,
            "issue_date": model_entitie.issue_date,
            "registration_date": model_entitie.registration_date,
            "manufacture_date": model_entitie.manufacture_date,
            "engine_number": model_entitie.engine_number,
            "engine_power": model_entitie.engine_power
        }
    
    def get_fields(self) -> dict:
        """return the schema"""
        return self.__fields_doc.copy()
