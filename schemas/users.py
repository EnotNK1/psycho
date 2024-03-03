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
    gender: str

class ResetPassword(pydantic.BaseModel):
    email: str