from sqladmin import ModelView

from database.models.users import Users, Daily_task
from database.models.review import Review


class UsersAdmin(ModelView, model=Users):
    column_list = [Users.id, Users.email]
    column_details_exclude_list = [Users.password]
    can_delete = False
    name_plural = "Users"
    name = "User"
    icon = "fa-solid fa-user"

class ReviewAdmin(ModelView, model=Review):
    column_list = [Review.text, Review.email]
    name_plural = "Reviews"
    name = "Review"

class DailyTaskAdmin(ModelView, model=Daily_task):
    name_plural = "Daily_tasks"
    name = "Daily_task"