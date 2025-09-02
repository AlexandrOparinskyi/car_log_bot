from fastapi import FastAPI
from sqladmin import Admin

from database import engine
from .auth import SingleUserAuth
from .views import UserAdmin

app = FastAPI()
authentication_backend = SingleUserAuth("12345")
admin = Admin(app=app,
              engine=engine,
              authentication_backend=authentication_backend,
              title="Admin panel")

admin.add_view(UserAdmin)
