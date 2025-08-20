from aiogram import Router

from .dialogs import home_dialog


def register_home_dialogs(router: Router):
    router.include_router(home_dialog)