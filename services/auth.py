import jwt
from datetime import datetime, timedelta

# Функция для генерации JWT токена
def generate_token(user_id):
    # Установка срока действия токена (1 час)
    expiry = datetime.utcnow() + timedelta(hours=1)

    # Создание токена с идентификатором пользователя и сроком действия
    token = jwt.encode({'user_id': user_id, 'exp': expiry}, 'secret_key', algorithm='HS256')

    return token

# Функция для проверки JWT токена
def verify_token(token):
    try:
        # Проверка токена и декодирование его содержимого
        payload = jwt.decode(token, 'secret_key', algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # Обработка исключения при истечении срока действия токена
        return 'Token has expired'
    except jwt.InvalidTokenError:
        # Обработка других недопустимых токенов
        return 'Invalid token'