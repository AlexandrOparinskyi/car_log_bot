from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Format

from .filters import check_enter_refuel_total_price
from .getters import (getter_total_price,
                      getter_refuel_edit_menu)
from states import RefuelState
from .handlers import enter_total_price_refuel
from ..general import error_enter_no_text

refuel_dialog = Dialog(
    Window(
        Format("{total_price_text}"),
        MessageInput(func=enter_total_price_refuel,
                     content_types=ContentType.TEXT,
                     filter=check_enter_refuel_total_price),
        MessageInput(func=error_enter_no_text),
        getter=getter_total_price,
        state=RefuelState.total_price
    ),
    Window(
        Format("{refuel_edit_menu_text}"),
        getter=getter_refuel_edit_menu,
        state=RefuelState.edit_menu
    )
)
