from typing import Dict

from aiogram.types import User
from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from utils import get_button_for_add_components, get_text_for_select_part, \
    generate_text_for_car_edit_menu


async def getter_start(i18n: TranslatorHub,
                       event_from_user: User,
                       **kwargs) -> Dict[str, str]:
    username = event_from_user.first_name

    return {"start_text": i18n.start.text(username=username),
            "acquaintance_button": i18n.acquaintance.button()}


async def getter_acquaintance(i18n: TranslatorHub,
                              **kwargs) -> Dict[str, str]:
    return {"first_acquaintance_text": i18n.first.acquaintance.text(),
            "add_first_car_button": i18n.add.first.car.button()}


async def getter_first_car_name(i18n: TranslatorHub,
                                **kwargs) -> Dict[str, str]:
    return {"first_car_name_text": i18n.first.car.name.text()}


async def getter_choice_next_step(i18n: TranslatorHub,
                                  dialog_manager: DialogManager,
                                  **kwargs) -> Dict[str, str]:
    start_car_edit_menu = i18n.start.choice.next.step.text(
        car_name=dialog_manager.dialog_data.get("car_name")
    )

    return {"choice_next_step": start_car_edit_menu,
            "car_menu_button": i18n.transition.to.car.menu.button(),
            "home_button": i18n.home.button()}


async def getter_car_edit_menu(i18n: TranslatorHub,
                               dialog_manager: DialogManager,
                               **kwargs) -> Dict[str, str]:
    start_car_edit_menu = i18n.start.car.edit.menu.text(
        car_name=dialog_manager.dialog_data.get("car_name"),
        car_data=generate_text_for_car_edit_menu(
            dialog_manager.dialog_data
        )
    )
    edit_car_buttons = get_button_for_add_components(
        dialog_manager.middleware_data.get("i18n")
    )
    return {"start_car_edit_menu": start_car_edit_menu,
            "edit_car_buttons": edit_car_buttons,
            "end_edit_car_button": i18n.end.edit.car.button()}


async def getter_edit_car_part(i18n: TranslatorHub,
                               dialog_manager: DialogManager,
                               **kwargs) -> Dict[str, str]:
    part = dialog_manager.dialog_data.get("part")
    part_data = get_text_for_select_part(
        dialog_manager.middleware_data.get("i18n")
    )
    edit_car_part_text, buttons = part_data[part]

    return {"edit_car_part_text": edit_car_part_text,
            "buttons": buttons,
            "back_button": i18n.back.button()}
