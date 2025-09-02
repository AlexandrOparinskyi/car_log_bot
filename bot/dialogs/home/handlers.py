from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states import HomeState, RefuelState


async def developer_button(callback: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager):
    await dialog_manager.switch_to(HomeState.write_developer)


async def add_record_button(callback: CallbackQuery,
                        button: Button,
                        dialog_manager: DialogManager):
    await dialog_manager.switch_to(HomeState.select_record)


async def refuel_button(callback: CallbackQuery,
                        button: Button,
                        dialog_manager: DialogManager):
    await dialog_manager.start(state=RefuelState.total_price)
