from typing import Dict

from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from bot.utils import (get_purchase_data_text,
                       get_user_by_id,
                       get_button_for_edit_purchase,
                       get_purchase_edit_text)
from database import User


async def getter_purchase_total_price(i18n: TranslatorHub,
                                      **kwargs) -> Dict[str, str]:
    return {"total_price_text": i18n.purchase.total.price.text(),
            "home_button": i18n.home.button(),
            "back_button": i18n.back.button()}


async def getter_purchase_edit_menu(i18n: TranslatorHub,
                                    dialog_manager: DialogManager,
                                    event_from_user: User,
                                    **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    car = user.get_selected_main_car

    if not dialog_manager.dialog_data.get("car") and car:
        dialog_manager.dialog_data.update(car=car)

    purchase_data = get_purchase_data_text(i18n,
                                           dialog_manager.dialog_data)
    edit_menu_text = i18n.purchase.edit.menu.text(purchase_data=purchase_data)

    buttons = get_button_for_edit_purchase(i18n)

    return {"edit_menu_text": edit_menu_text,
            "buttons": buttons,
            "home_button": i18n.home.button(),
            "end_edit_button": i18n.end.edit.car.button()}


async def getter_purchase_edit_param(i18n: TranslatorHub,
                                     dialog_manager: DialogManager,
                                     event_from_user: User,
                                     **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    text, buttons = get_purchase_edit_text(i18n,
                                           dialog_manager.dialog_data,
                                           user.active_cars)

    return {"edit_param_text": text,
            "buttons": buttons,
            "back_button": i18n.back.button()}
