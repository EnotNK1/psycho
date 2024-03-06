from schemas.users import Creds, Reg, ResetPassword
from database.database import register_user, get_all_users, check_user, get_id_user, check_role, get_password_user
from services.auth import send_email
from services.auth import generate_token, verify_token
import uuid
from starlette.responses import JSONResponse, Response
from smtplib import SMTPRecipientsRefused

class UserServise:

    async def get_users(self, access_token) -> list or str:
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return  "Invalid token"

        role = check_role(token_data['user_id'])

        if role == 0:
            items = get_all_users()
            return items
        else:
            return "access denied"

    async def authorization (self, payload: Creds, response: Response):

        if check_user(payload.email, payload.password) == 0:
            id_user = get_id_user(payload.email)

            token = generate_token(id_user)
            response.set_cookie(key="access_token", value=token, httponly=True)
            return "Logged in successfully"
        else:
            return "error"

    async def register(self, payload: Reg) -> str:

        if payload.password == payload.confirm_password:
            if register_user(uuid.uuid4().__str__(), payload.email, payload.username, payload.password, False, payload.gender, "", True, "1") == 0:
                return "Successfully"
            else:
                return "A user with this email address has already been registered"

    async def reset_password(self, payload: ResetPassword) -> str:

        if get_id_user(payload.email) != -1:
            try:
                user_password = get_password_user(payload.email)
                subject = "Password Reset"
                message = f"Your password is: {user_password}"
                send_email(payload.email, subject, message)
                return "The password email has been sent"
            except SMTPRecipientsRefused:
                return "incorrect email"
        else:
            return "No user with this e-mail account was found"





user_service: UserServise = UserServise()