from typing import Dict

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import (get_buttons_for_select_service_type,
                       get_button_for_service_edit_menu,
                       get_user_by_id,
                       get_service_data_text)
from bot.utils import get_service_edit_text_and_buttons


async def getter_select_type(i18n: TranslatorHub,
                             **kwargs) -> Dict[str, str]:
    buttons = get_buttons_for_select_service_type()

    return {"select_service_type_text": i18n.service.select.type.text(),
            "back_button": i18n.back.button(),
            "home_button": i18n.home.button(),
            "buttons": buttons}


async def getter_service_edit_menu(i18n: TranslatorHub,
                                   dialog_manager: DialogManager,
                                   event_from_user: User,
                                   **kwargs) -> Dict[str, str]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)

    user = await get_user_by_id(event_from_user.id)
    dialog_manager.dialog_data.update(user_id=user.id)
    car = user.get_selected_main_car

    if not dialog_manager.dialog_data.get("car") and car:
        dialog_manager.dialog_data.update(car=car)

    service_data = get_service_data_text(i18n,
                                         dialog_manager.dialog_data)
    service_edit_menu_text = i18n.service.edit.menu.text(
        service_data=service_data
    )
    buttons = get_button_for_service_edit_menu(i18n)

    return {"service_edit_menu_text": service_edit_menu_text,
            "buttons": buttons,
            "home_button": i18n.home.button(),
            "service_add_part_button": i18n.service.add.part.button(),
            "service_add_work_button": i18n.service.add.work.button(),
            "save_button": i18n.end.edit.car.button()}


async def getter_service_edit_param(i18n: TranslatorHub,
                                    dialog_manager: DialogManager,
                                    event_from_user: User,
                                    **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    service_param = dialog_manager.dialog_data.get("service_param")
    text, buttons = get_service_edit_text_and_buttons(i18n,
                                                      service_param,
                                                      user.active_cars)

    return {"service_edit_text": text,
            "buttons": buttons,
            "back_button": i18n.back.button()}


async def getter_service_calendar(i18n: TranslatorHub,
                                  **kwargs) -> Dict[str, str]:
    return {"service_calendar_text": i18n.service.calendar.text()}


async def getter_add_part_or_work(i18n: TranslatorHub,
                                  dialog_manager: DialogManager,
                                  **kwargs) -> Dict[str, str]:
    if dialog_manager.start_data:
        dialog_manager.dialog_data.update(**dialog_manager.start_data)

    add_param = dialog_manager.dialog_data.get("add_param")
    text = i18n.service.edit.error.param.text()

    if add_param == "service_add_part_button":
        text = i18n.service.add.part.text()
    if add_param == "service_add_work_button":
        text = i18n.service.add.work.text()

    return {"add_param_text": text,
            "back_button": i18n.back.button()}
