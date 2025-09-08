from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import StartState
from bot.utils import (create_new_car,
                       update_car_by_id)


async def enter_success_car_name(message: Message,
                                 widget: MessageInput,
                                 dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get("i18n")

    if len(message.text) > 60:
        dialog_manager.show_mode = ShowMode.NO_UPDATE

        await message.answer(
            text=i18n.error.long.first.car.name(
                len_message=len(message.text),
                current_length=60
            )
        )
        return

    car_id = await create_new_car(message.text,
                                  message.from_user.id,
                                  True)
    dialog_manager.dialog_data.update(car_id=car_id,
                                      car_name=message.text)

    await dialog_manager.next()


async def start_edit_car_button(callback: CallbackQuery,
                                widget: Select,
                                dialog_manager: DialogManager,
                                item_id: str):
    dialog_manager.dialog_data.update(part=item_id)

    if item_id in ("engine", "transmission"):
        await dialog_manager.switch_to(StartState.edit_to_button)
        return

    await dialog_manager.switch_to(state=StartState.edit_to_text)


async def start_save_car_part_button(callback: CallbackQuery,
                                     widget: Select,
                                     dialog_manager: DialogManager,
                                     item_id: str):
    part = dialog_manager.dialog_data.get("part")
    dialog_manager.dialog_data[part] = item_id

    await dialog_manager.switch_to(state=StartState.edit_car_menu)


async def start_save_car_part_enter(message: Message,
                                    widget: MessageInput,
                                    dialog_manager: DialogManager):
    part = dialog_manager.dialog_data.get("part")
    dialog_manager.dialog_data[part] = message.text

    await dialog_manager.switch_to(state=StartState.edit_car_menu)


async def save_start_car_and_exit(callback: CallbackQuery,
                                  button: Button,
                                  dialog_manager: DialogManager):
    await update_car_by_id(**dialog_manager.dialog_data)

    await dialog_manager.switch_to(state=StartState.end_acquaintance)
