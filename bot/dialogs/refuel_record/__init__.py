from aiogram import Router

from .dialogs import refuel_dialog


def register_refuel_dialogs(router: Router):
    router.include_router(refuel_dialog)