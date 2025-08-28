from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Format

from .getters import getter_total_price
from states import RefuelState

refuel_dialog = Dialog(
    Window(
        Format("{total_price_text}"),
        getter=getter_total_price,
        state=RefuelState.total_price
    )
)