from psycopg2 import Error
from sqlalchemy import Integer, String, create_engine, select, func
from sqlalchemy.orm import sessionmaker
from database.tables import Users, Base, Problem, Message_r_i_dialog
import uuid

# engine = create_engine(url="postgresql://postgres:postgresosikati@localhost:5432/psycho", echo=False)
engine = create_engine(url="postgresql://user:password@db:5432/dbname", echo=False)

session_factory = sessionmaker(engine)

class DatabaseService:
    def create_tables(self):
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def register_user(self, id, username, email, password, city, online, face_to_face, gender, description, role_id, is_active):
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
                                  user_id=user_id,
                                  )
                session.add(problem)
                session.commit()
                return 0
            except (Exception, Error) as error:
                print(error)
                return -1


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

database_service = DatabaseService()

database_service.create_tables()

if database_service.check_user("admin", "admin") == -1:
    database_service.register_user(uuid.uuid4(), "admin", "admin", "admin", "", True, True, "", "", 0, True)
