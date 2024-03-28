from schemas.users import Creds, Reg, ResetPassword, AddProblem, SaveTestRes, CreateTest, GetTestRes
from database.database import database_service
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

        role = database_service.check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            items = database_service.get_all_users()
            return items
        else:
            return "access denied"

    def authorization (self, payload: Creds, response: Response):

        if database_service.check_user(payload.email, payload.password) == 0:
            user_id = database_service.get_id_user(payload.email)

            token = generate_token(user_id)
            response.set_cookie(key="access_token", value=token, httponly=True)
            database_service.add_token_db(user_id, token)
            return token
        else:
            return "error"

    def register(self, payload: Reg) -> str:

        if payload.password == payload.confirm_password:
            if database_service.register_user(uuid.uuid4(), payload.username, payload.email, payload.password, "", False, False, "", "", 1, False) == 0:
                return "Successfully"
            else:
                return "A user with this email address has already been registered"
        else:
            return "Password mismatch"

    def reset_password(self, payload: ResetPassword) -> str:

        if database_service.get_id_user(payload.email) != -1:
            try:
                user_password = database_service.get_password_user(payload.email)
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

        database_service.add_problem_db(token_data['user_id'], payload.description)

        return "Successfully"

    def save_test_result(self, payload: SaveTestRes, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return  "Invalid token"

        database_service.save_test_result_db(token_data['user_id'], payload.title, uuid.UUID(payload.test_id), payload.date, payload.score)

        return "Successfully"

    def create_test(self, payload: CreateTest, access_token) -> str:
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            database_service.create_test_db(payload.title, payload.description, payload.short_desc)
        else:
            return "access denied"

    def get_test_res(self, payload: GetTestRes, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return  "Invalid token"

        res_list = database_service.get_test_res_db(token_data['user_id'], uuid.UUID(payload.test_id))

        return res_list





user_service: UserServise = UserServise()