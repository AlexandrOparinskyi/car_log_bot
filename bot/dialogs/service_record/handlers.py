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
    dialog_manager.dialog_data.update(service_param=callback.data)

    if callback.data == "service_add_work_button":
        await dialog_manager.start(state=ServiceWorkState.work_name,
                                   data={**dialog_manager.dialog_data})
        return

    if callback.data == "service_add_part_button":
        # Здесь будет добавление запчастей
        await callback.answer("Okay")
        return


async def enter_service_work_or_part_name(message: Message,
                                          widget: MessageInput,
                                          dialog_manager: DialogManager):
    service_work_data = dialog_manager.dialog_data.get("service_work_data")
    data = {}
    counter = 1
    lst_params = message.text.split("\n")

    if service_work_data:
        data = service_work_data
        counter = len(service_work_data) + 1

    for num, param in enumerate(lst_params, counter):
        data[num] = {"name": param}

    if widget.widget_id == "service_work":
        dialog_manager.dialog_data.update(service_work_data=data,
                                          selected_work=counter,
                                          add_param=widget.widget_id)
        await dialog_manager.switch_to(state=ServiceWorkState.edit_menu)
        return


async def paginator_handler(callback: CallbackQuery,
                            widget: Select,
                            dialog_manager: DialogManager,
                            item_id: str):
    selected_work = dialog_manager.dialog_data.get("selected_work")
    add_param = dialog_manager.dialog_data.get("add_param")

    if item_id == "selected_work":
        await callback.answer()
        return

    if item_id == "next":
        if add_param == "service_work":
            service_work_data = dialog_manager.dialog_data.get(
                "service_work_data"
            )
            if selected_work + 1 > len(service_work_data):
                return
            dialog_manager.dialog_data.update(selected_work=selected_work + 1)

    if item_id == "prev":
        if add_param == "service_work":
            if selected_work - 1 == 0:
                return
            dialog_manager.dialog_data.update(selected_work=selected_work - 1)

    await dialog_manager.update(dialog_manager.dialog_data)


async def add_work_button(callback: CallbackQuery,
                          button: Button,
                          dialog_manager: DialogManager,):
    await dialog_manager.switch_to(state=ServiceWorkState.work_name)


async def delete_service_work_button(callback: CallbackQuery,
                                     button: Button,
                                     dialog_manager: DialogManager):
    service_work_data = dialog_manager.dialog_data.get("service_work_data")
    selected_work = dialog_manager.dialog_data.get("selected_work")
    data = {}
    counter = 1

    for key, value in service_work_data.items():
        if key != selected_work:
            data[counter] = value
            counter += 1

    if selected_work == len(service_work_data):
        selected_work -= 1

    dialog_manager.dialog_data.update(service_work_data=data,
                                      selected_work=selected_work)

    if not data:
        await dialog_manager.start(state=ServiceState.edit_menu,
                                   data={**dialog_manager.dialog_data})
        return

    await dialog_manager.switch_to(state=ServiceWorkState.edit_menu)


async def select_service_work_edit_param(callback: CallbackQuery,
                                         widget: Select,
                                         dialog_manager: DialogManager,
                                         item_id: str):
    dialog_manager.dialog_data.update(service_work_param=item_id)

    await dialog_manager.switch_to(state=ServiceWorkState.param_edit_text)


async def enter_service_work_edit_param(message: Message,
                                        widget: MessageInput,
                                        dialog_manager: DialogManager):
    service_work_data = dialog_manager.dialog_data.get("service_work_data")
    service_work_param = dialog_manager.dialog_data.get("service_work_param")
    selected_work = dialog_manager.dialog_data.get("selected_work")
    m_text = message.text

    if service_work_param == "price":
        m_text = replace_dot_at_comma(m_text)

    service_work_data[selected_work][service_work_param] = m_text
    dialog_manager.dialog_data.update(service_work_data=service_work_data)

    await dialog_manager.switch_to(state=ServiceWorkState.edit_menu)
