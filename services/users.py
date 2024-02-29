from schemas.users import Creds, Reg
from database.database import register_user, get_all_users
import uuid

class UserServise:

    def get_users(self) -> list:

        items = get_all_users()
        return items


    def register(self, payload: Reg) -> str:

        if (payload.password == payload.confirm_password):
            if (register_user(uuid.uuid4().__str__(), payload.email, payload.username, payload.password, False, payload.gender, "", True, "1") == 0):
                return "Successfully"
            else:
                return "A user with this email address has already been registered"




user_service: UserServise = UserServise()