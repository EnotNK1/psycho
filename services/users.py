from schemas.users import Creds, Reg, ResetPassword, AddProblem, SaveTestRes, CreateTest, GetTestRes, UpdateUser, \
    Psychologist, GetClient, SendАpplication, ConfirmApplication, ProblemAnalysisCreate, CreateDeepConviction, \
    BeliefAnalysis, WritingFreeDiary, WatchApplication, GetBeliefAnalysis, CheckBelief, WritingThinkDiary, \
    ReadThinkDiary, ProblemAnalysisGet, WritingRIDialog, ReadRIDialog
from database.database import database_service
from services.auth import send_email
from services.auth import generate_token, verify_token
import uuid
from starlette.responses import JSONResponse, Response
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
            user_id = database_service.get_id_user(payload.email)

            token = generate_token(user_id)
            response.set_cookie(key="access_token", value=token, httponly=True)
            database_service.add_token_db(user_id, token)
            return token
        else:
            return "error"

    def register(self, payload: Reg) -> str:

        if payload.password == payload.confirm_password:
            user_id = uuid.uuid4()
            if database_service.register_user(user_id, payload.username, payload.email, payload.password, "",
                                              False, False, "", "", 1, False) == 0:
                token = generate_token(user_id)
                database_service.add_token_db(user_id, token)
                return token
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
            database_service.update_user_db(token_data['user_id'], payload.username, payload.gender, payload.birth_date,
                                            payload.request, payload.city, payload.description, payload.type)

            return "Successfully"
        except(Error):
            return "error"

    def psychologist_sent(self, payload: Psychologist, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.psychologist_sent_db(token_data['user_id'], payload.username, payload.title, payload.document,
                                                  payload.description,
                                                  payload.city, payload.online, payload.face_to_face, payload.gender,
                                                  payload.birth_date,
                                                  payload.request)
            if result != -1:
                return "Successfully"
            else:
                return "error"
        except(Error):
            return "error"

    def add_problem(self, payload: AddProblem, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.add_problem_db(token_data['user_id'], payload.description, payload.goal)
            return "Successfully"
        except(Error):
            return "error"

    def save_test_result(self, payload: SaveTestRes, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.save_test_result_db(token_data['user_id'], payload.title, uuid.UUID(payload.test_id),
                                                 payload.date, payload.score)
            return "Successfully"
        except(Error):
            return "error"

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
            return "Invalid token"

        res_list = database_service.get_test_res_db(token_data['user_id'], uuid.UUID(payload.test_id))

        return res_list

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

    def send_application(self, payload: SendАpplication, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(payload.user_id)
        if role == 2 and token_data['user_id'] != payload.user_id:
            database_service.send_application_db(token_data['user_id'], payload.user_id, payload.text)
            return "Successfully"
        else:
            return "error"

    def confirm_application(self, payload: ConfirmApplication, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"
        role = database_service.check_role(token_data['user_id'])
        if role == 2:
            database_service.confirm_application_db(token_data['user_id'], payload.user_id, payload.status)
            return "Successfully"
        else:
            return "error"

    def get_psycholog(self, payload: GetClient, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        role1 = database_service.check_role(uuid.UUID(payload.user_id))
        if role == 1 and role1 == 2:
            items = database_service.get_psycholog(payload.user_id)
            return items
        else:
            return "access denied"

    def get_list_psycholog(self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 1 or role == 2:
            items = database_service.get_list_psycholog(token_data['user_id'])
            return items
        else:
            return "access denied"


    def save_problem_analysis(self, payload: ProblemAnalysisCreate, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':
            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            database_service.save_problem_analysis_db(uuid.UUID(payload.problem_id), payload.type)
            return "Successfully"
        else:
            return "access denied"

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


    def writing_free_diary(self, payload: WritingFreeDiary, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.writing_free_diary_db(token_data['user_id'], payload.text)
            return "Successfully"
        except(Error):
            return "error"

    def writing_think_diary(self, payload: WritingThinkDiary, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.writing_think_diary_db(token_data['user_id'], payload.deep_conviction_id, payload.situation,
                                                   payload.mood, payload.level, payload.auto_thought, payload.proofs,
                                                   payload.refutations, payload.new_mood, payload.new_level, payload.behaviour)
            return "Successfully"
        except(Error):
            return "error"


    def reading_free_diary(self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.reading_free_diary_db(token_data['user_id'])
            return result
        except(Error):
            return "error"

    def reading_think_diary(self, payload: ReadThinkDiary, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.reading_think_diary_db(payload.think_diary_id)
            return result
        except(Error):
            return "error"

    def get_list_applications(self, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"


        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            result = database_service.get_list_applications_db(token_data['user_id'])
            return result
        else:
            return "access denied"

    def watch_application(self, payload: WatchApplication, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"


        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            result = database_service.watch_application_db(token_data['user_id'], payload.app_id)
            return result
        else:
            return "access denied"

    def get_problem_analysis(self, payload: ProblemAnalysisGet, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        role = database_service.check_role(uuid.UUID(token_data['user_id']))
        if role == 2:
            result = database_service.get_problem_analysis_db(payload.problem_id)
            return result
        else:
            return "access denied"

    def writing_r_i_dialog(self, payload: WritingRIDialog, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            database_service.writing_r_i_dialog_db(payload.problem_id, payload.text, payload.type)
            return "Successfully"
        except(Error):
            return "error"

    def reading_r_i_dialog(self, payload: ReadRIDialog, access_token):
        if not access_token:
            return "not token"
        token_data = verify_token(access_token)

        if token_data == 'Token has expired':

            return "Token has expired"
        elif token_data == 'Invalid token':
            return "Invalid token"

        try:
            result = database_service.reading_r_i_dialog_db(payload.problem_id)
            return result
        except(Error):
            return "error"

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


user_service: UserServise = UserServise()
