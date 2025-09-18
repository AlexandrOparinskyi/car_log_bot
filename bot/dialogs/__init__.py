from aiogram import Router

from .garage import register_garage_dialogs
from .home import register_home_dialogs
from .instruction import register_instruction_dialogs
from .purchase import register_purchase_dialogs
from .refuel_record import register_refuel_dialogs
from .service_record import register_service_dialogs
from .start import register_user_dialog
from .user import register_user_dialogs


def register_dialogs(router: Router):
    register_user_dialog(router)
    register_home_dialogs(router)
    register_instruction_dialogs(router)
    register_garage_dialogs(router)
    register_refuel_dialogs(router)
    register_user_dialogs(router)
    register_service_dialogs(router)
    register_purchase_dialogs(router)
