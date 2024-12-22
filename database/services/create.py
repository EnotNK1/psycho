from psycopg2 import Error
from sqlalchemy import create_engine, select, func, distinct
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, join, DeclarativeBase

from database.models.exercise import Exercise_structure, Field
from schemas.test import ResScale, ReqBorder, ReqScale
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
from database.models.daily_task import *
from database.destination_id_info import destination_id

from database.database import engine, session_factory
from database.calculator import calculator_service
from database.enum import DiaryType
from fastapi import FastAPI, HTTPException
import uuid
from datetime import datetime


class CreateServiceDB:
    def create_inquirty(self):
        with session_factory() as session:
            temp = session.query(Inquiry).all()

            if not temp:
                for i in range(len(inquiries)):
                    inquiry = Inquiry(id=i + 1,
                                      text=inquiries[i]
                                      )
                    session.add(inquiry)

            session.commit()

    def create_type_analysis(self):
        with session_factory() as session:
            temp = session.query(Type_analysis).all()
            if not temp:
                type = ["догматическое требование", "Драматизация", "НПФ", "Гибкое предпочтение", "Унизительные замечание",
                        "Перспектива", "Высокий порог фрустрации", "Безусловное принятие"]
                for i in range(len(type)):
                    tanalys = Type_analysis(id=i + 1,
                                            text=type[i]
                                            )
                    session.add(tanalys)
            session.commit()

    def create_test_db(self, title, description, short_desc, scales: List[ReqScale]):
        with session_factory() as session:
            try:
                test_id = uuid.uuid4()
                test = Test(id=test_id,
                            title=title,
                            description=description,
                            short_desc=short_desc
                            )

                if len(scales) < 1:
                    raise HTTPException(status_code=400, detail="Введите хотя бы одну шкалу!")

                for scale in scales:
                    if scale.min >= scale.max:
                        raise HTTPException(status_code=400, detail="Максимальное значение шкалы должно быть больше минимального!")

                    if scale.min < 0:
                        raise HTTPException(status_code=400, detail="Минимальное значение шкалы должно быть больше нуля!")
                    scale_id = uuid.uuid4()
                    new_scale = Scale(id=scale_id,
                                      title=scale.title,
                                      min=scale.min,
                                      max=scale.max,
                                      test_id=test_id)

                    session.add(new_scale)

                    if len(scale.borders) < 1:
                        raise HTTPException(status_code=400, detail="Введите границы шкал!")

                    sorted_borders = sorted(scale.borders, key=lambda obj: obj.left_border)
                    print(sorted_borders)
                    if sorted_borders[0].left_border != scale.min:
                        raise HTTPException(status_code=400, detail="Левая граница первого интервала должна быть равна минимальному значению шкалы!")

                    if sorted_borders[-1].right_border != scale.max:
                        raise HTTPException(status_code=400, detail="Правая граница последнего интервала должна быть равна максимальному значению шкалы!")

                    for i in range(0, len(sorted_borders)):
                        if i > 0 and (sorted_borders[i].left_border - sorted_borders[i-1].right_border) != 1:
                            raise HTTPException(status_code=400,
                                                detail="Границы интервалов в шкале введены неправильно!")

                        if sorted_borders[i].left_border < 0:
                            raise HTTPException(status_code=400,
                                                detail="Минимальное значение шкалы должно быть больше нуля!")

                        if sorted_borders[i].right_border <= sorted_borders[i].left_border:
                            raise HTTPException(status_code=400,
                                                detail="Правая граница должна быть больше левой!")

                    for border in sorted_borders:
                        border_id = uuid.uuid4()

                        new_border = Borders(id=border_id,
                                             left_border=border.left_border,
                                             right_border=border.right_border,
                                             color=border.color,
                                             title=border.title,
                                             scale_id=scale_id)
                        session.add(new_border)

                session.add(test)
                session.commit()
                return "Successfully!"
            except (Exception, Error) as error:
                raise error

    # def update_test_db(self, test_id,  title, description, short_desc):
    #     with session_factory() as session:
    #         try:
    #             test = session.get(Test, test_id)
    #             test.title = title
    #             test.description = description
    #             test.short_desc = short_desc
    #
    #             session.commit()
    #             return "Successfully!"
    #         except (Exception, Error) as error:
    #             raise error

    def add_test_db(self, test_id, test_info):
        with session_factory() as session:
            try:
                test = Test(
                    id=test_id,
                    title=test_info.title,
                    description=test_info.description,
                    short_desc=test_info.short_desc
                )
                session.add(test)

                for i in range(len(test_info.questions)):
                    question_id = uuid.uuid4()
                    question = Question(
                        id=question_id,
                        text=test_info.questions[i],
                        number=i + 1,
                        test_id=test_id
                    )
                    session.add(question)

                    for j in range(test_info.answers_cnt):
                        answer = Answer_choice(
                            id=uuid.uuid4(),
                            text=test_info.answers[i][j],
                            question_id=question_id,
                            score=test_info.answer_score[i][j]
                        )
                        session.add(answer)

                k = 0
                for i in range(len(test_info.scales)):
                    scale_id = uuid.uuid4()
                    scale = Scale(
                        id=scale_id,
                        test_id=test_id,
                        title=test_info.scales[i],
                        min=test_info.scale_limitation[k],
                        max=test_info.scale_limitation[k + 1],
                    )
                    k += 2
                    session.add(scale)

                    d = 0
                    p = 0
                    for j in range(len(test_info.scale_border[i]) // 2):
                        border = Borders(
                            id=uuid.uuid4(),
                            scale_id=scale_id,
                            left_border=test_info.scale_border[i][p],
                            right_border=test_info.scale_border[i][p + 1],
                            color=test_info.scale_color[i][d],
                            title=test_info.scale_title[i][d],
                            user_recommendation=test_info.user_recommendation[i][d]
                        )
                        p += 2
                        d += 1
                        session.add(border)
                session.commit()


            except (Exception, Error) as error:
                print(error)
                return -1

    def recreate_test(self, test_id, test_info):
        with session_factory() as session:
            try:
                query = (
                    session.query(Test)
                    .filter(Test.id == test_id)
                    .options(
                        selectinload(Test.question).selectinload(Question.answer_choice),
                        selectinload(Test.scale).selectinload(Scale.borders)
                    )
                )
                test = query.one_or_none()

                test.title = test_info.title
                test.description = test_info.description
                test.short_desc = test_info.short_desc

                i = 0
                for question in test.question:
                    question.text = test_info.questions[i]
                    question.number = i + 1

                    j = 0
                    for answer in question.answer_choice:
                        answer.text = test_info.answers[i][j]
                        answer.score = test_info.answer_score[i][j]
                        j += 1
                    i += 1

                k = 0
                i = 0
                for scale in test.scale:
                    scale.title = test_info.scales[i]
                    scale.min = test_info.scale_limitation[k]
                    scale.max = test_info.scale_limitation[k + 1]

                    k += 2

                    d = 0
                    p = 0
                    for border in scale.borders:
                        border.left_border = test_info.scale_border[i][p]
                        border.right_border = test_info.scale_border[i][p + 1]
                        border.color = test_info.scale_color[i][d]
                        border.title = test_info.scale_title[i][d]
                        border.user_recommendation = test_info.user_recommendation[i][d]

                        p += 2
                        d += 1
                    i += 1

                session.commit()


            except (Exception, Error) as error:
                print(error)
                return -1

    def create_test(self, test_info):
        with session_factory() as session:
            try:
                temp = session.query(Test).filter_by(description=test_info.description).first()
                if not temp:
                    test_id = uuid.uuid4()
                    create_service_db.add_test_db(test_id, test_info)
                else:
                    create_service_db.recreate_test(temp.id, test_info)

                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def create_education(self, edu_info):
        with session_factory() as session:
            try:
                temp = session.query(Educational_theme).filter_by(theme=edu_info.theme).first()
                if not temp:
                    edu_id = uuid.uuid4()
                    create_service_db.add_education_db(edu_id, edu_info)
                else:
                    create_service_db.recreate_education_db(temp.id, edu_info)

                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def add_education_db(self, edu_id, edu_info):
        with session_factory() as session:
            try:
                education = Educational_theme(
                    id=edu_id,
                    theme=edu_info.theme,
                    link=edu_info.link
                )
                session.add(education)
                for i in range(len(edu_info.text)):
                    education_material_id = uuid.uuid4()
                    education_material = Educational_material(
                        id=education_material_id,
                        text=edu_info.text[i],
                        title=edu_info.title,
                        type=edu_info.type,
                        educational_theme_id=edu_id
                    )
                    session.add(education_material)
                session.commit()


            except (Exception, Error) as error:
                print(error)
                return -1

    def recreate_education_db(self, edu_id, edu_info):
        with session_factory() as session:
            try:
                query = (
                    session.query(Educational_theme)
                    .filter(Educational_theme.id == edu_id)
                    .options(
                        selectinload(Educational_theme.educational_material)
                    )
                )
                education = query.one_or_none()

                education.theme = edu_info.theme
                education.link = edu_info.link

                i = 0
                for educational_material in education.educational_material:
                    educational_material.text = edu_info.text[i]
                    educational_material.title = edu_info.title
                    educational_material.type = edu_info.type
                    i += 1

                session.commit()


            except (Exception, Error) as error:
                print(error)
                return -1

    def create_exercise_structure(self, exercise_info):
        with session_factory() as session:
            try:
                temp = session.query(Exercise_structure).filter_by(title=exercise_info.title).first()
                if not temp:
                    exercise_id = uuid.uuid4()
                    create_service_db.add_exercise_structure(exercise_id, exercise_info)
                else:
                    create_service_db.recreate_exercise_structure(temp.id, exercise_info)

                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def add_exercise_structure(self, exercise_structure_id, exercise_info):
        with session_factory() as session:
            try:
                exercise_structure = Exercise_structure(
                    id=exercise_structure_id,
                    title=exercise_info.title,
                    description=exercise_info.description,
                    picture_link=exercise_info.picture_link
                )
                session.add(exercise_structure)

                for temp_field in exercise_info.fields:
                    field = Field(
                        id=uuid.uuid4(),
                        title=temp_field['title'],
                        description=temp_field['description'],
                        type=temp_field['type'],
                        major=temp_field['major'],
                        exercise_structure_id=exercise_structure_id
                    )
                    session.add(field)
                session.commit()

            except (Exception, Error) as error:
                print(error)
                return -1

    def recreate_exercise_structure(self, exercise_structure_id, exercise_info):
        with session_factory() as session:
            try:
                query = (
                    session.query(Exercise_structure)
                    .filter(Exercise_structure.id == exercise_structure_id)
                    .options(
                        selectinload(Exercise_structure.field)
                    )
                )
                exercise_structure = query.one_or_none()

                exercise_structure.description = exercise_info.description
                exercise_structure.picture_link = exercise_info.picture_link

                i = 0
                for temp_field in exercise_structure.field:

                    temp_field.title=exercise_info.fields[i]['title']
                    temp_field.description=exercise_info.fields[i]['description']
                    temp_field.type=exercise_info.fields[i]['type']
                    temp_field.major=exercise_info.fields[i]['major']
                    i += 1

                session.commit()

            except (Exception, Error) as error:
                print(error)
                return -1

# :)
    def get_destination_id_for_daily_task(self):
        with session_factory() as session:
            try:
                test = session.query(Test).all()
                exercise = session.query(Exercise_structure).all()
                education = session.query(Educational_theme).all()
                destination_id.clear()

                for temp in education:
                    if temp.theme == "Дыхательные техники":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Изучите основы дыхательных техник для снятия стресса и "
                                                          "улучшения самочувствия",
                                     "destination_id": temp.id,
                                     "number": 1, "day": 1}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "Трекер настроения":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.MOOD_TRACKER_AND_FREE_DIARY.name,
                                     "short_description": "Запишите свои эмоции сегодня, чтобы отслеживать изменения"
                                                          " в настроении",
                                     "destination_id": temp.id,
                                     "number": 2, "day": 1}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Основы КПТ":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Ознакомьтесь с ключевыми принципами когнитивно-поведенческой"
                                                          " терапии для изменения мышления",
                                     "destination_id": temp.id,
                                     "number": 3, "day": 1}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "Трекер настроения":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.MOOD_TRACKER_AND_FREE_DIARY.name,
                                     "short_description": "Запишите свои эмоции сегодня, чтобы отслеживать изменения"
                                                          " в настроении",
                                     "destination_id": temp.id,
                                     "number": 4, "day": 2}
                        destination_id.append(temp_dict)
                for temp in test:
                    if temp.title == "DASS-21":
                        temp_dict = {"title": temp.title, "type": DailyTaskType.TEST.name, "short_description": "Шкалы депрессии, "
                                                                                          "тревоги и стресса",
                                     "destination_id": temp.id,
                                     "number": 5, "day": 2}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Техники релаксации":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Узнайте о различных методах релаксации для "
                                                          "восстановления внутреннего баланса",
                                     "destination_id": temp.id,
                                     "number": 6, "day": 2}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "Трекер настроения":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.MOOD_TRACKER_AND_FREE_DIARY.name,
                                     "short_description": "Запишите свои эмоции сегодня, чтобы "
                                                          "отслеживать изменения в настроении",
                                     "destination_id": temp.id,
                                     "number": 7, "day": 3}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "КПТ-дневник":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Ведите дневник для анализа мыслей и поведения с "
                                                          "целью улучшения психологического состояния.",
                                     "destination_id": temp.id,
                                     "number": 8, "day": 3}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "КПТ-дневник":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.OTHER.name,
                                     "short_description": "Ведите дневник для анализа мыслей и поведения с целью "
                                                          "улучшения психологического состояния",
                                     "destination_id": temp.id,
                                     "number": 9, "day": 3}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Техники релаксации":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Узнайте о различных методах релаксации для восстановления"
                                                          " внутреннего баланса",
                                     "destination_id": temp.id,
                                     "number": 10, "day": 3}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "Трекер настроения":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.MOOD_TRACKER_AND_FREE_DIARY.name,
                                     "short_description": "Запишите свои эмоции сегодня, чтобы отслеживать "
                                                          "изменения в настроении",
                                     "destination_id": temp.id,
                                     "number": 11, "day": 4}
                        destination_id.append(temp_dict)
                for temp in test:
                    if temp.title == "Индикатор копинг-стратегий":
                        temp_dict = {"title": temp.title, "type": DailyTaskType.TEST.name,
                                     "short_description": "Опросник Индикатор копинг-стратегий",
                                     "destination_id": temp.id,
                                     "number": 12, "day": 4}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Копинг стратегии":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Изучите стратегии преодоления стресса, чтобы уверенно  "
                                                          "справляться с трудными ситуациями",
                                     "destination_id": temp.id,
                                     "number": 13, "day": 4}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Техники релаксации":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Узнайте о различных методах релаксации для восстановления "
                                                          "внутреннего баланса.",
                                     "destination_id": temp.id,
                                     "number": 14, "day": 4}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "Трекер настроения":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.MOOD_TRACKER_AND_FREE_DIARY.name,
                                     "short_description": "Запишите свои эмоции сегодня, чтобы отслеживать "
                                                          "изменения в настроении",
                                     "destination_id": temp.id,
                                     "number": 15, "day": 5}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "КПТ-дневник":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.OTHER.name,
                                     "short_description": "Ведите дневник для анализа мыслей и поведения с "
                                                          "целью улучшения психологического состояния",
                                     "destination_id": temp.id,
                                     "number": 16, "day": 5}
                        destination_id.append(temp_dict)
                for temp in test:
                    if temp.title == "Профессиональное выгорание":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.TEST.name,
                                     "short_description": "Опросник профессионального выгорания Маслач MBI/ПВ",
                                     "destination_id": temp.id,
                                     "number": 17, "day": 5}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Выгорание":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Понимание причин и признаков выгорания поможет "
                                                          "предотвратить его и сохранить баланс в жизни",
                                     "destination_id": temp.id,
                                     "number": 18, "day": 5}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "Трекер настроения":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.MOOD_TRACKER_AND_FREE_DIARY.name,
                                     "short_description": "Запишите свои эмоции сегодня, "
                                                          "чтобы отслеживать изменения в настроении",
                                     "destination_id": temp.id,
                                     "number": 19, "day": 6}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "КПТ-дневник":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.OTHER.name,
                                     "short_description": "Ведите дневник для анализа мыслей и поведения с целью"
                                                          " улучшения психологического состояния",
                                     "destination_id": temp.id,
                                     "number": 20, "day": 6}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Техники релаксации":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Узнайте о различных методах релаксации для "
                                                          "восстановления внутреннего баланса",
                                     "destination_id": temp.id,
                                     "number": 21, "day": 6}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "Трекер настроения":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.MOOD_TRACKER_AND_FREE_DIARY.name,
                                     "short_description": "Запишите свои эмоции сегодня, чтобы отслеживать "
                                                          "изменения в настроении",
                                     "destination_id": temp.id,
                                     "number": 22, "day": 7}
                        destination_id.append(temp_dict)
                for temp in test:
                    if temp.title == "DASS-21":
                        temp_dict = {"title": temp.title, "type": DailyTaskType.TEST.name,
                                     "short_description": "Шкалы депрессии, тревоги и стресса",
                                     "destination_id": temp.id,
                                     "number": 23, "day": 7}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Техники релаксации":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Узнайте о различных методах релаксации "
                                                          "для восстановления внутреннего баланса",
                                     "destination_id": temp.id,
                                     "number": 24, "day": 7}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "Трекер настроения":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.MOOD_TRACKER_AND_FREE_DIARY.name,
                                     "short_description": "Запишите свои эмоции сегодня, чтобы отслеживать "
                                                          "изменения в настроении",
                                     "destination_id": temp.id,
                                     "number": 25, "day": 8}
                        destination_id.append(temp_dict)
                for temp in exercise:
                    if temp.title == "КПТ-дневник":
                        temp_dict = {"title": temp.title,
                                     "type": DailyTaskType.OTHER.name,
                                     "short_description": "Ведите дневник для анализа мыслей и поведения с целью "
                                                          "улучшения психологического состояния",
                                     "destination_id": temp.id,
                                     "number": 26, "day": 8}
                        destination_id.append(temp_dict)
                for temp in education:
                    if temp.theme == "Техники релаксации":
                        temp_dict = {"title": temp.theme,
                                     "type": DailyTaskType.THEORY.name,
                                     "short_description": "Узнайте о различных методах релаксации для восстановления"
                                                          " внутреннего баланса",
                                     "destination_id": temp.id,
                                     "number": 27, "day": 8}
                        destination_id.append(temp_dict)

            except (Exception, Error) as error:
                print(error)
                return -1

    def add_daily_task(self, user_id):
        with session_factory() as session:
            try:

                user = session.get(Users, user_id)
                if not user.daily_tasks:
                    create_service_db.get_destination_id_for_daily_task()

                    for i in range(len(destination_id)):
                        is_current = False
                        if i in [0, 1, 2]:
                            is_current = True
                        daily_task = Daily_task(
                            id=uuid.uuid4(),
                            title=destination_id[i]["title"],
                            short_desc=destination_id[i]["short_description"],
                            destination_id=destination_id[i]["destination_id"],
                            number=destination_id[i]["number"],
                            day=destination_id[i]["day"],
                            is_complete=False,
                            is_current=is_current,
                            type=destination_id[i]["type"],
                            user_id=user_id
                        )
                        session.add(daily_task)
                    session.commit()

            except (Exception, Error) as error:
                print(error)
                return -1

    def create_daily_task(self):
        with session_factory() as session:
            try:

                users = session.query(Users).all()
                for user in users:
                    create_service_db.add_daily_task(user.id)

            except (Exception, Error) as error:
                print(error)
                return -1




create_service_db: CreateServiceDB = CreateServiceDB()