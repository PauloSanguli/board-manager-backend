from ....application.repositories.traffic_agent_repository import (
    ITrafficAgentRepository
)
from ....domain.entities.traffic_agent import AccountProps, Login

from sqlalchemy.orm import Session
from sqlalchemy import and_, select
from ...models import engine, traffic_agent

from ....application.security import PasswordSecure

from fastapi import HTTPException

from ..middleware.auth_agent import TokenHandler as token

from ..responses.agent_response import Responses as response




class AccountRepository(ITrafficAgentRepository):
    def create(account: AccountProps):
        try:
            with Session(engine) as session:
                query = traffic_agent.insert()

                session.execute(query, {
                    "username": account.username,
                    "password": PasswordSecure.encrypt(account.password),
                    "email": account.email,
                    "cellphone": account.cellphone
                })
        except Exception as error:
            raise HTTPException(
                detail="account dont created",
                status_code=400
            )
        else: session.commit()
    
    def login(modelAgent: Login):
        """login agent"""
        with Session(engine) as session:
            agentLog = session.execute(
                select(
                    traffic_agent.c.password,
                    traffic_agent.c.id
                ).where(and_(traffic_agent.c.email==modelAgent.email))
            ).fetchone()
        
        if agentLog:
            STATUS_CHECK_PASSWORD = PasswordSecure.check(modelAgent.password, agentLog[0])
            if STATUS_CHECK_PASSWORD:
                return token.create(agentLog[1])
            raise HTTPException(
                detail="invalid password",
                status_code=400
            )
        raise HTTPException(
            detail="account dont finded",
            status_code=404
        )

    def get_info_account(id_agent: int):
        """get datas of account"""
        with Session(engine) as session:
            result = session.execute(select(
                    traffic_agent.c.username,
                    traffic_agent.c.email,
                    traffic_agent.c.cellphone
                ).where(and_(
                    traffic_agent.c.id==id_agent
                ))).fetchone()
        
        if not result:
            raise HTTPException(
                detail="account dont finded",
                status_code=404
            )
        return response.return_datas(result)
            
            