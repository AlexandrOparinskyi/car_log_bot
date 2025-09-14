from datetime import date

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, Button, Calendar

from bot.states import ServiceState, ServiceWorkState
from bot.utils import (replace_dot_at_comma,
                       get_car_by_id)


async def select_service_type(callback: CallbackQuery,
                              widget: Select,
                              dialog_manager: DialogManager,
                              item_id: str):
    dialog_manager.dialog_data.update(service_type=item_id)

    await dialog_manager.switch_to(state=ServiceState.edit_menu)


async def service_edit_param(callback: CallbackQuery,
                             widget: Select,
                             dialog_manager: DialogManager,
                             item_id: str):
    dialog_manager.dialog_data.update(service_param=item_id)

    if item_id in ("car", "service_type", "date"):
        await dialog_manager.switch_to(state=ServiceState.param_edit_button)
        return

    await dialog_manager.switch_to(state=ServiceState.param_edit_text)


async def enter_service_param(message: Message,
                              widget: MessageInput,
                              dialog_manager: DialogManager):
    service_param = dialog_manager.dialog_data.get("service_param")
    m_text = message.text

    if service_param == "total_price":
        m_text = replace_dot_at_comma(m_text)

    dialog_manager.dialog_data[service_param] = m_text

    await dialog_manager.switch_to(state=ServiceState.edit_menu)


async def select_service_param_button(callback: CallbackQuery,
                                      widget: Select,
                                      dialog_manager: DialogManager,
                                      item_id: str):
    if item_id == "select_date":
        await dialog_manager.switch_to(state=ServiceState.calendar)
        return

    service_param = dialog_manager.dialog_data.get("service_param")

    if service_param == "car":
        item_id = await get_car_by_id(int(item_id))

    dialog_manager.dialog_data[service_param] = item_id

    await dialog_manager.switch_to(state=ServiceState.edit_menu)


async def service_edit_calendar(callback: CallbackQuery,
                                widget,
                                dialog_manager: DialogManager,
                                selected_date: date):
    dialog_manager.dialog_data.update(date=selected_date)

    await dialog_manager.switch_to(state=ServiceState.edit_menu)


async def service_add_part_or_work(callback: CallbackQuery,
                                   button: Button,
                                   dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(add_param=callback.data)

    await dialog_manager.start(state=ServiceWorkState.work_name,
                               data={**dialog_manager.dialog_data})


async def enter_service_work_or_part_name(message: Message,
                                          widget: MessageInput,
                                          dialog_manager: DialogManager):
    data = {}
    lst_params = message.text.split("\n")

    if widget.widget_id == "service_work":
        for num, param in enumerate(lst_params, 1):
            print(num, param)
