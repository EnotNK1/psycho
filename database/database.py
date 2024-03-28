from psycopg2 import Error
from sqlalchemy import Integer, String, create_engine, select, func
from sqlalchemy.orm import sessionmaker, joinedload
from database.tables import Users, Base, Problem, Message_r_i_dialog, Token, User_inquiries, Test_result, Test, Scale, \
    Inquiry, Education, Clients
import uuid

engine = create_engine(url="postgresql://postgres:1111@localhost:5432/psycho", echo=False)
# engine = create_engine(url="postgresql://user:password@db:5432/dbname", echo=False)

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
                print("xyi")
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
                    joinedload(Test_result.scale))
                res = session.execute(query)
                users = res.unique().scalars().all()

                user_list = []
                user_dict = {}
                for user in users:
                    user_dict['datetime'] = user.date
                    user_dict['scale'] = user.scale

                    user_list.append(user_dict)
                    user_dict = {}
                return user_list

            except (Exception, Error) as error:
                print(error)
                return -1

    def add_problem_db(self, user_id, description):
        with session_factory() as session:
            try:
                problem = Problem(id=uuid.uuid4(),
                                  description=description,
                                  user_id=user_id
                                  )
                session.add(problem)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

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
                print(error)
                return -1

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

    def save_test_result_db(self, user_id, title, test_id, date, score):
        with session_factory() as session:
            try:
                test_res_id = uuid.uuid4()
                test_res = Test_result(id=test_res_id,
                                       user_id=user_id,
                                       test_id=test_id,
                                       date=date
                                       )
                scale = Scale(id=uuid.uuid4(),
                              title=title,
                              score=score,
                              test_result_id=test_res_id)
                session.add(test_res)
                session.add(scale)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def create_test_db(self, title, description, short_desc):
        with session_factory() as session:
            try:
                test = Test(id=uuid.uuid4(),
                            title=title,
                            description=description,
                            short_desc=short_desc
                            )
                session.add(test)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1

    def create_inquirty(self):
        with session_factory() as session:
            inquiries = ["Самооценка", "Сон", "Страх", "Секс", "Агрессия", "Стресс", "Выгорание",
                         "Депрессия", "Вредные привычки", "Семья", "Мысли о суициде", "Панические атаки"]
            for i in range(len(inquiries)):
                inquiry = Inquiry(id=i + 1,
                                  text=inquiries[i]
                                  )
                session.add(inquiry)
            session.commit()

    def psychologist_sent_db(self, user_id, username, title, document, description, city, online, face_to_face, gender,
                             birth_date, request):
        with session_factory() as session:
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

    def getClient(self, user_id):
        with session_factory() as session:
            user = session.get(Users, user_id)
            list = []
            request = session.query(User_inquiries).filter_by(user_id=user_id, type=1).all()
            for obj in request:
                list.append(session.get(Inquiry, obj.inquiry_id).text)

            user_dict = {}
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
                if status == False:
                    temp = session.query(Clients).filter_by(client_id=client_id, psychologist_id=psyh_id).first()
                    session.delete(temp)
                    session.commit()

                elif status == True:
                    temp = session.query(Clients).filter_by(client_id=client_id, psychologist_id=psyh_id).first()
                    temp.status = status
                    session.commit()

                return 0
            except (Exception, Error) as error:
                print(error)
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

    def getListPsycholog(self, user_id):
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

database_service = DatabaseService()

database_service.create_tables()

if database_service.check_user("admin", "admin") == -1:
    database_service.create_inquirty()
    database_service.register_user(uuid.uuid4(), "admin", "admin", "admin", "", True, True, "", "", 0, True)
