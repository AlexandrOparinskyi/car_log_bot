from typing import Dict

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from utils import (get_user_by_id, get_car_by_id,
                   get_button_for_add_components,
                   generate_text_for_car_edit_menu,
                   get_text_for_select_part)


async def getter_garage(i18n: TranslatorHub,
                        event_from_user: User,
                        **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    car_buttons = [(c.id, c.name) for c in user.cars]

    return {"garage_text": i18n.garage.text(username=user.first_name,
                                            cars_count=len(user.cars)),
            "home_button": i18n.home.button(),
            "car_buttons": car_buttons,
            "add_car_button": i18n.add.car.button()}


async def getter_car_info(i18n: TranslatorHub,
                          dialog_manager: DialogManager,
                          **kwargs) -> Dict[str, str]:
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)
    edit_car_buttons = get_button_for_add_components(i18n)

    return {"car_info_text": i18n.car.info.text(car_name=car.name,
                                                car_data=""),
            "back_button": i18n.back.button(),
            "edit_car_buttons": edit_car_buttons,}


async def getter_car_name(i18n: TranslatorHub,
                          **kwargs) -> Dict[str, str]:
    return {"add_car_text": i18n.add.car.text()}


async def getter_edit_car_menu(i18n: TranslatorHub,
                               dialog_manager: DialogManager,
                               **kwargs) -> Dict[str, str]:
    car_name = dialog_manager.dialog_data.get("car_name")
    buttons = get_button_for_add_components(i18n)
    car_data = generate_text_for_car_edit_menu(dialog_manager.dialog_data)

    return {"edit_car_menu_text": i18n.edit.car.menu.text(car_name=car_name,
                                                          car_data=car_data),
            "buttons": buttons,
            "save_car_button": i18n.end.edit.car.button(),
            "home_button": i18n.home.button()}


async def getter_edit_car_part(i18n: TranslatorHub,
                                    dialog_manager: DialogManager,
                                    **kwargs) -> Dict[str, str]:
    text_for_part = get_text_for_select_part(i18n)
    text, buttons = text_for_part[dialog_manager.dialog_data.get("part")]

    return {"text": text,
            "buttons": buttons,
            "back_button": i18n.back.button()}
