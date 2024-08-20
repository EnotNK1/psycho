import datetime
from typing import List

import pydantic
import uuid


class CompleteEducation(pydantic.BaseModel):
    education_material_id: uuid.UUID

class ResponceGetAllTheme(pydantic.BaseModel):
    id: uuid.UUID
    theme: str
    score: int
    max_score: int

class ResponceGetAllMaterial(pydantic.BaseModel):
    id: uuid.UUID
    text: str