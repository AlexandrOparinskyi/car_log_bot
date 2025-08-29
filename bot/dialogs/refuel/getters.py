from typing import Dict

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from utils import get_refuel_data, get_user_by_id, get_refuel_button


async def getter_total_price(i18n: TranslatorHub,
                             **kwargs) -> Dict[str, str]:
    return {"total_price_text": i18n.refuel.total.price.text(),
            "home_button": i18n.home.button()}


async def getter_refuel_edit_menu(i18n: TranslatorHub,
                                  dialog_manager: DialogManager,
                                  event_from_user: User,
                                  **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    dialog_manager.dialog_data.update(user_id=user.id)
    car = user.get_selected_main_car

    if car:
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


async def getter_refuel_edit_text(i18n: TranslatorHub,
                                  dialog_manager: DialogManager,
                                  **widget_kwargs) -> Dict[str, str]:
    refuel_param = dialog_manager.dialog_data.get("refuel_param")
    text = i18n.refuel.edit.error.param.text()
    print(dialog_manager.dialog_data)

    if refuel_param == "total_price":
        text = i18n.refuel.edit.total.price.text()
    if refuel_param == "liters":
        text = i18n.refuel.edit.liters.text()
    if refuel_param == "comment":
        text = i18n.refuel.edit.comment.text()

    return {"refuel_edit_text": text,
            "back_button": i18n.back.button()}
