from database.database import database_service
import uuid
from psycopg2 import Error
from utils.token_utils import check_token
from fastapi import HTTPException
from schemas.mood_tracker import SaveMoodTracker

class MoodTrackerService:
    def get_mood_tracker(self, mood_tracker_id, access_token):
        token_data = check_token(access_token)

        try:
            res = database_service.get_mood_tracker_db(mood_tracker_id)
            return res
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def get_all_mood_tracker(self, access_token):
        token_data = check_token(access_token)

        try:
            res = database_service.get_all_mood_tracker_db(token_data['user_id'])
            return res
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")

    def save_mood_tracker(self, payload: SaveMoodTracker, access_token):
        token_data = check_token(access_token)

        try:
            res = database_service.save_mood_tracker_db(token_data['user_id'], payload.score, payload.free_diary_id,
                                                        payload.think_diary_id, payload.diary_type)
            return res
        except(Error):
            raise HTTPException(status_code=500, detail="Что-то пошло не так!")




mood_tracker_service: MoodTrackerService = MoodTrackerService()