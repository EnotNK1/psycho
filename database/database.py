import psycopg2
from psycopg2 import Error
from database.tables import create_user_table
import uuid

create_user_table()

def register_user(id, email, username, password, verified, gender, description, active, role_id):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgresosikati",
            host="localhost",
            port="5432",
            database="psycho"
        )

        cursor = connection.cursor()

        insert_query = """INSERT INTO users (id, email, username, password, verified, gender, description, active, role_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        record_to_insert = (id, email, username, password, verified, gender, description, active, role_id)

        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        print("Пользователь успешно зарегистрирован")
        cursor.close()
        connection.close()
        return 0

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return -1

register_user(uuid.uuid4().__str__(), "admin@mail.ru", "admin", "admin", True, "male", "", True, "0")

def check_user(email, password):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgresosikati",
            host="localhost",
            port="5432",
            database="psycho"
        )

        cursor = connection.cursor()

        query = "SELECT password FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        confirm_password = cursor.fetchone()

        cursor.close()
        connection.close()
        if (confirm_password[0] == password):
            return 0
        else:
            return -1

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return -1


def check_role(user_id):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgresosikati",
            host="localhost",
            port="5432",
            database="psycho"
        )

        cursor = connection.cursor()

        query = "SELECT role_id FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        confirm_id = cursor.fetchone()

        cursor.close()
        connection.close()
        if (confirm_id[0] == "0"):
            return 0
        elif (confirm_id[0] == "1"):
            return 1
        elif (confirm_id[0] == "2"):
            return 2
        else:
            return -1

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return -1

def get_id_user(email):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgresosikati",
            host="localhost",
            port="5432",
            database="psycho"
        )

        cursor = connection.cursor()

        query = "SELECT id FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        id_user = cursor.fetchone()

        cursor.close()
        connection.close()
        return id_user[0]

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return -1

def get_password_user(email):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgresosikati",
            host="localhost",
            port="5432",
            database="psycho"
        )

        cursor = connection.cursor()

        query = "SELECT password FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        password_user = cursor.fetchone()

        cursor.close()
        connection.close()
        return password_user[0]

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return -1

def get_all_users():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgresosikati",
            host="localhost",
            port="5432",
            database="psycho"
        )

        cursor = connection.cursor()

        select_query = """SELECT * FROM users"""

        cursor.execute(select_query)

        # Получение результатов запроса
        users = cursor.fetchall()

        # Вывод результатов
        user_list = []
        user_dict = {}
        for user in users:
            user_dict['id'] = user[0]
            user_dict['email'] = user[1]
            user_dict['username'] = user[2]
            user_dict['password'] = user[3]
            user_dict['verified'] = user[4]
            user_dict['gender'] = user[5]
            user_dict['description'] = user[6]
            user_dict['active'] = user[7]
            user_dict['role_id'] = user[8]
            user_list.append(user_dict)
            user_dict = {}

        cursor.close()
        connection.close()
        return user_list
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)