from pydantic import BaseModel

from datetime import date
from datetime import time

from typing import Optional

class InfractionsProps(BaseModel):
    """infraction fields"""
    board: str | None = ""
    id: int | None = 0
    num_carter_habilitacion: int
    obs: str
    date: date
    local: str
    time: time
    type_infraction: str
    info_payment: str
    value: float | None = 0.0
    paid: bool | None = False


class InfractionsMap:
    def __init__(self,infractions: InfractionsProps, identity_id: int, blocket_id: int):
        """create the schema identity card"""
        self.descript_infraction = InfractionsMap.__calcule_value(infractions.type_infraction)
        self.__infractions = {
            "identity_card_id": identity_id,
            "blocket_id": blocket_id,
            "num_carter_habilitacion": infractions.num_carter_habilitacion,
            "obs": infractions.obs,
            "date": infractions.date,
            "local": infractions.local,
            "time": infractions.time,
            "type_infraction": self.descript_infraction["descript"],
            "value": self.descript_infraction["value"],
            "info_payment": infractions.info_payment
        }
    
    def get_dic(self):
        """return the schema"""
        return self.__infractions.copy()
    
    @staticmethod
    def __get_descript(cod_infraction: str):
        """get descript and ucf for infraction"""
        UFC_INFRACTIONS = {
            "A01": {
                "descript": "conduzir bêbado",
                "ucf": 60
            },
            "A02": {
                "descript": "conduzir sob influência de subnstâncias nocisas ao organismo",
                "ucf": 120
            },
            "A03": {
                "description": "excesso de velocidade",
                "ucf": 80
            }
        }
        return UFC_INFRACTIONS.get(cod_infraction)

    @staticmethod
    def __calcule_value(cod_infraction: str):
        """calcule the value of infraction"""
        dic = InfractionsMap.__get_descript(cod_infraction)
        return {
            "descript": dic.get("descript"),
            "value": dic.get("ucf")*88
        }
