from schemas.users import Creds
from database.database import register_user, get_all_users

class UserServise:

    def get_users(self) -> list:
        items = get_all_users()

        return items


    def register(self, payload: Creds) -> None:
        register_user(payload.username, payload.password)




user_service: UserServise = UserServise()