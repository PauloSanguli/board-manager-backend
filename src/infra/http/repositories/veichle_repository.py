from ...models import (
    blocket,
    car_veichle_title,
    veichle,
    owner,
    engine,
    secure,
    inspection,
    license,
    infractions
)
from sqlalchemy.orm import Session
from sqlalchemy import select, and_

from ....domain.entities.blocket import BlocketMap
from ....domain.entities.car_veichle_title import CarVeichleTitleMap
from ....domain.entities.veichle import VeichleProps

from ....application.repositories.veichle_repository import IVeichleRepository

from ..responses.veichle_entities import Responses

from .owner_repository import OwnerRepository

from src.filter.board import ProcessImage as processor

from src.domain.entities.infractions import InfractionsMap

from src.domain.validators.validator_board import validate_board

from fastapi import HTTPException





class VeichleRepository(IVeichleRepository):
    """"""
    def create(veichle_model: VeichleProps):
        """insert veichle in database"""
        if not validate_board(veichle_model.board):
            raise HTTPException(
                detail="invalid board",
                status_code=400
        )

        try:
            __car_veichle_title_doc = CarVeichleTitleMap(veichle_model.car_veichle_title)
            __blocket_doc = BlocketMap(veichle_model.blocket)

            license_id = VeichleRepository.create_docs(veichle_model.license, license)
            secure_id = VeichleRepository.create_docs(veichle_model.secure, secure)
            inspection_id = VeichleRepository.create_docs(veichle_model.inspection, inspection)

            with Session(engine) as session:
                car_veichle_title_id = VeichleRepository.\
                    create_docs_car(car_veichle_title, __car_veichle_title_doc.get_fields())
                blocket_id = VeichleRepository.\
                    create_docs_car(blocket, __blocket_doc.get_fields())
                
                session.execute(veichle.insert(), {
                    "owner_id": veichle_model.owner_id,
                    "license_id": license_id,
                    "secure_id": secure_id,
                    "inspection_id": inspection_id,
                    "blocket_id": blocket_id,
                    "car_veichle_title_id": car_veichle_title_id,
                    "board": veichle_model.board
                })
                session.commit()
        except Exception as error:
            print(error)            
            raise HTTPException(
                detail="error inserting veichle",
                status_code=400
            )
        return "veichle inserted"
        
    def create_docs(doc, model_):
        """create determinated doc"""
        with Session(engine) as session:
            session.execute(model_.insert(), {
                "expiration_date": doc.expiration_date,
                "cod": doc.cod
            })#.fetchone()[0]
            session.commit()
        # return id
        query = select(model_.c.id).where(and_(model_.c.cod==doc.cod))
        return session.execute(query).fetchone()[0]

    def create_docs_car(model, dic):
        """create the car veichle title and blocket"""
        with Session(engine) as session:
            session.execute(model.insert(), dic)
            session.commit()

            query = select(model.c.id).where(and_(model.c.board==dic["board"]))
            return session.execute(query).fetchone()[0]

    def get_all():
        """get all veichles"""
        with Session(engine) as session:
            datas = session.execute(select(veichle).\
                where(and_(veichle.c.id))).fetchall()
        return datas
    
    def get_id_by_board(board):
        """get id by the board"""
        with Session(engine) as session:
            query = select(veichle.c.id).where(and_(veichle.c.board==board))
            id = session.execute(query).fetchone()[0]
        return id
    

    def get_by_board(board: str):
        """get veichle by board"""
        with Session(engine) as session:
            query = select(
                veichle.c.owner_id,blocket,car_veichle_title,secure,license,inspection,veichle.c.id
            ).select_from(
                veichle.outerjoin(
                    blocket, veichle.c.blocket_id==blocket.c.id
                ).outerjoin(
                    car_veichle_title, veichle.c.car_veichle_title_id==car_veichle_title.c.id
                ).outerjoin(
                    secure, veichle.c.secure_id==secure.c.id
                ).outerjoin(
                    license, veichle.c.license_id==license.c.id
                ).outerjoin(
                    inspection, veichle.c.inspection_id==inspection.c.id
                )
            ).where(and_(veichle.c.board==board))
            datas = session.execute(query).fetchone()
        owner = OwnerRepository.get_by_id(datas[0])
        return Responses.get_one(datas),owner

    def get_datas_by_board_picture(image: str):
        textImageResult = processor.extract_text(image)
    
    def regist_infraction_veichle(infraction_info):
        datas = VeichleRepository.\
            get_by_board(infraction_info.board)
        datas = {
            "owner": datas[1],
            "veichle": datas[0]
        }
        identityCardId = datas["owner"]["identity_card"]["id"]
        blocketId = datas["veichle"]["blocket"]["id"]
        
        schema_infraction_final = InfractionsMap(infraction_info, identityCardId, blocketId).get_dic()
        with Session(engine) as session:
            session.\
                execute(infractions.insert(),schema_infraction_final)
            session.commit()
    
    def get_infractions(board_car: str):
        """get infractions of an car"""
        with Session(engine) as session:
            query_select = select(
                    infractions.c.num_carter_habilitacion,
                    infractions.c.obs,
                    infractions.c.date,
                    infractions.c.local,
                    infractions.c.time,
                    infractions.c.type_infraction,
                    infractions.c.value,
                    infractions.c.info_payment,
                    infractions.c.paid,
                    infractions.c.id
                ).select_from(
                    infractions.join(
                        blocket, infractions.c.blocket_id==blocket.c.id
                    )
                ).where(and_(blocket.c.board==board_car))
            datas = session.execute(query_select).fetchall()
        return Responses.get_infractions(datas)
    
    def get_value(id: int):
        """get value of infraction"""
        with Session(engine) as session:
            value_paid = session.execute(select(infractions.c.value).\
                where(and_(infractions.c.id==id))).fetchone()
        if not value_paid:
            raise HTTPException(
                detail="infraction dont finded",
                status_code=404
            )
        return value_paid[0]

    def payment(id_infraction: int, value: float):
        """paid infraction"""
        value_paid = VeichleRepository.get_value(id_infraction)
        
        if value != value_paid:                    
            raise HTTPException(
                detail="the value is diferent",
                status_code=400
            )
            
        with Session(engine) as session:
            session.execute(infractions.update().values({
                "paid": True
            }).where(and_(infractions.c.id==id_infraction)))
            session.commit()
