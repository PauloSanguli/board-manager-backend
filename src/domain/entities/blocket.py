from typing import Type
from datetime import date

from pydantic import BaseModel



class BlocketProps(BaseModel):
    """blocket fields"""
    board: str
    chassis: str
    mark: str
    model: str
    category_veichle: str
    number_places: int
    color: str
    type_fuel: str
    fiscal_power: str
    issue_date_board: date
    veichle_purchase_date: date
    last_inspection_date: date
    enviroment_class_veichle: str
    emissions_co2: float
    gross_weight: float
    obs: str
    



class BlocketMap:
    """"""
    def __init__(self,model_entitie: BlocketProps):
        """create the schema of blocket"""
        self.__fields_doc = {
            "board":model_entitie.board,
            "chassis":model_entitie.chassis,
            "mark":model_entitie.mark,
            "model":model_entitie.model,
            "category_veichle":model_entitie.category_veichle,
            "number_places":model_entitie.number_places,
            "color":model_entitie.color,
            "type_fuel":model_entitie.type_fuel,
            "fiscal_power":model_entitie.fiscal_power,
            "issue_date_board":model_entitie.issue_date_board,
            "veichle_purchase_date":model_entitie.veichle_purchase_date,
            "last_inspection_date":model_entitie.last_inspection_date,
            "enviroment_class_veichle":model_entitie.enviroment_class_veichle,
            "emissions_co2":model_entitie.emissions_co2,
            "gross_weight":model_entitie.gross_weight,
            "obs":model_entitie.obs
        }
    
    def get_fields(self) -> dict:
        """return the schema"""
        return self.__fields_doc.copy()