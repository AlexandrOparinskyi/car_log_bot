from typing import Dict

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from utils import get_refuel_data, get_user_by_id


async def getter_total_price(i18n: TranslatorHub,
                             **kwargs) -> Dict[str, str]:
    return {"total_price_text": i18n.refuel.total.price.text()}


async def getter_refuel_edit_menu(i18n: TranslatorHub,
                                  dialog_manager: DialogManager,
                                  event_from_user: User,
                                  **kwargs) -> Dict[str, str]:
    user = await get_user_by_id(event_from_user.id)
    car = user.get_selected_main_car

    if car:
        dialog_manager.dialog_data.update(car=car)

    record_data = get_refuel_data(i18n,
                                  dialog_manager.dialog_data,
                                  user)
    refuel_edit_menu_text = i18n.refuel.edit.menu.text(
        record_data=record_data
    )

    return {"refuel_edit_menu_text": refuel_edit_menu_text}
