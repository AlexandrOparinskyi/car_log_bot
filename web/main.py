from fastapi import FastAPI, Request
from sqladmin import Admin

from database import engine
from .auth import SingleUserAuth
from .views import UserAdmin

app = FastAPI()
authentication_backend = SingleUserAuth()
admin = Admin(app=app,
              engine=engine,
              authentication_backend=authentication_backend,
              title="Admin panel",
              base_url="/")

admin.add_view(UserAdmin)


@app.middleware("http")
async def correct_scheme_middleware(request: Request, call_next):
    # Принудительно устанавливаем схему как HTTPS
    request.scope["scheme"] = "https"
    response = await call_next(request)
    return response
