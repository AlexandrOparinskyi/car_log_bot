from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select
from aiogram_dialog.widgets.text import Format

from .getters import (getter_garage,
                                    getter_car_info,
                                    getter_car_name,
                                    getter_edit_car_menu,
                                    getter_edit_car_part,
                                    getter_delete_car,
                                    getter_limit_car)
from bot.states import GarageState, AddCarState
from .handlers import (car_info,
                       add_car_button,
                       enter_car_name,
                       select_part_car_to_edit,
                       save_car_part_enter,
                       save_car_part_button,
                       save_updated_car,
                       delete_car_button,
                       delete_car)
from ..general import (home_button,
                       back_button,
                       error_no_message_car_name,
                       check_user_enter_edit_car,
                       error_enter_no_text,
                       service_in_developing)

garage_dialog = Dialog(
    Window(
        Format("{garage_text}"),
        Group(Select(Format("{item[1]}"),
                     id="car",
                     item_id_getter=lambda x: x[0],
                     items="car_buttons",
                     on_click=car_info),
              width=2),
        Button(Format("{add_car_button}"),
               id="add_car_button",
               on_click=add_car_button),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_garage,
        state=GarageState.garage
    ),
    Window(
        Format("{car_info_text}"),
        Group(Select(Format("{item[0]}"),
                     id="garage_edit_car_part",
                     item_id_getter=lambda x: x[1],
                     items="edit_car_buttons",
                     on_click=select_part_car_to_edit),
              width=2),
        Button(Format("{save_car_button}"),
               id="garage_save_car_button",
               on_click=save_updated_car),
        Button(Format("{delete_car_button}"),
               id="delete_car_button",
               on_click=delete_car_button),
        Button(Format("{back_button}"),
               id="back_button_to_garage",
               on_click=back_button),
        getter=getter_car_info,
        state=GarageState.car_info
    ),
    Window(
        Format("{text}"),
        MessageInput(func=save_car_part_enter,
                     content_types=ContentType.TEXT,
                     filter=check_user_enter_edit_car,
                     id="garage_edit_car_part"),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="garage_back_button_to_edit_menu",
               on_click=back_button),
        getter=getter_edit_car_part,
        state=GarageState.edit_to_text
    ),
    Window(
        Format("{text}"),
        Group(Select(Format("{item[0]}"),
                     id="garage_edit_car_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=save_car_part_button),
              width=2),
        Button(Format("{back_button}"),
               id="garage_back_button_to_edit_menu",
               on_click=back_button),
        getter=getter_edit_car_part,
        state=GarageState.edit_to_button
    ),
    Window(
        Format("{delete_car_text}"),
        Button(Format("{yes_button}"),
               id="yes_button",
               on_click=delete_car),
        Button(Format("{no_button}"),
               id="garage_back_button_to_edit_menu",
               on_click=back_button),
        getter=getter_delete_car,
        state=GarageState.delete_car
    ),
    Window(
        Format("{garage_limit_text}"),
        Button(Format("{connect_premium_button}"),
               id="connect_premium_button",
               on_click=service_in_developing),
        Button(Format("{back_button}"),
               id="back_button_to_garage",
               on_click=back_button),
        getter=getter_limit_car,
        state=GarageState.large_count_car
    )
)

add_car_dialog = Dialog(
    Window(
        Format("{add_car_text}"),
        MessageInput(func=enter_car_name,
                     content_types=ContentType.TEXT),
        MessageInput(func=error_no_message_car_name),
        Button(Format("{back_button}"),
               id="back_button_to_garage",
               on_click=back_button),
        getter=getter_car_name,
        state=AddCarState.car_name
    ),
    Window(
        Format("{edit_car_menu_text}"),
        Group(Select(Format("{item[0]}"),
                     id="car_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=select_part_car_to_edit),
              width=2),
        Button(Format("{save_car_button}"),
               id="save_car_button",
               on_click=save_updated_car),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_edit_car_menu,
        state=AddCarState.edit_car_menu
    ),
    Window(
        Format("{text}"),
        MessageInput(func=save_car_part_enter,
                     content_types=ContentType.TEXT,
                     filter=check_user_enter_edit_car),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="back_button_to_edit_menu",
               on_click=back_button),
        getter=getter_edit_car_part,
        state=AddCarState.edit_to_text
    ),
    Window(
        Format("{text}"),
        Group(Select(Format("{item[0]}"),
                     id="edit_car_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=save_car_part_button),
              width=2),
        Button(Format("{back_button}"),
               id="back_button_to_edit_menu",
               on_click=back_button),
        getter=getter_edit_car_part,
        state=AddCarState.edit_to_button
    )
)
