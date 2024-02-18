import sqlite3

db = sqlite3.connect('../server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    role TEXT,
    username TEXT,
    password TEXT
)""")
db.commit()


def get_users_db() -> list:
    items = []
    for value in sql.execute("SELECT * FROM users"):
        items.append(value)

    return items

def register_db(username, password) -> None:
    sql.execute(f"SELECT username FROM users WHERE username = '{username}'")
    role = "user"
    if sql.fetchone() is None:
        sql.execute("INSERT INTO users VALUES (?, ?, ?)", (role, username, password))
        db.commit()