from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from states import HomeState

home_dialog = Dialog(
    Window(
        Const("Главное меню"),
        state=HomeState.home
    )
)