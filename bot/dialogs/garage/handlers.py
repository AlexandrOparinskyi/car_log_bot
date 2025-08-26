from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from states import GarageState, AddCarState
from utils import create_new_car, update_car_by_id


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
    car_id = await create_new_car(message.text, message.from_user.id)
    dialog_manager.dialog_data.update(car_name=message.text,
                                      car_id=car_id)

    await dialog_manager.switch_to(state=AddCarState.edit_car_menu)


async def select_part_car_to_edit(callback: CallbackQuery,
                                  widget: Select,
                                  dialog_manager: DialogManager,
                                  item_id: str):
    dialog_manager.dialog_data.update(part=item_id)

    if item_id in ("engine", "transmission"):
        await dialog_manager.switch_to(state=AddCarState.edit_to_button)
        return

    await dialog_manager.switch_to(state=AddCarState.edit_to_text)


async def save_car_part_enter(message: Message,
                              widget: MessageInput,
                              dialog_manager: DialogManager):
    part = dialog_manager.dialog_data.get("part")
    dialog_manager.dialog_data[part] = message.text

    await dialog_manager.switch_to(state=AddCarState.edit_car_menu)


async def save_car_part_button(callback: CallbackQuery,
                               widget: Select,
                               dialog_manager: DialogManager,
                               item_id: str):
    part = dialog_manager.dialog_data.get("part")
    dialog_manager.dialog_data[part] = item_id

    await dialog_manager.switch_to(state=AddCarState.edit_car_menu)


async def save_updated_car(callback: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager):
    await update_car_by_id(**dialog_manager.dialog_data)

    await dialog_manager.start(state=GarageState.garage)
