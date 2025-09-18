from aiogram import Router

from .dialogs import purchase_dialog


def register_purchase_dialogs(router: Router):
    router.include_router(purchase_dialog)
