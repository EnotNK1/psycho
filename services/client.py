from database.database import database_service
from schemas.users import GetClient
from services.auth import verify_token
import uuid



class ClientService:

    def get_client(self, payload: GetClient, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 0 or role == 2:
            items = database_service.getClient(payload.user_id)
            return items
        else:
            return "access denied"

    def get_list_client(self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 0 or role == 2:
            items = database_service.getListClient(token_data['user_id'])
            return items
        else:
            return "access denied"


client_service: ClientService = ClientService()