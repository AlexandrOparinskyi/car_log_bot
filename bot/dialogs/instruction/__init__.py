from aiogram import Router

from .dialogs import instruction_dialog


def register_instruction_dialogs(router: Router):
    router.include_router(instruction_dialog)