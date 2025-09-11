from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Group, Select, Button
from aiogram_dialog.widgets.text import Format

from bot.states import ServiceState
from .getters import getter_select_type, getter_service_edit_menu
from .handlers import select_service_type
from ..general import (back_button,
                       home_button)

service_dialog = Dialog(
    Window(
        Format("{select_service_type_text}"),
        Group(Select(Format("{item[0]}"),
                     id="service_type",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=select_service_type),
              width=2),
        Button(Format("{back_button}"),
               id="back_button_to_select_record",
               on_click=back_button),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_select_type,
        state=ServiceState.select_type
    ),
    Window(
        Format("{service_edit_menu_text}"),
        getter=getter_service_edit_menu,
        state=ServiceState.edit_menu
    )
)
