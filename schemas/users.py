import datetime
from typing import List

import pydantic
import uuid


class Creds(pydantic.BaseModel):
    email: str
    password: str


class Reg(pydantic.BaseModel):
    email: str
    username: str
    password: str
    confirm_password: str


class ResetPassword(pydantic.BaseModel):
    email: str


class AddProblem(pydantic.BaseModel):
    description: str


class UpdateUser(pydantic.BaseModel):
    birth_date: datetime.date
    gender: str
    username: str
    request: List[int]
    city: str
    description: str
    type: int


class SaveTestRes(pydantic.BaseModel):
    title: str
    score: int
    test_id: str
    date: datetime.datetime


class CreateTest(pydantic.BaseModel):
    title: str
    description: str
    short_desc: str


class GetTestRes(pydantic.BaseModel):
    test_id: str


class Psychologist(pydantic.BaseModel):
    username: str
    title: str
    document: str
    description: str
    city: str
    online: bool
    face_to_face: bool
    gender: str
    birth_date: datetime.date
    request: List[int]


class GetClient(pydantic.BaseModel):
    user_id: str


class SendАpplication(pydantic.BaseModel):
    user_id: str
    text: str

class ConfirmApplication(pydantic.BaseModel):
    user_id: str
    status: bool