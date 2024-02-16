import pydantic
import uuid

class Creds(pydantic.BaseModel):
    username: str
    password: str

class User(pydantic.BaseModel):
    id: uuid.UUID
    username: str
