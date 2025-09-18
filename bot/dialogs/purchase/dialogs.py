from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select, Calendar
from aiogram_dialog.widgets.text import Format

from bot.states import PurchaseState
from .filters import check_enter_purchase_param
from .getters import (getter_purchase_total_price,
                      getter_purchase_edit_menu,
                      getter_purchase_edit_param)
from .handlers import (enter_purchase_total_price,
                       edit_purchase_params,
                       purchase_edit_calendar,
                       purchase_edit_car,
                       enter_purchase_param,
                       save_purchase_button)
from ..general import (error_enter_no_text,
                       back_button,
                       home_button)

purchase_dialog = Dialog(
    Window(
        Format("{total_price_text}"),
        MessageInput(func=enter_purchase_total_price,
                     content_types=ContentType.TEXT,
                     filter=check_enter_purchase_param),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="back_button_to_select_record",
               on_click=back_button),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_purchase_total_price,
        state=PurchaseState.total_price
    ),
    Window(
        Format("{edit_menu_text}"),
        Group(Select(Format("{item[0]}"),
                     id="refuel_params",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=edit_purchase_params),
              width=2),
        Button(Format("{end_edit_button}"),
               id="end_edit_button",
               on_click=save_purchase_button),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_purchase_edit_menu,
        state=PurchaseState.edit_menu
    ),
    Window(
        Format("{edit_param_text}"),
        MessageInput(func=enter_purchase_param,
                     content_types=ContentType.TEXT,
                     filter=check_enter_purchase_param),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="back_button_to_purchase_edit_menu",
               on_click=back_button),
        getter=getter_purchase_edit_param,
        state=PurchaseState.edit_to_text
    ),
    Window(
        Format("{edit_param_text}"),
        Group(Select(Format("{item[0]}"),
                     id="purchase_params",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=purchase_edit_car),
              width=2),
        Button(Format("{back_button}"),
               id="back_button_to_purchase_edit_menu",
               on_click=back_button),
        getter=getter_purchase_edit_param,
        state=PurchaseState.edit_to_button
    ),
    Window(
        Format("{edit_param_text}"),
        Calendar(
            id="calendar",
            on_click=purchase_edit_calendar
        ),
        Button(Format("{back_button}"),
               id="back_button_to_purchase_edit_menu",
               on_click=back_button),
        getter=getter_purchase_edit_param,
        state=PurchaseState.calendar
    )
)
