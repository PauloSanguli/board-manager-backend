from pydantic import BaseModel

from datetime import date





class IdentityCardProps(BaseModel):
    """identity card fields"""
    name: str
    membership: str
    ticket_number: str
    residence: str
    naturalness: str
    province: str
    date_birth: date
    sex: str
    marital_status: str
    height: float
    expired: bool
    issued_on: date
    valid_until: date



class IndentityCardMap:
    def __init__(self,identity_card: IdentityCardProps):
        """create the schema identity card"""
        self.__identity_card = {
            "name": identity_card.name,
            "membership": identity_card.membership,
            "ticket_number": identity_card.ticket_number,
            "residence": identity_card.residence,
            "naturalness": identity_card.naturalness,
            "province": identity_card.province,
            "date_birth": identity_card.date_birth,
            "sex": identity_card.sex,
            "marital_status": identity_card.marital_status,
            "height": identity_card.height,
            "expired": identity_card.expired,
            "issued_on": identity_card.issued_on,
            "valid_until": identity_card.valid_until
        }
    
    def get_dic(self):
        """return the schema"""
        return self.__identity_card.copy()
    