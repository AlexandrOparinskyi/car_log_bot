from typing import Optional

from fastapi import Request
from sqladmin.authentication import AuthenticationBackend

from config import Config, get_config


class SingleUserAuth(AuthenticationBackend):
    def __init__(self):
        config: Config = get_config()
        self.username = config.admin_panel.username
        self.password = config.admin_panel.password

        super().__init__(config.admin_panel.secret_key)

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        # Простая проверка на единственного пользователя
        if username == self.username and password == self.password:
            # Сохраняем факт входа в сессию
            request.session.update({"authenticated": True})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        # Просто очищаем сессию
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        # Проверяем, авторизован ли пользователь
        return request.session.get("authenticated", False)
