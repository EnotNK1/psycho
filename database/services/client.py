import uuid

from psycopg2 import Error

from database.database import session_factory
from database.models.test import *
from database.models.users import *


class ClientServiceDB:

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

    def get_tasks_db(self, client_id):
        with session_factory() as session:
            try:
                list = []
                dic = {}
                temp = session.query(Task).filter_by(client_id=client_id).all()

                for obj in temp:
                    desc = session.get(Test, obj.test_id)
                    dic["id"] = obj.id
                    dic["test_title"] = obj.test_title
                    dic["psychologist_id"] = obj.psychologist_id
                    dic["is_complete"] = obj.is_complete
                    dic["test_id"] = obj.test_id
                    dic["text"] = obj.text
                    dic["client_id"] = obj.client_id
                    dic["test_description"] = desc.description
                    list.append(dic)
                    dic = {}

                return list
            except (Exception, Error) as error:
                print(error)
                return -1

    def get_given_tasks_db(self, psychologist_id):
        with session_factory() as session:
            try:
                list = []
                dic = {}
                temp = session.query(Task).filter_by(psychologist_id=psychologist_id).all()

                for obj in temp:
                    desc = session.get(Test, obj.test_id)
                    dic["id"] = obj.id
                    dic["test_title"] = obj.test_title
                    dic["psychologist_id"] = obj.psychologist_id
                    dic["is_complete"] = obj.is_complete
                    dic["test_id"] = obj.test_id
                    dic["text"] = obj.text
                    dic["client_id"] = obj.client_id
                    dic["test_description"] = desc.description
                    list.append(dic)
                    dic = {}

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

    def delete_task_db(self, task_id):
        with session_factory() as session:
            try:
                temp = session.query(Task).get(task_id)
                if temp is not None:
                    session.delete(temp)
                    session.commit()
                    return 1
                else:
                    return -2
            except (Exception, Error) as error:
                print(error)
                return -1

    def delete_incorrect_tasks_db(self):
        with session_factory() as session:
            try:
                correct_id = []
                test_id = session.query(Test).all()
                for obj in test_id:
                    correct_id.append(obj.id)

                task = session.query(Task).all()
                for obj in task:
                    if obj.test_id not in correct_id:
                        session.delete(obj)
                session.commit()

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

    def get_your_psychologist_db(self, user_id):
        with session_factory() as session:
            try:
                user_dict = {}
                user_list = []

                list_psycholog = session.query(Clients).filter_by(client_id=user_id, status=True).all()
                for obj in list_psycholog:
                    request_list = []

                    temp = session.get(Users, obj.psychologist_id)

                    user_dict["id"] = temp.id
                    user_dict["role"] = temp.role_id
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

            except (Exception, Error) as error:
                print(error)
                return -1




client_service_db: ClientServiceDB = ClientServiceDB()