from typing import Dict

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import (get_refuel_data,
                       get_user_by_id,
                       get_refuel_button,
                       get_refuel_edit_text_and_buttons)


async def getter_total_price(i18n: TranslatorHub,
                             **kwargs) -> Dict[str, str]:
    return {"total_price_text": i18n.refuel.total.price.text(),
            "back_button": i18n.back.button(),
            "home_button": i18n.home.button()}


async def getter_refuel_edit_menu(i18n: TranslatorHub,
                                  dialog_manager: DialogManager,
                                  event_from_user: User,
                                  **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    dialog_manager.dialog_data.update(user_id=user.id)
    car = user.get_selected_main_car

    if not dialog_manager.dialog_data.get("car") and car:
        dialog_manager.dialog_data.update(car=car)

    record_data = get_refuel_data(i18n,
                                  dialog_manager.dialog_data,
                                  user)
    refuel_edit_menu_text = i18n.refuel.edit.menu.text(
        record_data=record_data
    )
    buttons = get_refuel_button(i18n)

    return {"refuel_edit_menu_text": refuel_edit_menu_text,
            "buttons": buttons,
            "full_tank_button": i18n.edit.refuel.full.tank.button(),
            "not_full_tank_button": i18n.edit.refuel.no.full.tank.button(),
            "save_button": i18n.end.edit.car.button(),
            "home_button": i18n.home.button()}


async def getter_refuel_edit_param(i18n: TranslatorHub,
                                   dialog_manager: DialogManager,
                                   event_from_user: User,
                                   **widget_kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    refuel_param = dialog_manager.dialog_data.get("refuel_param")
    text, buttons = get_refuel_edit_text_and_buttons(i18n,
                                                     refuel_param,
                                                     user.cars)

    return {"refuel_edit_text": text,
            "buttons": buttons,
            "back_button": i18n.back.button()}
