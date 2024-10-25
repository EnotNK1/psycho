from sqladmin import Admin

from admin.views import *
from database.database import engine
from app.app import app

admin = Admin(app, engine)

admin.add_view(UsersAdmin)
admin.add_view(ReviewAdmin)
