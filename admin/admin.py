from sqladmin import Admin

from admin.views import *
from database.database import engine
from app.app import app

admin = Admin(app, engine)

admin.add_view(UsersAdmin)
admin.add_view(ReviewAdmin)
admin.add_view(DailyTaskAdmin)
admin.add_view(TestAdmin)
admin.add_view(QuestionAdmin)
admin.add_view(AnswerAdmin)
admin.add_view(ScaleAdmin)
admin.add_view(ScaleResAdmin)
admin.add_view(BordersAdmin)
admin.add_view(TestResAdmin)
admin.add_view(EducationAdmin)
admin.add_view(EducationMaterialAdmin)
