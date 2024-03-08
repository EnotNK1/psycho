from schemas.users import Creds, Reg, ResetPassword, AddProblem
from database.database import register_user, get_all_users, check_user, get_id_user, check_role, get_password_user, add_problem_db
from services.auth import send_email
from services.auth import generate_token, verify_token
import uuid
from starlette.responses import JSONResponse, Response
from smtplib import SMTPRecipientsRefused

class UserServise:

    def get_users(self, access_token) -> list or str:
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return  "Invalid token"

        role = check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            items = get_all_users()
            return items
        else:
            return "access denied"

    def authorization (self, payload: Creds, response: Response):

        if check_user(payload.email, payload.password) == 0:
            id_user = get_id_user(payload.email)

            token = generate_token(id_user)
            response.set_cookie(key="access_token", value=token, httponly=True)
            return "Logged in successfully"
        else:
            return "error"

    def register(self, payload: Reg) -> str:

        if payload.role == 1 or payload.role == 2:
            if payload.password == payload.confirm_password:
                if register_user(uuid.uuid4(), payload.username, payload.email, payload.password, "", False, False, "", "", payload.role, False) == 0:
                    return "Successfully"
                else:
                    return "A user with this email address has already been registered"
            else:
                return "Password mismatch"
        else:
            return "Role is incorrect"

    def reset_password(self, payload: ResetPassword) -> str:

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

    def add_problem(self, payload: AddProblem, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return  "Invalid token"

        add_problem_db(token_data['user_id'], payload.description)

        return "Successfully"





user_service: UserServise = UserServise()