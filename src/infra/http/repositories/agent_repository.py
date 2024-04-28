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






class AccountRepository(ITrafficAgentRepository):
    def create(account: AccountProps):
        with Session(engine) as session:
            query = traffic_agent.insert()

            session.execute(query, {
                "username": account.username,
                "password": PasswordSecure.encrypt(account.password),
                "email": account.email,
                "cellphone": account.cellphone
            })
            session.commit()
    
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
