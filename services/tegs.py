from database.database import database_service
from services.auth import verify_token
from psycopg2 import Error




class TegsService:


    def get_list_tegs (self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.get_list_tegs()
            return result
        except(Error):
            return "error"


tegs_service: TegsService = TegsService()