from psycopg2 import Error
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker, joinedload, selectinload, join
from schemas.test import ResScale, ReqBorder, ReqScale
from typing import List
from sqlalchemy.exc import NoResultFound

from database.test_info import Test_maslach
from database.inquiries import inquiries
from database.tables import Users, Base, Problem, Message_r_i_dialog, Token, User_inquiries, Test_result, Test, Scale, \
    Inquiry, Education, Clients, Type_analysis, Intermediate_belief, Deep_conviction, FreeDiary, Diary_record, \
    Scale_result, Task, Borders, Question, Answer_choice
from fastapi import FastAPI, HTTPException
import uuid

# engine = create_engine(url="postgresql://postgres:postgresosikati@localhost:5432/psycho", echo=False)
engine = create_engine(url="postgresql://user:password@db:5432/dbname", echo=False)

session_factory = sessionmaker(engine)


class DatabaseService:
    def create_tables(self):
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def register_user(self, id, username, email, password, city, online, face_to_face, gender, description, role_id,
                      is_active):
        with session_factory() as session:
            try:
                user = Users(id=id,
                             username=username,
                             email=email,
                             password=password,
                             city=city,
                             online=online,
                             face_to_face=face_to_face,
                             gender=gender,
                             description=description,
                             role_id=role_id,
                             is_active=is_active
                             )
                session.add(user)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def check_user(self, email, password):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(email=email).one()
                pas = user.password

                if pas == password:
                    return 0
                else:
                    return -1

            except (Exception, Error) as error:
                print(error)
                return -1

    def check_role(self, id):
        with session_factory() as session:
            try:
                user = session.get(Users, id)
                role_id = user.role_id
                if role_id == 0:
                    return 0
                elif role_id == 1:
                    return 1
                elif role_id == 2:
                    return 2
                elif role_id == 3:
                    return 3
                else:
                    return -1

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_id_user(self, email):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(email=email).one()

                return user.id

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_user(self, email):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(email=email).one()

                return user

            except (Exception, Error) as error:
                print(error)
                return -1


    def get_user_by_id(self, id):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(id=id).one()

                return user

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_password_user(self, email):
        with session_factory() as session:
            try:
                user = session.query(Users).filter_by(email=email).one()
                return user.password

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_users(self):
        with session_factory() as session:
            try:
                query = select(Users)
                result = session.execute(query)
                users = result.scalars().all()

                user_list = []
                user_dict = {}
                for user in users:
                    user_dict['id'] = user.id
                    user_dict['username'] = user.username
                    user_dict['email'] = user.email
                    user_dict['password'] = user.password
                    user_dict['city'] = user.city
                    user_dict['online'] = user.online
                    user_dict['face_to_face'] = user.face_to_face
                    user_dict['gender'] = user.gender
                    user_dict['description'] = user.description
                    user_dict['role_id'] = user.role_id
                    user_dict['is_active'] = user.is_active
                    user_dict['token'] = user.token
                    user_list.append(user_dict)
                    user_dict = {}
                return user_list

            except (Exception, Error) as error:
                print(error)
                return -1

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
                        new_scale_result = {
                            "scale_id": scale_result.scale_id,
                            "score": scale_result.score
                        }

                        scale_results.append(new_scale_result)

                    result_dict["scale_results"] = scale_results
                    results_list.append(result_dict)

                return results_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_test_result_db(self, test_result_id):
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
                    new_scale_result = {
                        "scale_id": scale_result.scale_id,
                        "score": scale_result.score
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

    def add_problem_db(self, user_id, description, goal):
        with session_factory() as session:
            try:
                problem = Problem(id=uuid.uuid4(),
                                  description=description,
                                  user_id=user_id,
                                  goal=goal
                                  )
                session.add(problem)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_user_by_token(self, token_id):
        with session_factory() as session:
            try:
                token = session.query(Token).filter_by(token=token_id)
                user_id = token[0].user_id
                user = session.query(Users).filter_by(id=user_id).one()
                if user:
                    return user
                else:
                    return 0
            except (Exception, Error) as error:
                print(error)
                return 0

    def add_token_db(self, user_id, token_str):
        with session_factory() as session:
            try:
                token = Token(id=uuid.uuid4(),
                              user_id=user_id,
                              token=token_str,
                              exp_date=func.now(),
                              type=""
                              )
                session.add(token)
                session.commit()
                return 0
            except (Exception, Error) as error:
                raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")

    def update_user_db(self, user_id, username, gender, birth_date, request, city, description, type):

        with session_factory() as session:
            inquiry1 = session.query(User_inquiries).filter_by(user_id=user_id, type=type).all()
            for obj in inquiry1:
                session.delete(obj)
            user = session.get(Users, user_id)
            user.username = username
            user.gender = gender
            user.birth_date = birth_date
            user.city = city
            if user.role_id == 2:
                user.description = description
            session.commit()
            for i in range(len(request)):
                try:
                    user_inquiry = User_inquiries(id=uuid.uuid4(),
                                                  user_id=user_id,
                                                  inquiry_id=request[i],
                                                  type=type
                                                  )

                    session.add(user_inquiry)

                except (Exception, Error) as error:
                    print(error)
                    return -1

            session.commit()
            return 0

    # def add_message(problem_id):
    #     with session_factory() as session:
    #         try:
    #             message = Message_r_i_dialog(id=uuid.uuid4().__str__(),
    #                          is_rational=True,
    #                          text="sdf",
    #                          date=func.now(),
    #                          problem_id=problem_id
    #                          )
    #             session.add(message)
    #             session.commit()
    #             return 0
    #         except (Exception, Error) as error:
    #             print(error)
    #             return -1

    def save_test_result_db(self, user_id, test_id, date, results: List[ResScale]):
        with (session_factory() as session):
            try:
                if not session.query(Test).filter_by(id=test_id).one():
                    raise HTTPException(status_code=404, detail="Тест не найден!")

                test_res_id = uuid.uuid4()
                test_res = Test_result(id=test_res_id,
                                       user_id=user_id,
                                       test_id=test_id,
                                       date=date)

                session.add(test_res)

                scale_info = session.query(Scale).filter_by(test_id=test_id).all()

                for result in results:
                    scale = session.query(Scale).filter_by(id=result.scale_id).one()

                    if scale.test_id != test_id:
                        raise HTTPException(status_code=400,
                                            detail="Шкала не принадлежит переданному тесту!")

                    if len(scale_info) != len(results):
                        raise HTTPException(status_code=400,
                                            detail="Количество переданных шкал не совпадают с количеством шкал в базе данных!")

                    if result.score < scale.min:
                        raise HTTPException(status_code=400, detail="Результат не может быть меньше минимального значения шкалы!")

                    if result.score > scale.max:
                        raise HTTPException(status_code=400, detail="Результат не может быть больше максимального значения шкалы!")

                    scale_result = Scale_result(id=uuid.uuid4(),
                                                score=result.score,
                                                scale_id=result.scale_id,
                                                test_result_id=test_res_id)

                    session.add(scale_result)

                session.commit()
                return "Successfully!"

            except NoResultFound:
                raise HTTPException(status_code=404, detail="Тест или шкалы не были найдены!")
            except (Exception, Error) as error:
                raise error



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

    def create_inquirty(self):
        with session_factory() as session:
            for i in range(len(inquiries)):
                inquiry = Inquiry(id=i + 1,
                                  text=inquiries[i]
                                  )
                session.add(inquiry)
            session.commit()

    def psychologist_sent_db(self, user_id, username, title, document, description, city, online, face_to_face, gender,
                             birth_date, request):
        with session_factory() as session:
            try:
                database_service.update_user_db(user_id, username, gender, birth_date, request, city, description, 2)
                user = session.get(Users, user_id)
                user.online = online
                user.face_to_face = face_to_face
                user.role_id = 2

                ed = session.query(Education).filter_by(psychologist_id=user_id).all()
                for obj in ed:
                    session.delete(obj)
                session.commit()

                educ = Education(
                    id=uuid.uuid4(),
                    title=title,
                    document=document,
                    psychologist_id=user_id
                )
                session.add(educ)

                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def getClient(self, user_id):
        with session_factory() as session:
            user = session.get(Users, user_id)
            list = []
            request = session.query(User_inquiries).filter_by(user_id=user_id, type=1).all()
            for obj in request:
                list.append(session.get(Inquiry, obj.inquiry_id).text)

            user_dict = {}
            user_dict['client_id'] = user.id
            user_dict['username'] = user.username
            user_dict['birth_date'] = user.birth_date
            user_dict['gender'] = user.gender
            user_dict['request'] = list

        session.commit()
        return user_dict

    def getListClient(self, psyh_id):
        with session_factory() as session:
            user_dict = {}
            user_list = []

            list_clients = session.query(Clients).filter_by(psychologist_id=psyh_id, status=True).all()
            for obj in list_clients:
                request_list = []

                temp = session.get(Users, obj.client_id)

                user_dict["username"] = temp.username
                user_dict['is_active'] = temp.is_active
                user_dict['client_id'] = temp.id

                request_id = session.query(User_inquiries).filter_by(user_id=temp.id, type=1).all()

                for i in request_id:
                    request = session.query(Inquiry).filter_by(id=i.inquiry_id).first()
                    request_list.append(request.text)

                user_dict['request'] = request_list

                user_list.append(user_dict)
                user_dict = {}

            session.commit()
            return user_list

    def send_application_db(self, client_id, psyh_id, text):
        with session_factory() as session:
            temp = session.query(Clients).filter_by(client_id=client_id, psychologist_id=psyh_id).first()
            if temp:
                session.delete(temp)

            try:
                app = Clients(id=uuid.uuid4(),
                              psychologist_id=psyh_id,
                              client_id=client_id,
                              text=text,
                              status=False
                              )
                session.add(app)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def confirm_application_db(self, psyh_id, client_id, status):
        with session_factory() as session:
            try:

                temp = session.query(Clients).filter_by(client_id=client_id, psychologist_id=psyh_id).first()

                if temp is None:
                    raise ValueError(f"Клиент с client_id={client_id} и psychologist_id={psyh_id} не найден")

                if status is False:
                    session.delete(temp)
                elif status is True:
                    temp.status = status

                session.commit()
                return 0
            except ValueError as ve:
                print(f"Ошибка значения: {ve}")
                return -1
            except (Exception, Error) as error:
                print(f"Исключение: {error}")
                session.rollback()  # Откат в случае ошибки
                return -1

    def get_psycholog(self, user_id):
        with session_factory() as session:
            user = session.get(Users, user_id)
            list = []
            request = session.query(User_inquiries).filter_by(user_id=user_id, type=2).all()
            edu = session.query(Education).filter_by(psychologist_id=user_id).first()
            for obj in request:
                list.append(session.get(Inquiry, obj.inquiry_id).text)

            user_dict = {}
            user_dict['username'] = user.username
            user_dict['birth_date'] = user.birth_date
            user_dict['gender'] = user.gender
            user_dict['city'] = user.city
            user_dict['online'] = user.online
            user_dict['face_to_face'] = user.face_to_face
            user_dict['title'] = edu.title
            user_dict['document'] = edu.document
            user_dict['description'] = user.description
            user_dict['request'] = list

        session.commit()
        return user_dict

    def get_list_psycholog(self, user_id):
        with session_factory() as session:
            user_dict = {}
            user_list = []

            list_psycholog = session.query(Clients).filter_by(client_id=user_id, status=True).all()
            for obj in list_psycholog:
                request_list = []

                temp = session.get(Users, obj.psychologist_id)

                user_dict["username"] = temp.username
                user_dict['is_active'] = temp.is_active

                request_id = session.query(User_inquiries).filter_by(user_id=temp.id, type=2).all()

                for i in request_id:
                    request = session.query(Inquiry).filter_by(id=i.inquiry_id).first()
                    request_list.append(request.text)

                user_dict['request'] = request_list

                user_list.append(user_dict)
                user_dict = {}

            session.commit()
            return user_list

    def create_type_analysis(self):
        with session_factory() as session:
            type = ["догматическое требование", "Драматизация", "НПФ", "Гибкое предпочтение", "Унизительные замечание",
                    "Перспектива", "Высокий порог фрустрации", "Безусловное принятие"]
            for i in range(len(type)):
                tanalys = Type_analysis(id=i + 1,
                                        text=type[i]
                                        )
                session.add(tanalys)
            session.commit()

    def save_problem_analysis_db(self, problem_id, type):
        with session_factory() as session:
            try:
                temp = Intermediate_belief(
                    id=uuid.uuid4(),
                    problem_id=problem_id,
                    type=type
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def create_deep_conviction_db(self, problem_id, disadaptive, adaptive):
        with session_factory() as session:
            try:
                temp = Deep_conviction(
                    id=uuid.uuid4(),
                    problem_id=problem_id,
                    disadaptive=disadaptive,
                    adaptive=adaptive
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def save_belief_analysis_db(self, intermediate_conviction_id, text,
                                feeling_and_actions, motivation, hindrances, incorrect_victims, results):
        with session_factory() as session:
            try:
                temp = session.get(Intermediate_belief, intermediate_conviction_id)
                temp.text = text
                temp.feelings_and_actions = feeling_and_actions
                temp.motivation = motivation
                temp.hindrances = hindrances
                temp.incorrect_victims = incorrect_victims
                temp.results = results
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def save_belief_check_db(self, intermediate_conviction_id, truthfulness, consistency, usefulness):
        with session_factory() as session:
            try:
                temp = session.get(Intermediate_belief, intermediate_conviction_id)
                temp.truthfulness = truthfulness
                temp.consistency = consistency
                temp.usefulness = usefulness
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_belief_analysis(self, intermediate_conviction_id):
        with session_factory() as session:
            try:
                dic = {}
                temp = session.get(Intermediate_belief, intermediate_conviction_id)
                dic["feelings_and_actions"] = temp.feelings_and_actions
                dic["motivation"] = temp.motivation
                dic["hindrances"] = temp.hindrances
                dic["incorrect_victims"] = temp.incorrect_victims
                dic["results"] = temp.results

                return dic
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_belief_check(self, intermediate_conviction_id):
        with session_factory() as session:
            try:
                dic = {}
                temp = session.get(Intermediate_belief, intermediate_conviction_id)
                dic["truthfulness"] = temp.truthfulness
                dic["consistency"] = temp.consistency
                dic["usefulness"] = temp.usefulness

                return dic
            except (Exception, Error) as error:
                print(error)
                return -1

    def writing_free_diary_db(self, user_id, text):
        with session_factory() as session:
            try:
                temp = FreeDiary(
                    id=uuid.uuid4(),
                    user_id=user_id,
                    text=text
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def writing_think_diary_db(self, user_id, situation, mood, level, auto_thought, proofs,
                               refutations, new_mood, alternativeThought, new_level, behaviour):
        with session_factory() as session:
            try:
                temp = Diary_record(
                    id=uuid.uuid4(),
                    user_id=user_id,
                    situation=situation,
                    mood=mood,
                    level=level,
                    auto_thought=auto_thought,
                    proofs=proofs,
                    refutations=refutations,
                    new_mood=new_mood,
                    alternativeThought=alternativeThought,
                    new_level=new_level,
                    behavioral=behaviour,
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def reading_think_diary_db(self, think_diary_id):
        with session_factory() as session:
            try:
                dic = {}
                temp = session.get(Diary_record, think_diary_id)

                dic["situation"] = temp.situation
                dic["mood"] = temp.mood
                dic["level"] = temp.level
                dic["auto_thought"] = temp.auto_thought
                dic["proofs"] = temp.proofs
                dic["refutations"] = temp.refutations
                dic["new_mood"] = temp.new_mood
                dic["new_level"] = temp.new_level
                dic["behavioral"] = temp.behavioral
                return dic
            except (Exception, Error) as error:
                print(error)
                return -1

    def reading_free_diary_db(self, user_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(FreeDiary).filter_by(user_id=user_id).all()

                for obj in temp:
                    list.append({
                        "text": obj.text,
                        "free_diary_id": obj.id
                    })

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_list_applications_db(self, user_id):
        with session_factory() as session:
            try:
                result_list = []

                temp = session.query(Clients).filter_by(psychologist_id=user_id, status=False).all()

                for obj in temp:
                    user = session.get(Users, obj.client_id)
                    if user is None:
                        continue  # Skip if user not found

                    problem = session.query(Problem).filter_by(user_id=user.id).first()
                    if problem is None:
                        dict_item = {
                            "app_id": obj.id,
                            "client_id": obj.client_id,
                            "username": user.username,
                            "text": obj.text,
                            "online": user.online,
                            "problem_id": None,
                            "problem": None
                        }
                        result_list.append(dict_item)
                        continue  # Skip if problem not found

                    # Create a new dictionary for each iteration
                    dict_item = {
                        "app_id": obj.id,
                        "client_id": obj.client_id,
                        "username": user.username,
                        "text": obj.text,
                        "online": user.online,
                        "problem_id": problem.id,
                        "problem": problem.description
                    }

                    result_list.append(dict_item)
                return result_list
            except (Exception, Error) as error:
                print(error)
                return -1

    def watch_application_db(self, user_id, app_id):
        with session_factory() as session:
            try:
                app = session.get(Clients, app_id)
                user = session.get(Users, app.client_id)
                dict = {}

                dict["app_id"] = app.id
                dict["client_id"] = app.client_id
                dict["username"] = user.username
                dict["is_active"] = False
                dict["birth_date"] = user.birth_date
                dict["gender"] = user.gender
                dict["text"] = app.text

                return dict
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_problem_analysis_db(self, problem_id):
        with session_factory() as session:
            try:
                temp = session.query(Intermediate_belief).filter_by(problem_id=problem_id).all()
                list = []
                dict = {}

                for obj in temp:
                    dict["id"] = obj.id
                    dict["text"] = obj.text
                    dict["truthfulness"] = obj.truthfulness
                    dict["consistency"] = obj.consistency
                    dict["usefulness"] = obj.usefulness
                    dict["feelings_and_actions"] = obj.feelings_and_actions
                    dict["motivation"] = obj.motivation
                    dict["hindrances"] = obj.hindrances
                    dict["incorrect_victims"] = obj.incorrect_victims
                    dict["results"] = obj.results
                    dict["problem_id"] = obj.problem_id
                    dict["deep_conviction_id"] = obj.deep_conviction
                    dict["type"] = obj.type
                    list.append(dict)
                    dict = {}

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def writing_r_i_dialog_db(self, problem_id, text, type):
        with session_factory() as session:
            try:
                temp = Message_r_i_dialog(
                    id=uuid.uuid4(),
                    problem_id=problem_id,
                    text=text,
                    is_rational=type,
                    date=func.now()
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def reading_r_i_dialog_db(self, problem_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Message_r_i_dialog).filter_by(problem_id=problem_id).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_list_tegs(self):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Inquiry).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def manager_send_db(self, user_id, username, description, company, city, online, gender, birth_date):
        with session_factory() as session:
            try:
                user = session.get(Users, user_id)
                user.username = username
                user.description = description
                user.city = city
                user.company = company
                user.gender = gender
                user.birth_date = birth_date
                user.online = online
                user.role_id = 3

                session.commit()

                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def give_task_db(self, psychologist_id, text, test_title, test_id, client_id):
        with session_factory() as session:
            try:
                temp = Task(
                    id=uuid.uuid4(),
                    psychologist_id=psychologist_id,
                    text=text,
                    test_title=test_title,
                    test_id=test_id,
                    client_id=client_id,
                    is_complete=False
                )
                session.add(temp)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_tasks_db(self, client_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Task).filter_by(client_id=client_id).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def complete_task_db(self, client_id, task_id):
        with session_factory() as session:
            try:
                temp = session.get(Task, task_id)

                if temp.client_id == uuid.UUID(client_id):
                    temp.is_complete = True
                    session.commit()
                    return 1
                else:
                    return 2

            except (Exception, Error) as error:
                print(error)
                return -1

    def unfulfilled_task_db(self, client_id, task_id):
        with session_factory() as session:
            try:
                temp = session.get(Task, task_id)

                if temp.client_id == uuid.UUID(client_id):
                    temp.is_complete = False
                    session.commit()
                    return 1
                else:
                    return 2

            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_problems(self, user_id):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Problem).filter_by(user_id=user_id).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_think_diary_db(self, user_id):
        with session_factory() as session:
            try:
                list = []
                dict = {}
                temp = session.query(Diary_record).filter_by(user_id=user_id).all()

                for obj in temp:
                    dict["id"] = obj.id
                    dict["situation"] = obj.situation

                    list.append(dict)
                    dict = {}

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_psycholog_db(self):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Users).filter_by(role_id=2).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_all_manager_db(self):
        with session_factory() as session:
            try:
                list = []
                temp = session.query(Users).filter_by(role_id=3).all()

                for obj in temp:
                    list.append(obj)

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_test_questions_db(self, test_id):
        with session_factory() as session:
            try:
                list = []
                dic = {}
                temp = session.query(Question).filter_by(test_id=test_id).all()

                if temp == []:
                    return "тест не найден"

                for obj in temp:
                    dic["number"] = obj.number
                    dic["text"] = obj.text

                    list.append(dic)
                    dic = {}

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def create_test(self, test_info):
        with session_factory() as session:
            try:
                test_id = uuid.uuid4()
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
                        number=i+1,
                        test_id=test_id
                    )
                    session.add(question)

                    for j in range(len(test_info.answers)):
                        answer = Answer_choice(
                            id=uuid.uuid4(),
                            text=test_info.answers[j],
                            question_id=question_id,
                            score=j
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
                        max=test_info.scale_limitation[k+1],
                    )
                    k += 2
                    session.add(scale)

                    k = 0
                    for j in range(test_info.borders_cnt):

                        border = Borders(
                            id=uuid.uuid4(),
                            scale_id=scale_id,
                            left_border=test_info.scale_border[i][j],
                            right_border=test_info.scale_border[i][j+1],
                            color=test_info.scale_color[i][k],
                            title=test_info.scale_title[i][k]
                        )
                        j += 1
                        k += 1
                        session.add(border)


                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1




database_service = DatabaseService()

database_service.create_tables()

if database_service.check_user("admin", "admin") == -1:
    database_service.create_inquirty()
    database_service.create_type_analysis()
    database_service.create_test(Test_maslach)
    database_service.register_user(uuid.uuid4(), "admin", "admin", "admin", "", True, True, "", "", 0, True)
