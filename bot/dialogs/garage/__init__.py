from aiogram import Router

from .dialogs import garage_dialog, add_car_dialog
from .handlers import garage_button


def register_garage_dialogs(router: Router):
    router.include_router(garage_dialog)
    router.include_router(add_car_dialog)


__all = ["register_garage_dialogs",
         "garage_button"]
