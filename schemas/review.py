import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr

import pydantic
import uuid

class ReviewCreate(pydantic.BaseModel):
    text: str

class ReviewRead(pydantic.BaseModel):
    id: uuid.UUID
    text: str
    email: str
    is_read: bool
    created_at: datetime.datetime

    class Config:
        from_attributes = True