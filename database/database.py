import psycopg2
from psycopg2 import Error


def create_users_table():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgresosikati",
            host="localhost",
            port="5432",
            database="psycho"
        )

        cursor = connection.cursor()

        create_table_query = '''CREATE TABLE IF NOT EXISTS users (
                                id SERIAL PRIMARY KEY,
                                username VARCHAR(50) UNIQUE NOT NULL,
                                password VARCHAR(50) NOT NULL); '''

        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def register_user(username, password):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgresosikati",
            host="localhost",
            port="5432",
            database="psycho"
        )

        cursor = connection.cursor()

        insert_query = """INSERT INTO users (username, password) VALUES (%s, %s)"""
        record_to_insert = (username, password)

        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        print("Пользователь успешно зарегистрирован")
        cursor.close()
        connection.close()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


# Пример использования функций
create_users_table()


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
        user_item = []
        for user in users:
            user_item.append(user[0])
            user_item.append(user[1])
            user_item.append(user[2])
            user_list.append(user_item)
            user_item = []

        cursor.close()
        connection.close()
        return user_list
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)