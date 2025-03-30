import datetime
from typing import List, Optional
from typing import Union
from database.enum import FieldType
import pydantic
import uuid

class FieldResult(pydantic.BaseModel):
    field_id: uuid.UUID
    exercises: Optional[List[str]] = None
    value: Union[str, int]

class SaveExerciseResult(pydantic.BaseModel):
    exercise_structure_id: uuid.UUID
    result: List[FieldResult]


class DefiningProblemGroups(pydantic.BaseModel):
    sphere: str
    emotion: str
    target: str


class ProblemsAndGoals(pydantic.BaseModel):
    sphere: str
    emotion: str
    event: str
    argument: str
    target: str


class ProblemAnalysis(pydantic.BaseModel):
    problem: str
    target: str
    elaboration: str
    belief: str


class TestingBeliefs(pydantic.BaseModel):
    truthfulness_dogmatic: str
    logic_dogmatic: str
    utility_dogmatic: str
    truthfulness_flexible: str
    logic_flexible: str
    utility_flexible: str


class BeliefAnalysis(pydantic.BaseModel):
    action_dogmatic: str
    interference_dogmatic: str
    results_dogmatic: str
    action_flexible: str
    interference_flexible: str
    results_flexible: str

class ResponseGetExerciseResult(pydantic.BaseModel):
    title: str
    completed_exercise_id: uuid.UUID
    date: datetime.datetime

class ResponseGetDetailExerciseResult(pydantic.BaseModel):
    title: str
    date: datetime.datetime
    result: List[FieldResult]

class EditExerciseResult(pydantic.BaseModel):
    completed_exercise_id: uuid.UUID
    result: List[FieldResult]



class FilledFieldCreate(pydantic.BaseModel):
    field_id: uuid.UUID
    text: str

class FilledFieldRead(pydantic.BaseModel):
    id: uuid.UUID
    text: str
    type: str
    title: str

class CompletedExerciseCreate(pydantic.BaseModel):
    exercise_id: uuid.UUID
    filled_fields: List[FilledFieldCreate]

class CompletedExerciseRead(pydantic.BaseModel):
    id: uuid.UUID
    date: datetime.datetime
    filled_fields: List[FilledFieldRead]

class CompletedExerciseDetailRead(pydantic.BaseModel):
    title: str
    date: datetime.datetime
    filled_fields: List[FilledFieldRead]