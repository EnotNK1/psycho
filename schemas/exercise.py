import datetime
from typing import List, Optional
from typing import Union
from database.enum import FieldType
import pydantic
import uuid

# class FieldResult(pydantic.BaseModel):
#     field_id: uuid.UUID
#     exercises: Optional[List[str]] = None
#     value: Union[str, int]

# class SaveExerciseResult(pydantic.BaseModel):
#     exercise_structure_id: uuid.UUID
#     result: List[FieldResult]


class DefiningProblemGroups(pydantic.BaseModel):
    field_1: str
    field_2: str
    field_3: str


class ProblemsAndGoals(pydantic.BaseModel):
    field_1: str
    field_2: str
    field_3: str
    field_4: str
    field_5: str


class ProblemAnalysis(pydantic.BaseModel):
    field_1: str
    field_2: str
    field_3: str
    field_4: str


class TestingBeliefs(pydantic.BaseModel):
    field_1: str
    field_2: str
    field_3: str
    field_4: str
    field_5: str
    field_6: str


class BeliefAnalysis(pydantic.BaseModel):
    field_1: str
    field_2: str
    field_3: str
    field_4: str
    field_5: str
    field_6: str

# class ResponseGetExerciseResult(pydantic.BaseModel):
#     title: str
#     completed_exercise_id: uuid.UUID
#     date: datetime.datetime

# class ResponseGetDetailExerciseResult(pydantic.BaseModel):
#     title: str
#     date: datetime.datetime
#     result: List[FieldResult]

# class EditExerciseResult(pydantic.BaseModel):
#     completed_exercise_id: uuid.UUID
#     result: List[FieldResult]



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