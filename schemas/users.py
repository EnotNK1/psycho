import datetime

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