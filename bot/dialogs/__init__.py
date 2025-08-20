from aiogram import Router

from .home import register_home_dialogs
from .start import register_user_dialog


def register_dialogs(router: Router):
    register_user_dialog(router)
    register_home_dialogs(router)