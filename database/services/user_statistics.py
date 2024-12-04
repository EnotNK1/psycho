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
from database.models.review import *

from database.database import engine, session_factory
from database.calculator import calculator_service
from database.enum import DiaryType
from fastapi.responses import FileResponse
import uuid
from openpyxl import load_workbook
import pandas as pd


class UserStatisticsServicedb:
    def general_test_results(self, psychologist_id: uuid.UUID):
        with session_factory() as session:
            try:

                df = pd.DataFrame()
                excel_file = 'users.xlsx'
                df.to_excel(excel_file, index=False)

                fn = "users.xlsx"
                wb = load_workbook(fn)

                wb.create_sheet("выгорание")
                ws = wb["выгорание"]
                ws.append(["Email", "Эмоциональное истощение", "Деперсонализация", "Редукция проф. достижений", "Дата"])

                wb.create_sheet("DASS-21")
                ws = wb["DASS-21"]
                ws.append(["Email", "Тревога", "Депрессия", "Стресс", "Дата"])

                wb.create_sheet("тревоги")
                ws = wb["тревоги"]
                ws.append(["Email", "Шкала ситуативной тревожности", "Шкала личностной тревожности", "Дата"])

                wb.create_sheet("копинг")
                ws = wb["копинг"]
                ws.append(["Email", "Разрешение проблем", "Поиск социальной поддержки", "Избегание проблем", "Дата"])

                wb.create_sheet("CMQ")
                ws = wb["CMQ"]
                ws.append(["Email", "Шкала когнитивных ошибок", "Персонализация", "Чтение мыслей", "Упрямство",
                           "Морализация", "Катастрофизация", "Выученная беспомощность", "Максимализм",
                           "Преувеличение опасности", "Гипернормативность", "Дата"])


                wb.create_sheet("апатии")
                ws = wb["апатии"]
                ws.append(["Email", "Шкала профессиональной апатии", "Апатичные мысли", "Апатичные действия", "Дата"])

                wb.create_sheet("Бека")
                ws = wb["Бека"]
                ws.append(["Email", "Шкала депрессии", "Когнитивно-аффективная субшкала",
                           "Субшкала соматических проявлений депрессии", "Дата"])

                wb.create_sheet("Самооценка")
                ws = wb["Самооценка"]
                ws.append(["Email", "Шкала воспринимаемого стресса", "Фактор дистресса", "Фактор совладания", "Дата"])

                query = (
                    session.query(Clients)
                    .filter(Clients.psychologist_id == psychologist_id)
                    .join(Users, Clients.client_id == Users.id)
                    .join(Test_result, Test_result.user_id == Users.id)
                    .join(Test, Test_result.test_id == Test.id)
                    .options(
                        joinedload(Users.test_result)
                        .joinedload(Test_result.scale_result)
                        .joinedload(Scale_result.scale_id)
                    )
                )
                res = session.execute(query)
                clients = res.unique().scalars().all()

                for client in clients:
                    user = session.get(Users, client.client_id)

                    for test_result in user.test_result:
                        test = session.get(Test, test_result.test_id)
                        test_title = test.title
                        ws = wb["апатии"]
                        temp = []
                        for scale_result in test_result.scale_result:
                            temp.append(scale_result.score)
                        ws.append([user.email] + temp + [test_result.date.strftime("%d.%m.%Y")])

                wb.save(fn)
                wb.close()

                response = FileResponse(fn,
                                        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                        filename=fn)

                return response

            except Exception as error:
                print(error)


user_statistics_service_db: UserStatisticsServicedb = UserStatisticsServicedb()