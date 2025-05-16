from psycopg2 import Error
from sqlalchemy import create_engine, select, func, distinct
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, join, DeclarativeBase

from schemas.education_material import ResponceMaterial, ResponceGetAllMaterial, SubtopicResponse, CardResponse
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

from database.database import engine, session_factory
from database.calculator import calculator_service
from database.enum import DiaryType
from fastapi import FastAPI, HTTPException
import uuid
from datetime import datetime


class EducationServiceDB:
    def filling_in_links(self, education_theme):
        with session_factory() as session:
            try:

                links = [
                    "/education/images_education_material/img_2.png", "/education/images_education_material/img_3.png",
                    "/education/images_education_material/img_4.png", "/education/images_education_material/img_5.png",
                    "/education/images_education_material/img_6.png", "/education/images_education_material/img_7.png",
                    "/education/images_education_material/img_7.png", "/education/images_education_material/img_8.png",
                    "/education/images_education_material/img_9.png", "/education/images_education_material/img_10.png"
                ]
                i = 0
                for theme in education_theme:
                    theme.link = links[i]
                    i += 1


            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_education_theme_db(self, user_id):
        with session_factory() as session:
            try:
                query = select(Educational_theme).options(selectinload(Educational_theme.educational_material).
                                                          selectinload(Educational_material.educational_progress))
                result = session.execute(query)
                education_theme = result.scalars().all()
                education_service_db.filling_in_links(education_theme)
                user_list = []
                user_dict = {}
                user_id = uuid.UUID(user_id)
                for temp in education_theme:

                    score = 0
                    for education_material in temp.educational_material:
                        if len(education_material.educational_progress) != 0:
                            for educational_progress in education_material.educational_progress:
                                if educational_progress.user_id == user_id:
                                    score += 1

                    user_dict['id'] = temp.id
                    user_dict['theme'] = temp.theme
                    user_dict['score'] = score
                    user_dict['max_score'] = sum(len(material.card) for material in temp.educational_material)
                    user_dict['link_to_picture'] = temp.link
                    user_list.append(user_dict)
                    user_dict = {}
                return user_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_education_material_db(self, education_theme_id, user_id):
        with session_factory() as session:
            try:
                # 1. Проверка UUID
                try:
                    theme_uuid = uuid.UUID(str(education_theme_id))
                except (ValueError, AttributeError) as e:
                    print(f"Invalid UUID format: {e}")
                    return -1

                # 2. Проверка существования темы
                theme = session.get(Educational_theme, theme_uuid)
                if not theme:
                    print(f"Theme {theme_uuid} not found in DB")
                    return -1

                # 3. Загрузка всех подтем (Educational_material) с их карточками, сортируем по number
                materials = (
                    session.query(Educational_material)
                    .filter_by(educational_theme_id=theme_uuid)
                    .options(
                        selectinload(Educational_material.card)  # Жадная загрузка карточек
                    )
                    .order_by(Educational_material.number)  # Сортируем подтемы по number
                    .all()
                )

                # 4. Формирование ответа
                response = {
                    "theme": theme.theme,
                    "id": str(theme.id),
                    "max_score": sum(len(m.card) for m in materials),
                    "link_to_picture": theme.link or "",
                    "related_topics": [],
                    "subtopics": []
                }

                # 5. Обработка подтем и их карточек
                for material in materials:
                    # Сортируем карточки внутри подтемы по number
                    sorted_cards = sorted(material.card, key=lambda c: c.number if c.number is not None else 0)

                    subtopic = {
                        "subtitle": material.subtitle or "",
                        "number": material.number,  # Добавляем номер подтемы (если нужно)
                        "cards": [
                            {
                                "id": str(card.id),
                                "number": card.number,  # Добавляем номер карточки (если нужно)
                                "text": card.text,
                                "link_to_picture": card.link_to_picture or ""
                            }
                            for card in sorted_cards
                        ]
                    }
                    response["subtopics"].append(subtopic)

                # 6. Обработка связанных тем (если есть)
                if theme.related_topics:
                    for related_id in theme.related_topics:
                        try:
                            related_theme = session.get(Educational_theme, uuid.UUID(related_id))
                            if related_theme:
                                response["related_topics"].append({
                                    "id": str(related_theme.id),
                                    "theme": related_theme.theme,
                                    "link_to_picture": related_theme.link or "",
                                    "max_score": sum(len(m.card) for m in related_theme.educational_material)
                                })
                        except:
                            continue

                return response

            except Exception as e:
                print(f"Critical error: {str(e)}")
                return -1

    def complete_education_material_db(self, edu_id, user_id):
        with session_factory() as session:
            material = session.query(Educational_theme).get(edu_id)
            if not material:
                raise HTTPException(status_code=404, detail="Материал не найден!")

            # temp = session.query(Educational_progress).filter_by(
            #     user_id=user_id, educational_material_id=edu_id).first()


            # if not temp:
                # education_progress = Educational_progress(
                #     id=uuid.uuid4(),
                #     user_id=user_id,
                #     educational_material_id=edu_id
                # )
                # session.add(education_progress)
                # session.commit()
            dic = {
                "status": "ok"
            }
            return dic
            # else:
            #     raise HTTPException(status_code=409, detail="Данный материал уже пройден!")

    def get_edu_theme_by_edu_material(self, edu_material_id):
        with session_factory() as session:
            stmt = select(Educational_material.educational_theme_id).where(
                Educational_material.id == edu_material_id
            )
            theme_id = session.scalar(stmt)

            if theme_id is None:
                return None

            stmt = select(Educational_theme).where(Educational_theme.id == theme_id)
            theme = session.execute(stmt).scalar_one_or_none()

            return theme.id

    def delete_education_theme_db(self, education_theme_id):
        with session_factory() as session:
            try:
                temp = session.query(Educational_theme).get(education_theme_id)
                session.delete(temp)
                session.commit()
                dic = {}
                dic['status'] = "OK"

                return dic
            except (Exception, Error) as error:
                print(error)
                return -1



education_service_db: EducationServiceDB = EducationServiceDB()
