import psycopg2
from psycopg2 import Error

def create_user_table():
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
                                id VARCHAR(50) UNIQUE NOT NULL,
                                email VARCHAR(50) UNIQUE NOT NULL,
                                username VARCHAR(50) NOT NULL,
                                password VARCHAR(50) NOT NULL,
                                verified BOOLEAN NOT NULL,
                                gender VARCHAR(50) NOT NULL,
                                description VARCHAR(50),
                                active BOOLEAN NOT NULL,
                                role_id VARCHAR(50) NOT NULL); '''

        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)