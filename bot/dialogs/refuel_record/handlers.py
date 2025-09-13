from datetime import datetime

from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import ManagedCheckbox, Select, Button

from bot.states import RefuelState, HomeState
from bot.utils import (create_refuel_record,
                       replace_dot_at_comma,
                       get_car_by_id)


async def enter_total_price_refuel(message: Message,
                                   widget: MessageInput,
                                   dialog_manager: DialogManager):
    m_text = replace_dot_at_comma(message.text)
    dialog_manager.dialog_data.update(total_price=m_text)

    await dialog_manager.switch_to(state=RefuelState.edit_menu)


async def refuel_edit_params(callback: CallbackQuery,
                             widget: Select,
                             dialog_manager: DialogManager,
                             item_id: str):
    dialog_manager.dialog_data.update(refuel_param=item_id)

    if item_id in ("total_price", "liters", "comment"):
        await dialog_manager.switch_to(state=RefuelState.edit_to_text)
        return

    await dialog_manager.switch_to(state=RefuelState.edit_to_button)


async def enter_refuel_param(message: Message,
                             widget: MessageInput,
                             dialog_manager: DialogManager):
    refuel_param = dialog_manager.dialog_data.get("refuel_param")
    m_text = message.text

    if refuel_param in ("total_price", "liters"):
        m_text = replace_dot_at_comma(message.text)

    dialog_manager.dialog_data[refuel_param] = m_text

    await dialog_manager.switch_to(state=RefuelState.edit_menu)


async def select_refuel_param_button(callback: CallbackQuery,
                                     widget: Select,
                                     dialog_manager: DialogManager,
                                     item_id: str):
    if item_id == "select_date":
        await callback.answer("В разработке")
        return

    refuel_param = dialog_manager.dialog_data.get("refuel_param")

    if refuel_param == "car":
        item_id = await get_car_by_id(int(item_id))

    if refuel_param == "date":
        date = list(map(int, item_id.split("-")))
        item_id = datetime(*date)

    dialog_manager.dialog_data[refuel_param] = item_id

    await dialog_manager.switch_to(state=RefuelState.edit_menu)


async def full_tank_checkbox(callback: CallbackQuery,
                             checkbox: ManagedCheckbox,
                             dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(full_tank=checkbox.is_checked())


async def save_refuel(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    await create_refuel_record(**dialog_manager.dialog_data)
    i18n = dialog_manager.middleware_data.get("i18n")

    await callback.answer(i18n.refuel.success.added.text())
    await dialog_manager.start(state=HomeState.home)
