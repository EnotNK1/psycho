from psycopg2 import Error
from sqlalchemy import create_engine, select, func, distinct
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, join, DeclarativeBase

from database.models.exercise import Exercise_structure, Сompleted_exercise, Filled_field
from schemas.exercise import FieldResult
from typing import List
from sqlalchemy.exc import NoResultFound

from database.inquiries import inquiries
from database.models.client import *
from database.models.diary import *
from database.models.education import *
from database.models.experiment import *
from database.models.inquiry import *
from database.models.mood_tracker import *
from database.models.post import *
from database.models.problem import *
from database.models.test import *
from database.models.users import *
from database.models.review import *

from database.database import engine, session_factory
from database.calculator import calculator_service
from database.enum import DiaryType
from fastapi import FastAPI, HTTPException
import uuid
from datetime import datetime

class ExerciseServicedb:

    def get_all_exercises(self) -> list:
        with session_factory() as session:
            try:
                query = select(Exercise_structure).options(joinedload(Exercise_structure.field))
                res = session.execute(query)
                exercise = res.unique().scalars().all()

                result_list = []
                for exercise_structure in exercise:
                    result_dict = {
                        "id": exercise_structure.id,
                        "title": exercise_structure.title,
                        "description": exercise_structure.description,
                    }
                    result_list.append(result_dict)

                    # field_results = []
                    #
                    # for field in exercise_structure.field:
                    #     field_results.append(field)
                    # result_dict["field"] = field_results
                    # result_list.append(result_dict)

                return result_list
            except (Exception, Error) as error:
                print(error)
                return []

    def get_exercise(self, exercise_id: uuid.UUID) -> list:
        with session_factory() as session:
            try:
                query = select(Exercise_structure).filter_by(id=exercise_id).options(
                    joinedload(Exercise_structure.field))
                res = session.execute(query)
                exercise = res.unique().scalars().all()

                result_list = []
                for exercise_structure in exercise:
                    result_dict = {
                        "id": exercise_structure.id,
                        "title": exercise_structure.title,
                        "description": exercise_structure.description,
                    }
                    result_list.append(result_dict)

                    field_results = []
                    for field in exercise_structure.field:
                        field_results.append(field)
                    result_dict["field"] = field_results

                return result_list
            except (Exception, Error) as error:
                print(error)
                return []

    def save_exercise_result_db(self, user_id, exercise_id, results: List[FieldResult]):
        with (session_factory() as session):
            try:
                result = 0
                exercise = session.query(Exercise_structure).filter_by(id=exercise_id).one()
                if not exercise:
                    raise HTTPException(status_code=404, detail="Упражнение не найдено!")

                field_cnt = len(exercise.field)
                # if field_cnt
                completed_exercise_id = uuid.uuid4()
                filled_fields = []
                #
                # for i in range(0, field_cnt):
                #     field = results[i]
                #     filled_field = Filled_field(
                #        id=uuid.uuid4(),
                #         text=field.value,
                #         field_id=field.field_id,
                #         completed_exercise_id=completed_exercise_id
                #     )
                #     filled_fields.append(filled_field)

                calculator_service.check_number_responses(len(results), field_cnt)
                exercise_result = Сompleted_exercise(id=completed_exercise_id,
                                                     date=datetime.now(),
                                                     exercise_structure_id=exercise_id,
                                                     user_id=user_id,
                                                     filled_field=filled_fields
                                                     )
                session.add(exercise_result)

                for i in range(0, field_cnt):
                    field = results[i]
                    filled_field = Filled_field(
                        id=uuid.uuid4(),
                        text=field.value,
                        field_id=field.field_id,
                        completed_exercise_id=completed_exercise_id
                    )
                    filled_fields.append(filled_field)
                    session.add(filled_field)

                session.commit()
                return {
                    "result": result,
                    "exercise_result_id": completed_exercise_id
                }

            except NoResultFound:
                raise HTTPException(status_code=404, detail="Упражнение или поле не были найдены!")
            except (Exception, Error) as error:
                raise error

    def get_exercise_results(self, exercise_id, user_id):
        with session_factory() as session:
            try:
                exercise_results = session.query(Сompleted_exercise).filter(
                    (Сompleted_exercise.exercise_structure_id == exercise_id) & (Сompleted_exercise.user_id == user_id)
                ).all()
                results_list = []

                for exercise_result in exercise_results:
                    result_dict = {
                        "completed_exercise_id": exercise_result.id,
                        "date": exercise_result.date
                    }
                    results_list.append(result_dict)

                return results_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_completed_exercise_results(self, completed_exercise_id, user_id):
        with session_factory() as session:
            try:
                exercise_results = session.query(Сompleted_exercise).filter(
                    (Сompleted_exercise.id == completed_exercise_id)
                ).first()

                if exercise_results == None:
                    raise HTTPException(status_code=404, detail="Такое упражнение не найдено!")

                if str(user_id) != str(exercise_results.user_id):
                    raise HTTPException(status_code=401, detail="Вы не имеете доступ к чужим упражнениям!")

                exercise_structure = session.query(Exercise_structure).filter(
                    Exercise_structure.id == exercise_results.exercise_structure_id
                ).first()

                title = exercise_structure.title if exercise_structure else "Не найдено"

                filled_fields = session.query(Filled_field).filter(
                    (Filled_field.completed_exercise_id == completed_exercise_id)
                ).all()
                filled_fields_values = []
                print(filled_fields)

                for filled_field in filled_fields:
                    filled_fields_values.append({
                        "field_id": filled_field.field_id,
                        "value": filled_field.text
                    })
                print(filled_fields_values)

                result_dict = {
                    "title": title,
                    "date": exercise_results.date,
                    "result": filled_fields_values
                }

                return result_dict

            except (Exception, Error) as error:
                print(error)
                return []

    def delete_exercise_result(self, completed_exercise_id, user_id):
        with session_factory() as session:
            try:
                exercise_results = session.query(Сompleted_exercise).filter(
                    (Сompleted_exercise.id == completed_exercise_id)
                ).first()

                if exercise_results == None:
                    raise HTTPException(status_code=404, detail="Такое упражнение не найдено!")

                if str(user_id) != str(exercise_results.user_id):
                    raise HTTPException(status_code=401, detail="Вы не имеете доступ к чужим упражнениям!")

                completed_exercise = session.query(Сompleted_exercise).filter_by(id=completed_exercise_id).one_or_none()
                session.delete(completed_exercise)
                session.commit()
            except (Exception, Error) as error:
                print(error)

    def edit_exercise_result(self, completed_exercise_id, results, user_id):

        with session_factory() as session:
            try:
                completed_exercise = session.query(Сompleted_exercise).get(completed_exercise_id)
                if completed_exercise == None:
                    raise HTTPException(status_code=404, detail="Выполненное упражнение не найдено!")

                if str(user_id) != str(completed_exercise.user_id):
                    raise HTTPException(status_code=401, detail="Вы не имеете доступ к чужим упражнениям!")

                filled_fields = session.query(Filled_field).filter(
                    (Filled_field.completed_exercise_id == completed_exercise_id)
                ).all()

                for filled_field in filled_fields:
                    for result in results:
                        if result.field_id == filled_field.field_id:
                            filled_field.text = result.value
                            break

                session.commit()
            except (Exception, Error) as error:
                print(error)

exercise_service_db: ExerciseServicedb = ExerciseServicedb()