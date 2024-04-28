"""clas props of newspaper"""

from pydantic import BaseModel

from datetime import datetime

from typing import Type




class NewspaperProps(BaseModel):
    reference: str
    body: str
    date_publish: Type[datetime]
    updated_at: Type[datetime]
    owner_id: int
