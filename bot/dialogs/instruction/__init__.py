from aiogram import Router

from .dialogs import instruction_dialog
from .handlers import *


def register_instruction_dialogs(router: Router):
    router.include_router(instruction_dialog)


__all__ = ["instruction_button",
           "register_instruction_dialogs"]
