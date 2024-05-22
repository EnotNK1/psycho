from database.database import database_service
from schemas.problem import GetBeliefAnalysis, CheckBelief, BeliefAnalysis, CreateDeepConviction
from services.auth import verify_token
import uuid




class BeliefService:

    def create_deep_conviction(self, payload: CreateDeepConviction, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            database_service.create_deep_conviction_db(uuid.UUID(payload.problem_id), payload.disadaptive,
                                                       payload.adaptive)
            return "Successfully"
        else:
            return "access denied"

    def save_belief_analysis(self, payload: BeliefAnalysis, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            database_service.save_belief_analysis_db(uuid.UUID(payload.intermediate_conviction_id), payload.text,
                                                       payload.feeling_and_actions, payload.motivation, payload.hindrances,
                                                       payload.incorrect_victims, payload.results)
            return "Successfully"
        else:
            return "access denied"

    def save_belief_check(self, payload: CheckBelief, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            database_service.save_belief_check_db(uuid.UUID(payload.intermediate_conviction_id), payload.truthfulness,
                                                     payload.consistency, payload.usefulness)
            return "Successfully"
        else:
            return "access denied"

    def get_belief_analysis(self, payload: GetBeliefAnalysis, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            result = database_service.get_belief_analysis(uuid.UUID(payload.intermediate_conviction_id))
            return result
        else:
            return "access denied"

    def get_belief_check(self, payload: GetBeliefAnalysis, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            result = database_service.get_belief_check(uuid.UUID(payload.intermediate_conviction_id))
            return result
        else:
            return "access denied"


belief_service: BeliefService = BeliefService()