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
                # Проверяем корректность UUID
                try:
                    theme_uuid = uuid.UUID(education_theme_id)
                except ValueError:
                    print(f"Invalid UUID format: {education_theme_id}")
                    return -1

                # Получаем тему с материалами
                query = (
                    select(Educational_theme)
                    .filter_by(id=theme_uuid)
                    .options(
                        selectinload(Educational_theme.educational_material)
                        .selectinload(Educational_material.card),
                        selectinload(Educational_theme.educational_material)
                        .selectinload(Educational_material.educational_progress),
                    )
                )

                try:
                    education_theme = session.execute(query).scalars().one()
                except NoResultFound:
                    print(f"Theme not found: {education_theme_id}")
                    return -1
                except Exception as e:
                    print(f"Database error: {str(e)}")
                    return -1

                # Логирование для отладки
                print(f"Found theme: {education_theme.theme}")
                print(f"Materials count: {len(education_theme.educational_material)}")

                # Сортируем материалы по number
                try:
                    sorted_materials = sorted(
                        education_theme.educational_material,
                        key=lambda m: m.number
                    )
                    print("Materials sorted successfully")
                except Exception as e:
                    print(f"Sorting error: {str(e)}")
                    return -1

                # Собираем связанные темы
                related_topics_ = []
                if education_theme.related_topics:
                    for related_topic_id in education_theme.related_topics:
                        try:
                            topic_uuid = uuid.UUID(related_topic_id)
                            query = select(Educational_theme).filter_by(id=topic_uuid)
                            result = session.execute(query)
                            education_theme_rel = result.scalars().one()

                            # Получаем изображение для связанной темы
                            link_to_picture = None
                            if education_theme_rel.educational_material:
                                sorted_rel_materials = sorted(
                                    education_theme_rel.educational_material,
                                    key=lambda m: m.number
                                )
                                if sorted_rel_materials and sorted_rel_materials[0].card:
                                    sorted_rel_cards = sorted(
                                        sorted_rel_materials[0].card,
                                        key=lambda c: c.number
                                    )
                                    if sorted_rel_cards:
                                        link_to_picture = sorted_rel_cards[0].link_to_picture

                            topic = ResponceMaterial(
                                id=education_theme_rel.id,
                                theme=education_theme_rel.theme,
                                link_to_picture=link_to_picture,
                                max_score=sum(
                                    len(material.card) for material in education_theme_rel.educational_material)
                            )
                            related_topics_.append(topic)
                        except Exception as e:
                            print(f"Error processing related topic {related_topic_id}: {str(e)}")
                            continue

                # Формируем подтемы
                subtopics = []
                for material in sorted_materials:
                    try:
                        # Сортируем карточки
                        sorted_cards = sorted(
                            material.card,
                            key=lambda c: c.number
                        )

                        cards = [
                            CardResponse(
                                id=card.id,
                                text=card.text,
                                link_to_picture=card.link_to_picture
                            )
                            for card in sorted_cards
                        ]

                        subtopics.append(SubtopicResponse(
                            subtitle=material.subtitle,
                            cards=cards
                        ))
                    except Exception as e:
                        print(f"Error processing material {material.id}: {str(e)}")
                        continue

                # Получаем основное изображение
                main_link_to_picture = None
                if education_theme.educational_material and sorted_materials:
                    first_material = sorted_materials[0]
                    if first_material.card:
                        sorted_cards = sorted(
                            first_material.card,
                            key=lambda c: c.number
                        )
                        if sorted_cards:
                            main_link_to_picture = sorted_cards[0].link_to_picture

                # Формируем ответ
                response = ResponceGetAllMaterial(
                    theme=education_theme.theme,
                    id=str(education_theme.id),
                    link_to_picture=main_link_to_picture or education_theme.link_to_picture,
                    max_score=sum(len(material.card) for material in education_theme.educational_material),
                    related_topics=related_topics_,
                    subtopics=subtopics
                )

                return response

            except Exception as error:
                print(f"Critical error in get_all_education_material_db: {str(error)}", exc_info=True)
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
