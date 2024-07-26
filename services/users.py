from schemas.users import Creds, Reg, ResetPassword, UpdateUser, UserResponse, UserData
from database.database import database_service
from services.auth import send_email
from services.auth import generate_token
import uuid
from starlette.responses import Response
from smtplib import SMTPRecipientsRefused
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


app = FastAPI()

items = {"foo": "The Foo Wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


class UserServise:

    def get_users(self, access_token) -> list or str:
        token_data = check_token(access_token)

        role = database_service.check_role(uuid.UUID(token_data['user_id']))

        if role == 0:
            items = database_service.get_all_users()
            return items
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")


    def get_data_user(self, access_token: str) -> UserData:
        try:
            # Проверяем токен и получаем данные из него
            token_data = check_token(access_token)
            user_id = uuid.UUID(token_data['user_id'])  # Извлекаем user_id из токена

            # Получаем данные пользователя
            user_data = database_service.get_data_user(user_id)
            if user_data is None:
                raise HTTPException(status_code=404, detail="Пользователь не найден")

            return UserData(**user_data)

        except ValueError as ve:
            # Логируем деталь ошибки
            raise HTTPException(status_code=400, detail=f"Некорректный токен: {ve}")
        except HTTPException as he:
            # Логируем деталь ошибки
            raise he
        except Exception as e:
            # Логируем деталь ошибки
            raise HTTPException(status_code=500, detail=f"Внутренняя ошибка сервера: {e}")
        # token_data = check_token(access_token)
        #
        # role = database_service.check_role(uuid.UUID(token_data['user_id']))
        #
        # if role == 0 or role == 1 or role == 2:
        #     items = database_service.get_all_users()
        #     return items
        # else:
        #     raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")


    def authorization(self, payload: Creds, response: Response):
         if database_service.check_user(payload.email, payload.password) == 0:
            user = database_service.get_user(payload.email)
            if user == -1:
                raise HTTPException(status_code=404,
                                    detail="Пользователя с такими данными не найдено!")
            print(user)
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
         else: raise HTTPException(status_code=404, detail="Пользователя с такими данными не найдено!")


    def authorization_token(self, payload, response: Response):

        user = database_service.get_user_by_token(payload.token)
        if user == 0:
            raise HTTPException(status_code=400, detail="Не валидный токен!")
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

    def register(self, payload: Reg, response: Response) -> UserResponse:

        if payload.password == payload.confirm_password:
            user_id = uuid.uuid4()
            if database_service.register_user(user_id, payload.username, payload.email, payload.password, "",
                                              True, False, "", "", 1, False) == 0:
                token = generate_token(user_id)
                database_service.add_token_db(user_id, token)
                new_user = UserResponse(token=token, user_id=user_id, role=1, email=payload.email, username=payload.username)
                response.set_cookie(key="access_token", value=token, httponly=True)
                return new_user
            else:
                raise HTTPException(status_code=409, detail="Пользователь с таким адресом электронной почты уже зарегистрирован")
        else:
            raise HTTPException(status_code=400, detail="Пароли не совпадают!")

    def reset_password(self, payload: ResetPassword) -> str:

        if database_service.get_id_user(payload.email) != -1:
            try:
                user_password = database_service.get_password_user(payload.email)
                subject = "Password Reset"
                message = f"Your password is: {user_password}"
                send_email(payload.email, subject, message)
                return "The password email has been sent"
            except SMTPRecipientsRefused:
                raise HTTPException(status_code=400, detail="Email введен неверно!")
        else:
            raise HTTPException(status_code=404, detail="Ни один пользователь с этой учетной записью электронной почты не найден!")

    def update_user(self, payload: UpdateUser, access_token):
        token_data = check_token(access_token)

        try:
            if (21 > payload.type) and (payload.type > 0):
                database_service.update_user_db(token_data['user_id'], payload.username, payload.gender, payload.birth_date,
                                                payload.request, payload.city, payload.description, payload.type)
                return "Successfully"
            else:
                raise HTTPException(status_code=400, detail="Тип пользователя введен неверно!")
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")


user_service: UserServise = UserServise()
