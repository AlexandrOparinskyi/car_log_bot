from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Group, Select
from aiogram_dialog.widgets.text import Format

from bot.states import StartState
from .getters import (getter_start,
                      getter_acquaintance,
                      getter_first_car_name,
                      getter_choice_next_step,
                      getter_car_edit_menu,
                      getter_edit_car_part,
                      getter_end_acquaintance)
from .handlers import (enter_success_car_name,
                       start_edit_car_button,
                       start_save_car_part_button,
                       start_save_car_part_enter,
                       save_start_car_and_exit)
from ..general import (home_button,
                       back_button,
                       next_state,
                       error_no_message_car_name,
                       check_user_enter_edit_car,
                       error_enter_no_text)

start_dialog = Dialog(
    Window(
        Format("{start_text}"),
        Button(Format("{acquaintance_button}"),
               id="acquaintance_button",
               on_click=next_state),
        getter=getter_start,
        state=StartState.start
    ),
    Window(
        Format("{first_acquaintance_text}"),
        Button(Format("{add_first_car_button}"),
               id="add_first_car_button",
               on_click=next_state),
        getter=getter_acquaintance,
        state=StartState.acquaintance
    ),
    Window(
        Format("{first_car_name_text}"),
        MessageInput(func=enter_success_car_name,
                     content_types=ContentType.TEXT),
        MessageInput(func=error_no_message_car_name),
        getter=getter_first_car_name,
        state=StartState.car_name
    ),
    Window(
        Format("{choice_next_step}"),
        Button(Format("{car_menu_button}"),
               id="car_menu_button",
               on_click=next_state),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_choice_next_step,
        state=StartState.choice
    ),
    Window(
        Format("{start_car_edit_menu}"),
        Group(Select(Format("{item[0]}"),
                     id="start_car_edit",
                     item_id_getter=lambda x: x[1],
                     items="edit_car_buttons",
                     on_click=start_edit_car_button),
              width=2),
        Button(Format("{end_edit_car_button}"),
               id="end_edit_car_button",
               on_click=save_start_car_and_exit),
        getter=getter_car_edit_menu,
        state=StartState.edit_car_menu
    ),
    Window(
        Format("{edit_car_part_text}"),
        Group(Select(Format("{item[0]}"),
                     id="edit_car_part",
                     item_id_getter=lambda x: x[1],
                     items="buttons",
                     on_click=start_save_car_part_button),
              width=2),
        Button(Format("{back_button}"),
               id="start_back_button_to_car_edit_menu",
               on_click=back_button),
        getter=getter_edit_car_part,
        state=StartState.edit_to_button
    ),
    Window(
        Format("{edit_car_part_text}"),
        MessageInput(func=start_save_car_part_enter,
                     content_types=ContentType.TEXT,
                     filter=check_user_enter_edit_car),
        MessageInput(func=error_enter_no_text),
        getter=getter_edit_car_part,
        state=StartState.edit_to_text
    ),
    Window(
        Format("{end_acquaintance_text}"),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_end_acquaintance,
        state=StartState.end_acquaintance
    )
)
