from schemas.users import Creds
import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    role TEXT,
    username TEXT,
    password TEXT
)""")
db.commit()

class UserServise:

    def get_users(self) -> list:
        items = []
        # for value in sql.execute("SELECT * FROM users"):
        #     items.append(value)

        return items


    def register(self, payload: Creds) -> None:
        pass
        # sql.execute("SELECT username FROM users")
        # if sql.fetchone() is None:
        #     sql.execute("INSERT INTO users (role, username, password) VALUES (?, ?, ?)", ('user', payload.username, payload.password))
        #     db.commit()




user_service: UserServise = UserServise()