from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select, Checkbox
from aiogram_dialog.widgets.text import Format

from .filters import check_enter_refuel_param
from .getters import (getter_total_price,
                      getter_refuel_edit_menu,
                      getter_refuel_edit_param)
from states import RefuelState
from .handlers import (enter_total_price_refuel,
                       save_refuel,
                       full_tank_checkbox,
                       refuel_edit_params,
                       enter_refuel_param,
                       select_refuel_param_button)
from ..general import (error_enter_no_text,
                       home_button,
                       back_button)

refuel_dialog = Dialog(
    Window(
        Format("{total_price_text}"),
        MessageInput(func=enter_total_price_refuel,
                     content_types=ContentType.TEXT,
                     filter=check_enter_refuel_param),
        MessageInput(func=error_enter_no_text),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_total_price,
        state=RefuelState.total_price
    ),
    Window(
        Format("{refuel_edit_menu_text}"),
        Group(Select(Format("{item[0]}"),
                     id="refuel_params",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=refuel_edit_params),
              Checkbox(Format("{full_tank_button}"),
                       Format("{not_full_tank_button}"),
                       id="full_tank_checkbox",
                       default=False,
                       on_state_changed=full_tank_checkbox),
              width=2),
        Button(Format("{save_button}"),
               id="save_button",
               on_click=save_refuel),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_refuel_edit_menu,
        state=RefuelState.edit_menu
    ),
    Window(
        Format("{refuel_edit_text}"),
        MessageInput(func=enter_refuel_param,
                     content_types=ContentType.TEXT,
                     filter=check_enter_refuel_param),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="back_to_edit_params_refuel",
               on_click=back_button),
        getter=getter_refuel_edit_param,
        state=RefuelState.edit_to_text
    ),
    Window(
        Format("{refuel_edit_text}"),
        Group(Select(Format("{item[0]}"),
                     id="refuel_param_button",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=select_refuel_param_button),
              width=2),
        Button(Format("{back_button}"),
               id="back_to_edit_params_refuel",
               on_click=back_button),
        getter=getter_refuel_edit_param,
        state=RefuelState.edit_to_button
    )
)
