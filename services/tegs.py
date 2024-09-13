from database.services.tegs import tegs_service_db
from psycopg2 import Error
from utils.token_utils import check_token

class TegsService:
    def get_list_tegs (self, access_token):
        token_data = check_token(access_token)

        try:
            result = tegs_service_db.get_list_tegs()
            return result
        except(Error):
            return "error"


tegs_service: TegsService = TegsService()