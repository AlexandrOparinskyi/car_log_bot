from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Group, Select, Button, Calendar
from aiogram_dialog.widgets.text import Format

from bot.states import ServiceState, ServiceWorkState, ServicePartState
from .filters import check_enter_service_param
from .getters import (getter_select_type,
                      getter_service_edit_menu,
                      getter_service_edit_param,
                      getter_service_calendar,
                      getter_add_part_or_work,
                      getter_service_work_edit_menu,
                      getter_service_work_edit_params, getter_service_part_edit_menu)
from .handlers import (select_service_type,
                       service_edit_param,
                       enter_service_param,
                       select_service_param_button,
                       service_edit_calendar,
                       service_add_part_or_work,
                       enter_service_work_name,
                       paginator_handler,
                       select_service_work_edit_param,
                       enter_service_work_edit_param,
                       delete_service_work_button,
                       add_work_button, enter_service_part_name)
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
        Button(Format("{service_add_part_button}"),
               id="service_add_part_button",
               on_click=service_add_part_or_work),
        Button(Format("{service_add_work_button}"),
               id="service_add_work_button",
               on_click=service_add_part_or_work),
        Group(Select(Format("{item[0]}"),
                     id="service_edit_menu",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=service_edit_param),
              width=2),
        Button(Format("{save_button}"),
               id="save_button",
               on_click=None),
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
        Button(Format("{back_button}"),
               id="back_button_to_edit_params_service",
               on_click=back_button),
        getter=getter_service_calendar,
        state=ServiceState.calendar
    )
)

service_work_dialog = Dialog(
    Window(
        Format("{add_param_text}"),
        MessageInput(func=enter_service_work_name,
                     content_types=ContentType.TEXT,
                     id="service_work"),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="back_button_to_edit_params_service_at_work",
               on_click=back_button),
        getter=getter_add_part_or_work,
        state=ServiceWorkState.work_name
    ),
    Window(
        Format("{service_work_edit_menu_text}"),
        Group(Select(Format("{item[0]}"),
                     id="service_work_edit_button",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=select_service_work_edit_param),
              Button(Format("{delete_service_work_button}"),
                     id="delete_service_work_button",
                     on_click=delete_service_work_button),
              width=2),
        Group(Select(Format("{item[0]}"),
                     id="paginator_buttons",
                     item_id_getter=lambda x: x[1],
                     items="paginator_buttons",
                     on_click=paginator_handler),
              width=3),
        Button(Format("{add_work_button}"),
               id="add_work_button",
               on_click=add_work_button),
        Button(Format("{back_button}"),
               id="back_button_to_edit_params_service_at_work",
               on_click=back_button),
        getter=getter_service_work_edit_menu,
        state=ServiceWorkState.edit_menu
    ),
    Window(
        Format("{service_work_edit_text}"),
        MessageInput(func=enter_service_work_edit_param,
                     content_types=ContentType.TEXT),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="back_button_to_edit_service_work_param",
               on_click=back_button),
        getter=getter_service_work_edit_params,
        state=ServiceWorkState.param_edit_text
    )
)

service_part_dialog = Dialog(
    Window(
        Format("{add_param_text}"),
        MessageInput(func=enter_service_part_name,
                     content_types=ContentType.TEXT,
                     id="service_part"),
        MessageInput(func=error_enter_no_text),
        Button(Format("{back_button}"),
               id="back_button_to_edit_params_service_at_work",
               on_click=back_button),
        getter=getter_add_part_or_work,
        state=ServicePartState.part_name
    ),
    Window(
        Format("{service_part_edit_menu_text}"),
        Group(Select(Format("{item[0]}"),
                     id="service_part_edit_button",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=None),
              width=2),
        Group(Select(Format("{item[0]}"),
                     id="paginator_buttons",
                     item_id_getter=lambda x: x[1],
                     items="paginator_buttons",
                     on_click=paginator_handler),
              width=3),
        Button(Format("{back_button}"),
               id="back_button_to_edit_params_service_at_part",
               on_click=back_button),
        getter=getter_service_part_edit_menu,
        state=ServicePartState.edit_menu
    )
)
