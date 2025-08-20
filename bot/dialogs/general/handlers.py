from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button, Select

from states import HomeState, StartState


async def home_button(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    await dialog_manager.start(state=HomeState.home,
                               mode=StartMode.RESET_STACK)


async def back_button(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    if callback.data == "start_back_button_to_car_edit_menu":
        await dialog_manager.switch_to(StartState.edit_car_menu)
