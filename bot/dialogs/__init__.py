from aiogram import Router

from .garage import register_garage_dialogs
from .home import register_home_dialogs
from .instruction import register_instruction_dialogs
from .start import register_user_dialog


def register_dialogs(router: Router):
    register_user_dialog(router)
    register_home_dialogs(router)
    register_instruction_dialogs(router)
    register_garage_dialogs(router)