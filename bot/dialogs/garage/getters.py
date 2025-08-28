from typing import Dict

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from utils import (get_user_by_id, get_car_by_id,
                   get_button_for_add_components,
                   generate_text_for_car_edit_menu,
                   get_text_for_select_part,
                   generate_car_info)


async def getter_garage(i18n: TranslatorHub,
                        event_from_user: User,
                        **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    cars = sorted(user.active_cars, key=lambda x: x.created_at)
    car_buttons = [(c.id, c.name) for c in cars]

    if not user.is_premium:
        car_buttons = car_buttons[:2]

    return {"garage_text": i18n.garage.text(username=user.first_name,
                                            cars_count=len(car_buttons)),
            "home_button": i18n.home.button(),
            "car_buttons": car_buttons,
            "add_car_button": i18n.add.car.button()}


async def getter_car_info(i18n: TranslatorHub,
                          dialog_manager: DialogManager,
                          **kwargs) -> Dict[str, str]:
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)
    dialog_manager.dialog_data.update(car_name=car.name)
    edit_car_buttons = get_button_for_add_components(i18n)
    car_data = generate_car_info(car, dialog_manager.dialog_data)

    return {"car_info_text": i18n.car.info.text(car_name=car.name,
                                                car_data=car_data),
            "back_button": i18n.back.button(),
            "edit_car_buttons": edit_car_buttons,
            "save_car_button": i18n.end.edit.car.button(),
            "delete_car_button": i18n.delete.car.button()}


async def getter_car_name(i18n: TranslatorHub,
                          **kwargs) -> Dict[str, str]:
    return {"add_car_text": i18n.add.car.text(),
            "back_button": i18n.back.button()}


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


async def getter_delete_car(i18n: TranslatorHub,
                            dialog_manager: DialogManager,
                            event_from_user: User,
                            **kwargs) -> Dict[str, str]:
    car_id = int(dialog_manager.dialog_data.get("car_id"))
    car = await get_car_by_id(car_id)
    username = event_from_user.first_name

    return {"delete_car_text": i18n.delete.car.text(username=username,
                                                    car_name=car.name),
            "yes_button": i18n.yes.button(descr=", удалить"),
            "no_button": i18n.no.button(descr=", оставить")}


async def getter_limit_car(i18n: TranslatorHub,
                           event_from_user: User,
                           **kwargs) -> Dict[str, str]:
    username = event_from_user.first_name

    return {"garage_limit_text": i18n.garage.limit.text(username=username),
            "back_button": i18n.back.button(),
            "connect_premium_button": i18n.connect.premium.button()}
