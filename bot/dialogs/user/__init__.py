from aiogram import Router

from .dialogs import user_dialog
from .handlers import user_home_button


def register_user_dialogs(router: Router):
    router.include_router(user_dialog)


__all__ = ["user_home_button",
           "register_user_dialogs"]
