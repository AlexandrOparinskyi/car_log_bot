from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select
from aiogram_dialog.widgets.text import Format

from dialogs.garage.getters import (getter_garage,
                                    getter_car_info,
                                    getter_car_name, getter_edit_car_menu)
from .handlers import (car_info,
                       add_car_button,
                       enter_car_name)
from ..general import (home_button,
                       back_button,
                       error_no_message_car_name)
from states import GarageState, AddCarState

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
                     id="edit_car_part",
                     item_id_getter=lambda x: x[1],
                     items="edit_car_buttons",),
              width=2),
        Button(Format("{back_button}"),
               id="back_button_to_garage",
               on_click=back_button),
        getter=getter_car_info,
        state=GarageState.car_info
    )
)

add_car_dialog = Dialog(
    Window(
        Format("{add_car_text}"),
        MessageInput(func=enter_car_name,
                     content_types=ContentType.TEXT),
        MessageInput(func=error_no_message_car_name),
        getter=getter_car_name,
        state=AddCarState.car_name
    ),
    Window(
        Format("{edit_car_menu_text}"),
        Group(Select(Format("{item[0]}"),
                     id="car_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons"),
              width=2),
        Button(Format("save_car_button"),
               id="save_car_button",
               on_click=None),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_edit_car_menu,
        state=AddCarState.edit_car_menu
    )
)
