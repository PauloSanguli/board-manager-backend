from datetime import date
from typing import Type

from fastapi import HTTPException

from ..responses.owner_responses import Responses

from ...models import (
    owner as owner_table, engine, identity_card, driving_license
)
from sqlalchemy.orm import Session
from sqlalchemy import select, and_

from ....domain.entities.owner import OwnerProps
from ....domain.entities.driving_license import DrivingLicenseMap
from ....domain.entities.identity_card import IndentityCardMap

from ....application.repositories.owner_repository import (
    IOwnerRepository
)
import logging



logging.basicConfig()

class OwnerRepository(IOwnerRepository):
    """repository owner"""

    def create(owner: OwnerProps):
        """insert the owner in database"""
        __driving_license_dic = DrivingLicenseMap(owner.driving_license)
        __identity_card_dic = IndentityCardMap(owner.identity_card)
        try:
            with Session(engine) as session:

                query_ident = identity_card.insert()
                query_drivi = driving_license.insert()
                query_owner = owner_table.insert()

                session.execute(query_drivi, __driving_license_dic.get_dic())
                session.execute(query_ident, __identity_card_dic.get_dic())
                session.commit()
                
                session.execute(query_owner, {
                    "identity_card_id": OwnerRepository.\
                        get_id_by_ticket_number(owner.identity_card.ticket_number),
                    "driving_license_id": OwnerRepository.\
                        get_id_by_name_and_date(owner.driving_license.name, owner.driving_license.issue_date)
                })
                session.commit()
        except:
            raise HTTPException(
                status_code=400,
                detail="owner dont created"
            )
        else:
            return {
                "msg": "owner created"
            }

    
    def get_all():
        """get all owners"""
        with Session(engine) as session:
            query = select(
                identity_card,
                driving_license,
                owner_table.c.id
            ).\
                select_from(
                    owner_table.outerjoin(
                        identity_card, owner_table.c.identity_card_id==identity_card.c.id
                    ).outerjoin(
                        driving_license,owner_table.c.driving_license_id==driving_license.c.id
                    )
                )
            datas = session.execute(query).fetchall()
            
        return Responses.get_all(datas)
    
    def get_by_id(id: int):
        """get  identity card or driving license by id"""
        with Session(engine) as session:
            query = select(
                identity_card,
                driving_license,
                owner_table.c.id
            ).select_from(
                owner_table.outerjoin(
                    identity_card, owner_table.c.identity_card_id==identity_card.c.id
                ).outerjoin(
                    driving_license, owner_table.c.driving_license_id==driving_license.c.id
                )
            ).where(owner_table.c.id==id)
            datas = session.execute(query).fetchone()
            
        return Responses.get_one(datas)
    
    def get_id_by_ticket_number(ticket: str):
        """find identity card by ticket number"""
        with Session(engine) as session:
            query = select(identity_card.c.id).\
                where(and_(identity_card.c.ticket_number==ticket))
            datas = session.execute(query).fetchone()[0]
        return datas
    
    def get_id_by_name_and_date(name: str, date_: date):
        """find driving license by name and issue date"""
        with Session(engine) as session:
            query = select(driving_license.c.id).\
                where(and_(driving_license.c.name==name,driving_license.c.issue_date==date_))
            datas = session.execute(query).fetchone()[0]
        return datas
    
    def get_driving_license(ticket_number: str):
        """get driving license of an owner by ticket number"""
        with Session(engine) as session:
            query = select(
                    driving_license.c.name,
                    driving_license.c.issue_date,
                    driving_license.c.expiration_date,
                    driving_license.c.category_veichle,
                    driving_license.c.restrictions,
                    driving_license.c.veichle_identification_number,
                    driving_license.c.document_issuer_signature,
                    driving_license.c.expired,
                ).select_from(
                driving_license.join(
                    owner_table, driving_license.c.id==owner_table.c.driving_license_id
                ).join(
                    identity_card, owner_table.c.identity_card_id==identity_card.c.id
                )
            ).where(and_(identity_card.c.ticket_number==ticket_number))
            result = session.execute(query).fetchone()
        if not result:
            raise HTTPException(
                detail="driving license dont finded",
                status_code=404                
            )
        return Responses.get_driving_license(result)
