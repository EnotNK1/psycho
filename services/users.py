from schemas.users import Creds
from database.database import get_users_db, register_db

class UserServise:

    def get_users(self) -> list:
        items = get_users_db()

        return items


    def register(self, payload: Creds) -> None:
        register_db(payload.username, payload.password)




user_service: UserServise = UserServise()