from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Select, Button, Calendar
from aiogram_dialog.widgets.text import Format

from bot.states import ServiceState
from .filters import check_enter_service_param
from .getters import (getter_select_type,
                      getter_service_edit_menu,
                      getter_service_edit_param,
                      service_calendar)
from .handlers import (select_service_type,
                       service_edit_param,
                       enter_service_param,
                       select_service_param_button,
                       service_edit_calendar)
from ..general import (back_button,
                       home_button,
                       error_enter_no_text)

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
        Group(Select(Format("{item[0]}"),
                     id="service_edit_menu",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=service_edit_param),
              width=2),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_service_edit_menu,
        state=ServiceState.edit_menu
    ),
    Window(
        Format("{service_edit_text}"),
        MessageInput(func=enter_service_param,
                     content_types=ContentType.TEXT,
                     filter=check_enter_service_param),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="back_button_to_edit_params_service",
               on_click=back_button),
        getter=getter_service_edit_param,
        state=ServiceState.param_edit_text
    ),
    Window(
Format("{service_edit_text}"),
        Group(Select(Format("{item[0]}"),
                     id="service_edit_params",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=select_service_param_button),
              width=2),
        Button(Format("{back_button}"),
               id="back_button_to_edit_params_service",
               on_click=back_button),
        getter=getter_service_edit_param,
        state=ServiceState.param_edit_button
    ),
    Window(
        Format("{service_calendar_text}"),
        Calendar(
            id="calendar",
            on_click=service_edit_calendar
        ),
        getter=service_calendar,
        state=ServiceState.calendar
    )
)
