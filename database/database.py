from psycopg2 import Error
from sqlalchemy import Integer, String, create_engine, select
from sqlalchemy.orm import sessionmaker
from database.tables import Users, Base
import uuid

engine = create_engine(url="postgresql://postgres:postgresosikati@localhost:5432/psycho", echo=False)

session_factory = sessionmaker(engine)

def create_tables():
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
create_tables()

def register_user(id, email, username, password, verified, gender, description, active, role_id):
    with session_factory() as session:
        try:
            user = Users(id=id,
                         email=email,
                         username=username,
                         password=password,
                         verified=verified,
                         gender=gender,
                         description=description,
                         active=active,
                         role_id=role_id
                         )
            session.add(user)
            session.commit()
            return 0
        except (Exception, Error) as error:
            print(error)
            return -1
# register_user(uuid.uuid4().__str__(), "admin", "admin", "admin", True, True, "", True, 0)

def check_user(email, password):
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

def check_role(id):
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

def get_id_user(email):
    with session_factory() as session:
        try:
            user = session.query(Users).filter_by(email=email).one()
            return user.id

        except (Exception, Error) as error:
            print(error)
            return -1

def get_password_user(email):
    with session_factory() as session:
        try:
            user = session.query(Users).filter_by(email=email).one()
            return user.password

        except (Exception, Error) as error:
            print(error)
            return -1

def get_all_users():
    with session_factory() as session:
        try:
            query = select(Users)
            result = session.execute(query)
            users = result.scalars().all()

            user_list = []
            user_dict = {}
            for user in users:
                user_dict['id'] = user.id
                user_dict['email'] = user.email
                user_dict['username'] = user.username
                user_dict['password'] = user.password
                user_dict['verified'] = user.verified
                user_dict['gender'] = user.gender
                user_dict['description'] = user.description
                user_dict['active'] = user.active
                user_dict['role_id'] = user.role_id
                user_list.append(user_dict)
                user_dict = {}
            return user_list

        except (Exception, Error) as error:
            print(error)
            return -1
