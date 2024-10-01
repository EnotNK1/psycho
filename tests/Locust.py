from locust import HttpUser, task, between
import json
import random


class WebsiteUser(HttpUser):
    wait_time = between(10, 15)  # время между запросами, в секундах

    @task(1)
    def register_user(self):
        reg_data = {
            "email": "test@example.com",
            "username": "testuser",
            "password": "test123",
            "confirm_password": "test123"
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/users/reg", data=json.dumps(reg_data), headers=headers)

    @task(2)
    def auth_user(self):
        creds_data = {
            "email": "test@example.com",
            "password": "test123"
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/users/auth", data=json.dumps(creds_data), headers=headers)

    @task(3)
    def reset_password(self):
        reset_data = {
            "email": "test@example.com"
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/users/reset_password", data=json.dumps(reset_data), headers=headers)

    @task(4)
    def update_user(self):
        update_data = {
            "birth_date": "2000-01-01",
            "gender": "male",
            "username": "new_username",
            "request": [1, 2, 3],
            "city": "New City",
            "description": "New Description",
            "type": 1
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/users/update_user", data=json.dumps(update_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(5)
    def get_users(self):
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.get("/users/get", cookies={'access_token': access_token})

    @task(6)
    def auth_token_user(self):
        token_data = {
            "token": "some_token_value"
        }
        headers = {'Content-Type': 'application/json'}
        response = self.client.post("/users/auth_token", data=json.dumps(token_data), headers=headers)

    @task(7)
    def save_test_result(self):
        test_data = {
            "title": "Test Title",
            "score": 80,
            "test_id": "test_id_value",
            "date": "2024-06-05T12:00:00"  # примерный формат даты и времени
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/test/save_test_result", data=json.dumps(test_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(8)
    def create_test(self):
        test_data = {
            "title": "New Test",
            "description": "Description of the new test",
            "short_desc": "Short description"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/test/create_test", data=json.dumps(test_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(9)
    def get_test_res(self):
        test_data = {
            "test_id": "test_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/test/get_test_result", data=json.dumps(test_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(10)
    def get_list_tegs(self):
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.get("/tegs/get_list_tegs", headers=headers, cookies={'access_token': access_token})

    @task(11)
    def psychologist_sent(self):
        psychologist_data = {
            "username": "Psychologist Username",
            "title": "Psychologist Title",
            "document": "Document",
            "description": "Description",
            "city": "City",
            "online": True,
            "face_to_face": False,
            "gender": "male",
            "birth_date": "1990-01-01",  # примерный формат даты
            "request": [1, 2, 3]
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/psychologist/send_psychologist", data=json.dumps(psychologist_data),
                                    headers=headers, cookies={'access_token': access_token})

    @task(12)
    def get_client(self):
        client_data = {
            "user_id": "user_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/psychologist/get_client", data=json.dumps(client_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(13)
    def get_list_client(self):
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.get("/psychologist/get_list_client", headers=headers,
                                   cookies={'access_token': access_token})

    @task(14)
    def confirm_application(self):
        application_data = {
            "user_id": "user_id_value",
            "status": True
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/psychologist/confirm_application", data=json.dumps(application_data),
                                    headers=headers, cookies={'access_token': access_token})

    @task(15)
    def get_psycholog(self):
        client_data = {
            "user_id": "user_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/client/get_psycholog", data=json.dumps(client_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(16)
    def get_list_get_psycholog(self):
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.get("/client/get_list_get_psycholog", headers=headers,
                                   cookies={'access_token': access_token})

    @task(17)
    def add_problem(self):
        problem_data = {
            "description": "Problem Description",
            "goal": "Problem Goal"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/problem/new_problem", data=json.dumps(problem_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(18)
    def save_problem_analysis(self):
        analysis_data = {
            "problem_id": "problem_id_value",
            "type": 1
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/problem/save_problem_analysis", data=json.dumps(analysis_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(19)
    def get_analysis(self):
        analysis_data = {
            "problem_id": "problem_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])  # случайный выбор токена доступа
        response = self.client.post("/problem/get_analysis", data=json.dumps(analysis_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(20)
    def writing_free_diary(self):
        diary_data = {
            "text": "Diary text"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/diary/writing_free_diary", data=json.dumps(diary_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(21)
    def reading_free_diary(self):
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.get("/diary/reading_free_diary", headers=headers, cookies={'access_token': access_token})

    @task(22)
    def writing_think_diary(self):
        think_diary_data = {
            "deep_conviction_id": "deep_conviction_id_value",
            "situation": "Situation",
            "mood": "Mood",
            "level": 1,
            "auto_thought": "Auto thought",
            "proofs": "Proofs",
            "refutations": "Refutations",
            "new_mood": "New Mood",
            "new_level": 2,
            "behaviour": "Behaviour"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/diary/writing_think_diary", data=json.dumps(think_diary_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(23)
    def reading_think_diary(self):
        think_diary_data = {
            "think_diary_id": "think_diary_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/diary/reading_think_diary", data=json.dumps(think_diary_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(24)
    def reading_r_i_dialog(self):
        dialog_data = {
            "problem_id": "problem_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/diary/reading_r_i_dialog", data=json.dumps(dialog_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(25)
    def writing_r_i_dialog(self):
        dialog_data = {
            "problem_id": "problem_id_value",
            "text": "Dialog text",
            "type": True
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/dialog/writing_r_i_dialog", data=json.dumps(dialog_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(26)
    def create_deep_conviction(self):
        conviction_data = {
            "disadaptive": "Disadaptive belief",
            "adaptive": "Adaptive belief",
            "problem_id": "problem_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/belief/create_deep_conviction", data=json.dumps(conviction_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(27)
    def save_belief_analysis(self):
        analysis_data = {
            "text": "Belief analysis text",
            "feeling_and_actions": "Feeling and actions",
            "motivation": "Motivation",
            "hindrances": "Hindrances",
            "incorrect_victims": "Incorrect victims",
            "results": "Results",
            "intermediate_conviction_id": "intermediate_conviction_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/belief/save_belief_analysis", data=json.dumps(analysis_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(28)
    def save_belief_check(self):
        check_data = {
            "truthfulness": "Truthfulness",
            "consistency": "Consistency",
            "usefulness": "Usefulness",
            "intermediate_conviction_id": "intermediate_conviction_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/belief/save_belief_check", data=json.dumps(check_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(29)
    def get_belief_analysis(self):
        analysis_data = {
            "intermediate_conviction_id": "intermediate_conviction_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/belief/get_belief_analysis", data=json.dumps(analysis_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(30)
    def get_belief_check(self):
        check_data = {
            "intermediate_conviction_id": "intermediate_conviction_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/belief/get_belief_check", data=json.dumps(check_data), headers=headers,
                                    cookies={'access_token': access_token})

    @task(32)
    def get_list_applications(self):
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.get("/application/get_list_applications", headers=headers,
                                   cookies={'access_token': access_token})

    @task(33)
    def watch_application(self):
        application_data = {
            "app_id": "app_id_value"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/application/watch_application", data=json.dumps(application_data),
                                    headers=headers, cookies={'access_token': access_token})

    @task(34)
    def send_application(self):
        application_data = {
            "user_id": "user_id_value",
            "text": "Application text"
        }
        headers = {'Content-Type': 'application/json'}
        access_token = random.choice(["access_token1", "access_token2"])
        response = self.client.post("/client/send_application", data=json.dumps(application_data), headers=headers,
                                    cookies={'access_token': access_token})
