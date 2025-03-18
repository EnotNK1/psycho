from psycopg2 import Error
from sqlalchemy import create_engine, select, func, distinct
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, join, DeclarativeBase
from sqlalchemy.dialects.postgresql import ARRAY

from database.exercise_info import Cpt_diary, Definition_group_problems, Definition_problems_setting_goals, \
    Problem_analysis, Testing_beliefs, Beliefs_analysis, Note
from database.models.exercise import Exercise_structure, Сompleted_exercise, Filled_field, Field
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

    def filling_in_links(self, exercise):
        with session_factory() as session:
            try:

                links = [
                    "/exercise/images_exercise/КПТ_дневник.png", "/exercise/images_exercise/Определение_групп_проблем.png",
                    "/exercise/images_exercise/Определение_проблемы_постановка_цели.png", "/exercise/images_exercise/Анализ_проблемы.png", "/exercise/images_exercise/Проверка_убеждений.png",
                    "/exercise/images_exercise/Анализ_убеждений.png", "/exercise/images_exercise/Лестница_страха.png"
                ]
                i = 0
                for theme in exercise:
                    theme.picture_link = links[i]
                    i += 1

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_exercises(self) -> list:
        with session_factory() as session:
            try:
                query = select(Exercise_structure).options(
                    joinedload(Exercise_structure.field))
                res = session.execute(query)
                exercise = res.unique().scalars().all()

                exercise_service_db.filling_in_links(exercise)

                result_list = []
                for exercise_structure in exercise:
                    result_dict = {
                        "id": exercise_structure.id,
                        "title": exercise_structure.title,
                        "description": exercise_structure.description,
                        "link_to_picture": exercise_structure.picture_link,
                        "linked_exercise_id": exercise_structure.linked_exercise_id,
                        "closed": exercise_structure.closed
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

    def get_exercise(self, exercise_id: uuid.UUID):
        with session_factory() as session:
            try:
                # Получаем упражнение по ID
                query = (
                    select(Exercise_structure)
                    .filter_by(id=exercise_id)
                    .options(
                        joinedload(Exercise_structure.field).joinedload(Field.variants)
                    )
                )
                res = session.execute(query)
                exercise = res.unique().scalars().all()

                for exercise_structure in exercise:
                    result_dict = {
                        "id": exercise_structure.id,
                        "title": exercise_structure.title,
                        "description": exercise_structure.description,
                        "closed": exercise_structure.closed
                    }

                    field_results = []
                    for field in exercise_structure.field:
                        field_data = {
                            "title": field.title,
                            "hint": field.hint,
                            "description": field.description,
                            "major": field.major,
                            "id": field.id,
                            "type": field.type,
                            "exercise_structure_id": field.exercise_structure_id,
                            "variants": [variant.title for variant in field.variants],
                            "exercises": field.exercises,
                        }
                        field_results.append(field_data)

                    # Определяем порядок полей для текущего упражнения
                    if exercise_structure.title == "КПТ-дневник":
                        expected_order = [field['title'] for field in Cpt_diary.fields]
                    elif exercise_structure.title == "Определение групп проблем":
                        expected_order = [field['title'] for field in Definition_group_problems.fields]
                    elif exercise_structure.title == "Проблемы и цели":
                        expected_order = [field['title'] for field in Definition_problems_setting_goals.fields]
                    elif exercise_structure.title == "Анализ проблемы":
                        expected_order = [field['title'] for field in Problem_analysis.fields]
                    elif exercise_structure.title == "Проверка убеждений":
                        expected_order = [field['title'] for field in Testing_beliefs.fields]
                    elif exercise_structure.title == "Анализ убеждений":
                        expected_order = [field['title'] for field in Beliefs_analysis.fields]
                    else:
                        expected_order = []  # Если упражнение не найдено, порядок не меняем

                    # Сортируем поля по порядку, указанному в expected_order
                    if expected_order:
                        field_results.sort(key=lambda x: expected_order.index(x['title']))

                    # Ищем все заполненные поля (filled_field), которые связаны с текущим упражнением
                    filled_fields_to_pull = session.query(Filled_field).filter(
                        Filled_field.exercises.contains([exercise_structure.title])
                    ).all()

                    pulled_fields = [
                        {
                            "id": filled_field.id,
                            "field_id": filled_field.field_id,
                            "text": filled_field.text,
                            "exercises": filled_field.exercises
                        }
                        for filled_field in filled_fields_to_pull
                    ]

                    # Добавляем "стянутые" поля в результат
                    result_dict["pulled_fields"] = pulled_fields
                    result_dict["field"] = field_results

                return result_dict

            except (Exception, Error) as error:
                print(error)
                return []

    def save_exercise_result_db(self, user_id, exercise_id, results: List[FieldResult]):
        with (session_factory() as session):
            try:
                result = 0
                exercise = session.query(
                    Exercise_structure).filter_by(id=exercise_id).one()
                if not exercise:
                    raise HTTPException(
                        status_code=404, detail="Упражнение не найдено!")

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

                calculator_service.check_number_responses(
                    len(results), field_cnt)
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
                        completed_exercise_id=completed_exercise_id,
                        exercises=field.exercises if field.exercises is not None else []
                    )
                    filled_fields.append(filled_field)
                    session.add(filled_field)

                linked_exercise = session.query(Exercise_structure).filter_by(
                    linked_exercise_id=exercise.id).first()
                if linked_exercise:
                    # Проверяем, выполнял ли текущий пользователь это упражнение ранее
                    has_completed = session.query(Сompleted_exercise).filter(
                        (Сompleted_exercise.exercise_structure_id == linked_exercise.id) &
                        (Сompleted_exercise.user_id == user_id)
                    ).first()
                    # Если пользователь еще не выполнял это упражнение, разблокируем его
                    if not has_completed:
                        linked_exercise.closed = False
                        session.add(linked_exercise)

                session.commit()
                return {
                    "exercise_result_id": completed_exercise_id
                }

            except NoResultFound:
                raise HTTPException(
                    status_code=404, detail="Упражнение или поле не были найдены!")
            except (Exception, Error) as error:
                raise error

    def get_exercise_results(self, exercise_id, user_id):
        with session_factory() as session:
            try:
                exercise_results = session.query(
                    Сompleted_exercise.id.label('completed_exercise_id'),
                    Сompleted_exercise.date,
                    Exercise_structure.title
                ).join(
                    Exercise_structure, Exercise_structure.id == Сompleted_exercise.exercise_structure_id
                ).filter(
                    (Сompleted_exercise.exercise_structure_id == exercise_id) & (
                        Сompleted_exercise.user_id == user_id)
                ).all()
                results_list = []

                for exercise_result in exercise_results:
                    result_dict = {
                        "title": exercise_result.title,
                        "completed_exercise_id": exercise_result.completed_exercise_id,
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
                    raise HTTPException(
                        status_code=404, detail="Такое упражнение не найдено!")

                if str(user_id) != str(exercise_results.user_id):
                    raise HTTPException(
                        status_code=401, detail="Вы не имеете доступ к чужим упражнениям!")

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
                        "value": filled_field.text,
                        "exercises": filled_field.exercises if filled_field.exercises else []  # Добавляем поле exercises
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
                    raise HTTPException(
                        status_code=404, detail="Такое упражнение не найдено!")

                if str(user_id) != str(exercise_results.user_id):
                    raise HTTPException(
                        status_code=401, detail="Вы не имеете доступ к чужим упражнениям!")

                completed_exercise = session.query(Сompleted_exercise).filter_by(
                    id=completed_exercise_id).one_or_none()
                session.delete(completed_exercise)
                session.commit()
            except (Exception, Error) as error:
                print(error)

    def edit_exercise_result(self, completed_exercise_id, results, user_id):

        with session_factory() as session:
            try:
                completed_exercise = session.query(
                    Сompleted_exercise).get(completed_exercise_id)
                if completed_exercise is None:
                    raise HTTPException(
                        status_code=404, detail="Выполненное упражнение не найдено!")

                if str(user_id) != str(completed_exercise.user_id):
                    raise HTTPException(
                        status_code=401, detail="Вы не имеете доступ к чужим упражнениям!")

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
