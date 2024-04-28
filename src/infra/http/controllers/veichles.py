from ...models import engine

from sqlalchemy.orm import Session
from sqlalchemy import and_




class Controller:
    def update_doc(doc, id, model_type):
        with Session(engine) as session:
            query = model_type.update().values({
                "cod": doc.cod,
                "expiration_date": doc.expiration_date
            }).where(
                model_type.c.id==id
            )
            session.execute(query)
            session.commit()
