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

    def __init__(self, sql, db):
        self.sql = sql
        self.db = db

    def get_users(self) -> list:
        items = []
        for value in self.sql.execute("SELECT * FROM users"):
            items.append(value)

        return items


    def register(self, payload: Creds) -> None:
        self.sql.execute("SELECT username FROM users")

        role = "user"

        if self.sql.fetchone() is None:
            self.sql.execute("INSERT INTO users VALUES (?, ?, ?)", (role, payload.username, payload.password))
            self.db.commit()




user_service: UserServise = UserServise(sql, db)