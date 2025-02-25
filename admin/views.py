from sqladmin import ModelView

from database.models.users import Users, Daily_task
from database.models.review import Review
from database.models.test import Test, Question, Answer_choice, Scale, Scale_result, Borders, Test_result
from database.models.education import Educational_theme, Educational_material


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

class TestAdmin(ModelView, model=Test):
    column_list = [Test.title]
    name_plural = "Tests"
    name = "Test"

class BordersAdmin(ModelView, model=Borders):
    column_list = [Borders.title]
    name_plural = "Borders"
    name = "Border"

class TestResAdmin(ModelView, model=Test_result):
    name_plural = "Test_results"
    name = "Test_result"

class QuestionAdmin(ModelView, model=Question):
    column_list = [Question.text]
    name_plural = "Questions"
    name = "Question"

class AnswerAdmin(ModelView, model=Answer_choice):
    column_list = [Answer_choice.text]
    name_plural = "Answer_choices"
    name = "Answer_choice"

class ScaleAdmin(ModelView, model=Scale):
    column_list = [Scale.title]
    name_plural = "Scales"
    name = "Scale"

class ScaleResAdmin(ModelView, model=Scale_result):
    name_plural = "Scale_results"
    name = "Scale_result"
class EducationAdmin(ModelView, model=Educational_theme):
    column_list = [Educational_theme.theme]
    name_plural = "Educations"
    name = "Education"

class EducationMaterialAdmin(ModelView, model=Educational_material):
    # column_list = [Educational_material.text]
    name_plural = "Educational_materials"
    name = "Educational_material"