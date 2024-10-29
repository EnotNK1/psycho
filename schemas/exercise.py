import datetime
from typing import List, Optional
from typing import Union
from database.enum import FieldType
import pydantic
import uuid

class FieldResult(pydantic.BaseModel):
    field_id: uuid.UUID
    value: Union[str, int]

class SaveExerciseResult(pydantic.BaseModel):
    exercise_result_id: uuid.UUID
    result: List[FieldResult]

class ResponseGetExerciseResult(pydantic.BaseModel):
    completed_exercise_id: uuid.UUID
    date: datetime.datetime

class ResponseGetDetailExerciseResult(pydantic.BaseModel):
    title: str
    date: datetime.datetime
    result: List[FieldResult]

class EditExerciseResult(pydantic.BaseModel):
    completed_exercise_id: uuid.UUID
    result: List[FieldResult]



# class FilledFieldCreate(pydantic.BaseModel):
#     field_id: uuid.UUID
#     text: str
#
# class FilledFieldRead(pydantic.BaseModel):
#     id: uuid.UUID
#     text: str
#     type: str
#     title: str
#
# class CompletedExerciseCreate(pydantic.BaseModel):
#     exercise_id: uuid.UUID
#     filled_fields: List[FilledFieldCreate]
#
# class CompletedExerciseRead(pydantic.BaseModel):
#     id: uuid.UUID
#     date: datetime.datetime
#     filled_fields: List[FilledFieldRead]
#
# class CompletedExerciseDetailRead(pydantic.BaseModel):
#     title: str
#     date: datetime.datetime
#     filled_fields: List[FilledFieldRead]