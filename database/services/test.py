from psycopg2 import Error
from sqlalchemy import create_engine, select, func, distinct
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, join, DeclarativeBase
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


class TestServiceDB:

    def get_test_res_db(self, user_id, test_id):
        with session_factory() as session:
            try:
                query = select(Test_result).filter_by(user_id=user_id, test_id=test_id).options(
                    selectinload(Test_result.scale_result))
                res = session.execute(query)
                test_results = res.unique().scalars().all()

                results_list = []
                for test_result in test_results:
                    result_dict = {
                        "test_id": test_result.test_id,
                        "test_result_id": test_result.id,
                        "datetime": test_result.date,
                    }

                    scale_results = []

                    for scale_result in test_result.scale_result:
                        query = select(Scale).filter_by(id=scale_result.scale_id).options(
                            selectinload(Scale.borders))
                        res = session.execute(query)
                        scale = res.unique().scalars().all()
                        for scal in scale:
                            for border in scal.borders:
                                if scale_result.score >= border.left_border and scale_result.score <= border.right_border:

                                    new_scale_result = {
                                        "scale_id": scale_result.scale_id,
                                        "scale_title": scal.title,
                                        "score": scale_result.score,
                                        "max_score": scal.max,
                                        "conclusion": border.title,
                                        "color": border.color,
                                        "user_recommendation": border.user_recommendation
                                    }
                                    scale_results.append(new_scale_result)

                    result_dict["scale_results"] = scale_results
                    results_list.append(result_dict)

                return results_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_test_result_db(self, test_result_id, user_id):
        with session_factory() as session:
            try:
                query = select(Test_result).filter_by(id=test_result_id).options(
                    selectinload(Test_result.scale_result))
                res = session.execute(query)
                test_result = res.unique().scalars().one()

                result_dict = {
                    "user_id": test_result.user_id,
                    "test_id": test_result.test_id,
                    "test_result_id": test_result.id,
                    "datetime": test_result.date,
                }

                scale_results = []

                for scale_result in test_result.scale_result:
                    query = select(Scale).filter_by(id=scale_result.scale_id).options(
                        selectinload(Scale.borders))
                    res = session.execute(query)
                    scale = res.unique().scalars().all()
                    for scal in scale:
                        for border in scal.borders:
                            if scale_result.score >= border.left_border and scale_result.score <= border.right_border:

                                if test_result.user_id == user_id:
                                    user_recommendation = border.user_recommendation
                                else:
                                    user_recommendation = ""

                                new_scale_result = {
                                    "scale_id": scale_result.scale_id,
                                    "scale_title": scal.title,
                                    "score": scale_result.score,
                                    "max_score": scal.max,
                                    "conclusion": border.title,
                                    "color": border.color,
                                    "user_recommendation": user_recommendation
                                }
                                scale_results.append(new_scale_result)

                result_dict["scale_results"] = scale_results

                return result_dict

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_passed_tests_db(self, user_id):
        with session_factory() as session:
            try:
                query = (
                    select(Test)
                    .join(Test_result, Test.id == Test_result.test_id)
                    .filter(Test_result.user_id == user_id)
                )
                res = session.execute(query)
                users = res.unique().scalars().all()

                user_list = []
                user_dict = {}
                for user in users:
                    user_dict['title'] = user.title
                    user_dict['description'] = user.description
                    user_dict['test_id'] = user.id

                    user_list.append(user_dict)
                    user_dict = {}
                return user_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_tests_db(self):
        with session_factory() as session:
            try:
                query = select(Test)
                result = session.execute(query)
                users = result.scalars().all()

                user_list = []
                user_dict = {}
                for user in users:
                    user_dict['title'] = user.title
                    user_dict['description'] = user.description
                    user_dict['short_desc'] = user.short_desc
                    user_dict['test_id'] = user.id

                    user_list.append(user_dict)
                    user_dict = {}
                return user_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_test_info(self, test_id):
        with session_factory() as session:
            try:
                test = session.query(Test).filter_by(id=test_id).one()
                result = {
                    "test_id": test.id,
                    "title": test.title,
                    "description": test.description,
                    "short_desc": test.short_desc
                }

                scales = session.query(Scale).filter_by(test_id=test_id)
                list_scales = []

                for scale in scales:
                    new_scale = {
                        "scale_id": scale.id,
                        "title": scale.title,
                        "min": scale.min,
                        "max": scale.max
                    }

                    list_borders = []
                    borders = session.query(Borders).filter_by(scale_id=scale.id)

                    for border in borders:
                        new_border = {
                            "border_id": border.id,
                            "left_border": border.left_border,
                            "right_border": border.right_border,
                            "color": border.color,
                            "title": border.title
                        }

                        list_borders.append(new_border)

                    new_scale["borders"] = list_borders
                    list_scales.append(new_scale)

                result["scales"] = list_scales
                return result

            except (Exception, Error) as error:
                print(error)
                raise HTTPException(status_code=404, detail="Такой тест не найден!")

    def save_test_result_db(self, user_id, test_id, date, results: List[int]):
        with (session_factory() as session):
            try:
                result = 0
                test = session.query(Test).filter_by(id=test_id).one()
                if not test:
                    raise HTTPException(status_code=404, detail="Тест не найден!")

                if test.title == "Профессиональное выгорание":
                    answers_cnt = 22
                    scale_title = ["Эмоциональное истощение", "Деперсонализация", "Редукция проф. достижений"]
                    calculator_service.check_number_responses(len(results), answers_cnt)
                    scale_sum_list = calculator_service.test_maslach_calculate_results(results)
                    result = test_service_db.save_test_res_all_db(test_id, user_id, date, scale_title, scale_sum_list)
                elif test.title == "Шкала профессиональной апатии":
                    answers_cnt = 10
                    scale_title = ["Шкала профессиональной апатии", "Апатичные мысли", "Апатичные действия"]
                    calculator_service.check_number_responses(len(results), answers_cnt)
                    scale_sum_list = calculator_service.test_jas_calculate_results(results)
                    result = test_service_db.save_test_res_all_db(test_id, user_id, date, scale_title, scale_sum_list)
                elif test.title == "DASS-21":
                    answers_cnt = 21
                    scale_title = ["Тревога", "Депрессия", "Стресс"]
                    calculator_service.check_number_responses(len(results), answers_cnt)
                    scale_sum_list = calculator_service.test_dass21_calculate_results(results)
                    result = test_service_db.save_test_res_all_db(test_id, user_id, date, scale_title, scale_sum_list)
                elif test.title == "Шкала тревоги Спилбергера-Ханина, STAI":
                    answers_cnt = 40
                    scale_title = ["Шкала ситуативной тревожности", "Шкала личностной тревожности"]
                    calculator_service.check_number_responses(len(results), answers_cnt)
                    scale_sum_list = calculator_service.test_stai_calculate_results(results)
                    result = test_service_db.save_test_res_all_db(test_id, user_id, date, scale_title, scale_sum_list)
                elif test.title == "Опросник когнтитвных ошибок CMQ":
                    answers_cnt = 45
                    scale_title = ["Шкала когнитивных ошибок", "Персонализация", "Чтение мыслей", "Упрямство", "Морализация", "Катастрофизация",
                                   "Выученная беспомощность", "Максимализм", "Преувеличение опасности",
                                   "Гипернормативность"]
                    calculator_service.check_number_responses(len(results), answers_cnt)
                    scale_sum_list = calculator_service.test_cmq_calculate_results(results)
                    result = test_service_db.save_test_res_all_db(test_id, user_id, date, scale_title, scale_sum_list)
                elif test.title == "Индикатор копинг-стратегий":
                    answers_cnt = 33
                    scale_title = ["Разрешение проблем", "Поиск социальной поддержки", "Избегание проблем"]
                    calculator_service.check_number_responses(len(results), answers_cnt)
                    scale_sum_list = calculator_service.test_coling_calculate_results(results)
                    result = test_service_db.save_test_res_all_db(test_id, user_id, date, scale_title, scale_sum_list)
                elif test.title == "Шкала депрессии Бека":
                    answers_cnt = 21
                    scale_title = ["Шкала депрессии", "Когнитивно-аффективная субшкала", "Субшкала соматических проявлений депрессии"]
                    calculator_service.check_number_responses(len(results), answers_cnt)
                    scale_sum_list = calculator_service.test_back_calculate_results(results)
                    result = test_service_db.save_test_res_all_db(test_id, user_id, date, scale_title, scale_sum_list)
                elif test.title == "Самооценка стрессоустойчивости Коухена-Виллиансона":
                    answers_cnt = 10
                    scale_title = ["Шкала воспринимаемого стресса", "Фактор дистресса", "Фактор совладания"]
                    calculator_service.check_number_responses(len(results), answers_cnt)
                    scale_sum_list = calculator_service.test_stress_calculate_results(results)
                    result = test_service_db.save_test_res_all_db(test_id, user_id, date, scale_title, scale_sum_list)


                return result

            except NoResultFound:
                raise HTTPException(status_code=404, detail="Тест или шкалы не были найдены!")
            except (Exception, Error) as error:
                raise error

    def save_test_res_all_db(self, test_id, user_id, date, scale_title: List[str], scale_sum_list: List[int]):
        with session_factory() as session:
            try:
                result = []
                dic = {}
                temp = {}

                test_res_id = uuid.uuid4()
                test_res = Test_result(id=test_res_id,
                                       user_id=user_id,
                                       test_id=test_id,
                                       date=date)
                session.add(test_res)

                scale_info = session.query(Scale).filter_by(test_id=test_id).all()
                dic["test_result_id"] = test_res_id
                for scale in scale_info:
                    borders = session.query(Borders).filter_by(scale_id=scale.id).all()
                    i = scale_title.index(scale.title)

                    if scale_sum_list[i] < scale.min or scale_sum_list[i] > scale.max:
                        raise HTTPException(status_code=400,
                                            detail="Результат не может быть меньше или больше границ шкалы!")
                    scale_result = Scale_result(id=uuid.uuid4(),
                                                score=scale_sum_list[i],
                                                scale_id=scale.id,
                                                test_result_id=test_res_id)

                    for bord in borders:
                        if scale_sum_list[i] >= bord.left_border and scale_sum_list[i] <= bord.right_border:
                            color = bord.color
                            conclusion = bord.title
                            user_recommendation = bord.user_recommendation
                            break


                    temp["scale_id"] = scale.id
                    temp["scale_title"] = scale.title
                    temp["score"] = scale_sum_list[i]
                    temp["conclusion"] = conclusion
                    temp["color"] = color
                    temp["user_recommendation"] = user_recommendation
                    result.append(temp)
                    temp = {}
                    session.add(scale_result)
                dic["result"] = result

                session.commit()
                return dic


            except (Exception, Error) as error:
                raise error

    def get_test_questions_db(self, test_id):
        with session_factory() as session:
            try:
                list = []
                dic = {}
                temp = session.query(Question).filter_by(test_id=test_id).all()
                if temp == []:
                    return "тест не найден"

                answer = session.query(Answer_choice).all()

                for obj in temp:
                    answer_options = []
                    for ans in answer:
                        if obj.id == ans.question_id:
                            answer_options.append({"id": ans.id, "text": ans.text, "score": ans.score})

                    dic["number"] = obj.number
                    dic["text"] = obj.text
                    dic["answer_options"] = answer_options

                    list.append(dic)
                    dic = {}

                list.sort(key=lambda x: x['number'])
                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def delete_test_db(self, test_id):
        with session_factory() as session:
            try:
                temp = session.query(Test).get(test_id)
                session.delete(temp)
                session.commit()
                dic = {}
                dic['status'] = "OK"

                return dic
            except (Exception, Error) as error:
                print(error)
                return -1


test_service_db: TestServiceDB = TestServiceDB()