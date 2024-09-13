from database.services.users import user_service_db
from database.services.belief import bser_service_db
from schemas.problem import CheckBelief, BeliefAnalysis, CreateDeepConviction
from utils.token_utils import check_token
import uuid




class BeliefService:

    def create_deep_conviction(self, payload: CreateDeepConviction, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 2 or role == 3:
            bser_service_db.create_deep_conviction_db(uuid.UUID(payload.problem_id), payload.disadaptive,
                                                       payload.adaptive)
            return "Successfully"
        else:
            return "access denied"

    def save_belief_analysis(self, payload: BeliefAnalysis, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 2 or role == 3:
            bser_service_db.save_belief_analysis_db(uuid.UUID(payload.intermediate_conviction_id), payload.text,
                                                       payload.feeling_and_actions, payload.motivation, payload.hindrances,
                                                       payload.incorrect_victims, payload.results)
            return "Successfully"
        else:
            return "access denied"

    def save_belief_check(self, payload: CheckBelief, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 2 or role == 3:
            bser_service_db.save_belief_check_db(uuid.UUID(payload.intermediate_conviction_id), payload.truthfulness,
                                                     payload.consistency, payload.usefulness)
            return "Successfully"
        else:
            return "access denied"

    def get_belief_analysis(self, intermediate_conviction_id: str, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 2 or role == 3:
            result = bser_service_db.get_belief_analysis(uuid.UUID(intermediate_conviction_id))
            return result
        else:
            return "access denied"

    def get_belief_check(self, intermediate_conviction_id: str, access_token):
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 2 or role == 3:
            result = bser_service_db.get_belief_check(uuid.UUID(intermediate_conviction_id))
            return result
        else:
            return "access denied"


belief_service: BeliefService = BeliefService()