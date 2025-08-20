from aiogram import Router

from .dialogs import start_dialog


def register_user_dialog(router: Router):
    router.include_router(start_dialog)