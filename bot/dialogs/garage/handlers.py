from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from states import GarageState, AddCarState


async def garage_button(callback: CallbackQuery,
                        button: Button,
                        dialog_manager: DialogManager):
    await dialog_manager.start(state=GarageState.garage)


async def car_info(callback: CallbackQuery,
                   widget: Select,
                   dialog_manager: DialogManager,
                   item_id: str):
    dialog_manager.dialog_data.update(car_id=item_id)

    await dialog_manager.switch_to(state=GarageState.car_info)


async def add_car_button(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    await dialog_manager.start(state=AddCarState.car_name)


async def enter_car_name(message: Message,
                         widget: MessageInput,
                         dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(car_name=message.text)

    await dialog_manager.switch_to(state=AddCarState.edit_car_menu)

