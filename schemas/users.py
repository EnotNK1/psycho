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


class UserResponse(pydantic.BaseModel):
    token: str
    user_id: uuid.UUID
    role: int
    email: str
    username: str


class ResetPassword(pydantic.BaseModel):
    email: str


class UpdateUser(pydantic.BaseModel):
    birth_date: datetime.date
    gender: str
    username: str
    request: List[int]
    city: str
    description: str
    type: int


class AuthToken(pydantic.BaseModel):
    token: str


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

class Manager(pydantic.BaseModel):
    username: str
    description: str
    city: str
    online: bool
    gender: str
    birth_date: datetime.date

class GiveTask(pydantic.BaseModel):
    text: str
    user_id: uuid.UUID
    test_title: str
    test_id: uuid.UUID

class TaskId(pydantic.BaseModel):
    task_id: uuid.UUID