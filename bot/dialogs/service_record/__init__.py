from aiogram import Router

from .dialogs import service_dialog


def register_service_dialogs(router: Router):
    router.include_router(service_dialog)
