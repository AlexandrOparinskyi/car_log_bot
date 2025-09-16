from datetime import date

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Select, Button

from bot.states import (ServiceState,
                        ServiceWorkState,
                        ServicePartState,
                        HomeState)
from bot.utils import (replace_dot_at_comma,
                       get_car_by_id,
                       create_service_record,
                       create_service_work_record)
from database import ServiceTypeEnum, ServiceWork, ServicePart


async def select_service_type(callback: CallbackQuery,
                              widget: Select,
                              dialog_manager: DialogManager,
                              item_id: str):
    now_date = date.today()
    title = (f"{ServiceTypeEnum[item_id].value} "
             f"{now_date.strftime('%d.%m.%Y')}")
    dialog_manager.dialog_data.update(service_type=item_id,
                                      date=now_date,
                                      title=title)

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


async def service_add_work(callback: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(service_param=callback.data)

    service_work_data = dialog_manager.dialog_data.get("service_work_data")
    if service_work_data:
        dialog_manager.dialog_data.update(add_param="service_work")
        await dialog_manager.start(state=ServiceWorkState.edit_menu,
                                   data={**dialog_manager.dialog_data})
        return

    await dialog_manager.start(state=ServiceWorkState.work_name,
                               data={**dialog_manager.dialog_data})


async def service_add_part(callback: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(service_param=callback.data)
    service_part_data = dialog_manager.dialog_data.get("service_part_data")

    if service_part_data:
        dialog_manager.dialog_data.update(add_param="service_part")
        await dialog_manager.start(state=ServicePartState.edit_menu,
                                   data={**dialog_manager.dialog_data})
        return

    await dialog_manager.start(state=ServicePartState.part_name,
                               data={**dialog_manager.dialog_data})


async def enter_service_work_name(message: Message,
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

    dialog_manager.dialog_data.update(service_work_data=data,
                                      selected_work=counter,
                                      add_param=widget.widget_id)

    await dialog_manager.switch_to(state=ServiceWorkState.edit_menu)


async def enter_service_part_name(message: Message,
                                  widget: MessageInput,
                                  dialog_manager: DialogManager):
    service_part_data = dialog_manager.dialog_data.get("service_part_data")

    data = {}
    counter = 1
    lst_params = message.text.split("\n")

    if service_part_data:
        data = service_part_data
        counter = len(service_part_data) + 1

    for num, param in enumerate(lst_params, counter):
        data[num] = {"name": param, "quantity": 1}

    dialog_manager.dialog_data.update(service_part_data=data,
                                      selected_part=counter,
                                      add_param=widget.widget_id)

    await dialog_manager.switch_to(state=ServicePartState.edit_menu)


async def paginator_handler(callback: CallbackQuery,
                            widget: Select,
                            dialog_manager: DialogManager,
                            item_id: str):
    selected_work = dialog_manager.dialog_data.get("selected_work")
    selected_part = dialog_manager.dialog_data.get("selected_part")
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
        if add_param == "service_part":
            service_part_data = dialog_manager.dialog_data.get(
                "service_part_data"
            )
            if selected_part + 1 > len(service_part_data):
                return
            dialog_manager.dialog_data.update(selected_part=selected_part + 1)

    if item_id == "prev":
        if add_param == "service_work":
            if selected_work - 1 == 0:
                return
            dialog_manager.dialog_data.update(selected_work=selected_work - 1)
        if add_param == "service_part":
            if selected_part - 1 == 0:
                return
            dialog_manager.dialog_data.update(selected_part=selected_part - 1)

    await dialog_manager.update({**dialog_manager.dialog_data})


async def add_work_button(callback: CallbackQuery,
                          button: Button,
                          dialog_manager: DialogManager, ):
    await dialog_manager.switch_to(state=ServiceWorkState.work_name)


async def add_part_button(callback: CallbackQuery,
                          button: Button,
                          dialog_manager: DialogManager, ):
    await dialog_manager.switch_to(state=ServicePartState.part_name)


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


async def delete_service_part_button(callback: CallbackQuery,
                                     button: Button,
                                     dialog_manager: DialogManager):
    service_part_data = dialog_manager.dialog_data.get("service_part_data")
    selected_part = dialog_manager.dialog_data.get("selected_part")
    data = {}
    counter = 1

    for key, value in service_part_data.items():
        if key != selected_part:
            data[counter] = value
            counter += 1

    if selected_part == len(service_part_data):
        selected_part -= 1

    dialog_manager.dialog_data.update(service_part_data=data,
                                      selected_part=selected_part)

    if not data:
        await dialog_manager.start(state=ServiceState.edit_menu,
                                   data={**dialog_manager.dialog_data})
        return

    await dialog_manager.switch_to(state=ServicePartState.edit_menu)


async def select_service_work_edit_param(callback: CallbackQuery,
                                         widget: Select,
                                         dialog_manager: DialogManager,
                                         item_id: str):
    dialog_manager.dialog_data.update(service_work_param=item_id)

    await dialog_manager.switch_to(state=ServiceWorkState.param_edit_text)


async def select_service_part_edit_param(callback: CallbackQuery,
                                         widget: Select,
                                         dialog_manager: DialogManager,
                                         item_id: str):
    dialog_manager.dialog_data.update(service_part_param=item_id)

    await dialog_manager.switch_to(state=ServicePartState.param_edit_text)


async def enter_service_work_edit_param(message: Message,
                                        widget: MessageInput,
                                        dialog_manager: DialogManager):
    service_work_data = dialog_manager.dialog_data.get("service_work_data")
    service_work_param = dialog_manager.dialog_data.get("service_work_param")
    selected_work = dialog_manager.dialog_data.get("selected_work")
    i18n = dialog_manager.middleware_data.get("i18n")
    m_text = message.text

    if service_work_param == "price":
        try:
            m_text = replace_dot_at_comma(m_text)
            float(m_text)
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            error_text = i18n.service.edit.total.price.error.text()
            await message.answer(
                text=error_text
            )
            return

    if service_work_param == "price":
        service_work_data[selected_work][service_work_param] = float(m_text)
    else:
        service_work_data[selected_work][service_work_param] = float(m_text)

    dialog_manager.dialog_data.update(service_work_data=service_work_data)

    await dialog_manager.switch_to(state=ServiceWorkState.edit_menu)


async def enter_service_part_edit_param(message: Message,
                                        widget: MessageInput,
                                        dialog_manager: DialogManager):
    service_part_data = dialog_manager.dialog_data.get("service_part_data")
    service_part_param = dialog_manager.dialog_data.get("service_part_param")
    selected_part = dialog_manager.dialog_data.get("selected_part")
    i18n = dialog_manager.middleware_data.get("i18n")
    m_text = message.text

    if service_part_param in ("price", "total_price"):
        try:
            m_text = replace_dot_at_comma(m_text)
            float(m_text)
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            error_text = i18n.service.edit.total.price.error.text()
            await message.answer(
                text=error_text
            )
            return

    if service_part_param == "quantity":
        try:
            int(m_text)
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            error_text = i18n.service.part.edit.quantity.error.text()
            await message.answer(
                text=error_text
            )
            return

    if service_part_param == "quantity":
        service_part_data[selected_part][service_part_param] = int(m_text)
    elif service_part_param in ("price_per_unit", "total_price"):
        service_part_data[selected_part][service_part_param] = float(m_text)
    else:
        service_part_data[selected_part][service_part_param] = m_text

    dialog_manager.dialog_data.update(service_part_data=service_part_data)

    await dialog_manager.switch_to(state=ServicePartState.edit_menu)


async def save_button(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    service_id = await create_service_record(**dialog_manager.dialog_data)
    await create_service_work_record(
        ServiceWork,
        dialog_manager.dialog_data.get("service_work_data"),
        int(service_id)
    )
    await create_service_work_record(
        ServicePart,
        dialog_manager.dialog_data.get("service_part_data"),
        int(service_id)
    )
    await dialog_manager.start(state=HomeState.home)
