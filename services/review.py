from schemas.review import ReviewCreate, ReviewRead
from database.services.users import user_service_db
from database.services.review import review_service_db
from services.auth import send_email
from services.auth import generate_token
import uuid
from starlette.responses import Response
from smtplib import SMTPRecipientsRefused
from psycopg2 import Error
from fastapi import FastAPI, HTTPException
from utils.token_utils import check_token


class ReviewService:

    def create_review(self, payload: ReviewCreate, access_token: str):
        token_data = check_token(access_token)
        user_email = user_service_db.get_email_by_id(uuid.UUID(token_data['user_id']))

        if user_email is None:
            raise HTTPException(status_code=404, detail="Пользователь не найден")

        review_data = {"text": payload.text, "email": user_email}
        result = review_service_db.create_review(review_data)
        return result

    def get_reviews(self, access_token: str) -> list[ReviewRead]:
        token_data = check_token(access_token)

        role = user_service_db.check_role(uuid.UUID(token_data['user_id']))
        if role == 0:
            reviews = review_service_db.get_all_reviews()
            return reviews
        else:
            raise HTTPException(status_code=403, detail="У вас недостаточно прав для выполнения данной операции!")



        # token_data = check_token(access_token)
        # reviews = review_service_db.get_all_reviews()
        #
        #
        # return [ReviewRead(**review) for review in reviews]

    def mark_review_as_read(self, review_id: uuid.UUID, access_token: str) -> str:
        token_data = check_token(access_token)
        review_service_db.mark_review_as_read(review_id)
        return "Отзыв помечен как прочитанный"

    def delete_review(self, review_id: uuid.UUID, access_token: str) -> str:
        token_data = check_token(access_token)
        review_service_db.delete_review(review_id)
        return "Отзыв успешно удален"

review_service: ReviewService = ReviewService()