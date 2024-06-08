from schemas.users import Creds, Reg, ResetPassword, UpdateUser
from database.database import database_service
from services.auth import send_email
from services.auth import generate_token, verify_token
import uuid
from starlette.responses import Response
from smtplib import SMTPRecipientsRefused
from psycopg2 import Error


class UserServise:

    def get_users(self, access_token) -> list or str:
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            items = database_service.get_all_users()
            return items
        else:
            return "access denied"

    def authorization(self, payload: Creds, response: Response):

        if database_service.check_user(payload.email, payload.password) == 0:
            user = database_service.get_user(payload.email)

            token = generate_token(user.id)
            response.set_cookie(key="access_token", value=token, httponly=True)
            database_service.add_token_db(user.id, token)
            return {
                "token": token,
                "user_id": user.id,
                "role": user.role_id,
                "email": user.email,
                "username": user.username
            }
        else:
            return "error"

    def authorization_token(self, payload, response: Response):

        user = database_service.get_user_by_token(payload.token)
        if user == 0:
            return "Error"
        token = generate_token(user.id)
        response.set_cookie(key="access_token", value=token, httponly=True)
        database_service.add_token_db(user.id, token)
        return {
            "token": token,
            "user_id": user.id,
            "role": user.role_id,
            "email": user.email,
            "username": user.username
        }

    def register(self, payload: Reg):

        if payload.password == payload.confirm_password:
            user_id = uuid.uuid4()
            if database_service.register_user(user_id, payload.username, payload.email, payload.password, "",
                                              True, False, "", "", 1, False) == 0:
                token = generate_token(user_id)
                database_service.add_token_db(user_id, token)
                return {
                    "token": token,
                    "user_id": user_id,
                    "role": 1,
                    "email": payload.email,
                    "username": payload.username
                }
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

    def update_user(self, payload: UpdateUser, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            if (21 > payload.type) and (payload.type > 0):
                database_service.update_user_db(token_data['user_id'], payload.username, payload.gender, payload.birth_date,
                                                payload.request, payload.city, payload.description, payload.type)
                return "Successfully"
            else:
                return "error"
        except(Error):
            return "error"


user_service: UserServise = UserServise()
