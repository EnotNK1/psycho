from schemas.users import Creds, Reg
from database.database import register_user, get_all_users, check_user, get_id_user, check_role
from services.auth import generate_token, verify_token
import uuid
from starlette.responses import JSONResponse, Response

class UserServise:

    def get_users(self, access_token) -> list or str:
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        role = check_role(token_data['user_id'])

        if (role == 0):
            items = get_all_users()
            return items
        else:
            return "access denied"

    def authorization (self, payload: Creds, response: Response):

        if (check_user(payload.email, payload.password) == 0):
            id_user = get_id_user(payload.email)

            token = generate_token(id_user)
            response.set_cookie(key="access_token", value=token, httponly=True)
            return "Logged in successfully"
        else:
            return "error"

    def register(self, payload: Reg) -> str:

        if (payload.password == payload.confirm_password):
            if (register_user(uuid.uuid4().__str__(), payload.email, payload.username, payload.password, False, payload.gender, "", True, "1") == 0):
                return "Successfully"
            else:
                return "A user with this email address has already been registered"




user_service: UserServise = UserServise()