from ...models import (
    identity_card, driving_license, engine
)
from sqlalchemy.orm import Session
from sqlalchemy import select, and_, update

from ....domain.entities.identity_card import (
    IdentityCardProps, IndentityCardMap
)
from ....domain.entities.driving_license import (
    DrivingLicenseProps, DrivingLicenseMap
)




class ControllerOwner:
    def update_identity_card(identity_card_: IdentityCardProps, id: int):
        """update identity card"""
        with Session(engine) as session:
            __identity_card_dic = IndentityCardMap(identity_card_)
            query_identity_c = identity_card.update().values(__identity_card_dic.get_dic()).\
                where(and_(
                    identity_card.c.id==id)
                )
            print(query_identity_c)
            session.execute(query_identity_c)
            session.commit()
    
    def update_driving_license(driving_license_: DrivingLicenseProps, id: int):
        """update driving license"""
        with Session(engine) as session:
            __driving_license_dic = DrivingLicenseMap(driving_license_)
            query_driving_li = driving_license.update().values(__driving_license_dic.get_dic()).\
                where(and_(
                    driving_license.c.id==id)
                )
            session.execute(query_driving_li)
            session.commit()
        
