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
    link_to_picture: str

class ResponceMaterial(pydantic.BaseModel):
    id: uuid.UUID
    text: str
    link_to_picture: str


class ResponceGetAllMaterial(pydantic.BaseModel):
    theme: str
    score: int
    max_score: int
    materials: List[ResponceMaterial]
