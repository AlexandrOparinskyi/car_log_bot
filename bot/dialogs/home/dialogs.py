from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Group, Button, Row
from aiogram_dialog.widgets.text import Format

from states import HomeState
from .getters import getter_home
from ..general import service_in_developing

home_dialog = Dialog(
    Window(
        Format("{home_text}"),
        Group(Button(Format("{add_button}"),
                     id="add_button",
                     on_click=service_in_developing),
              Row(Button(Format("{garage_button}"),
                            id="garage_button",
                            on_click=service_in_developing),
                     Button(Format("{lk_button}"),
                            id="lk_button",
                            on_click=service_in_developing)),
              Row(Button(Format("{instructions_button}"),
                            id="instructions_button",
                            on_click=service_in_developing),
                     Button(Format("{reviews_button}"),
                            id="reviews_button",
                            on_click=service_in_developing)),
              Button(Format("{support_project_button}"),
                     id="support_project_button",
                     on_click=service_in_developing),
              Button(Format("{write_developer_button}"),
                     id="write_developer_button",
                     on_click=service_in_developing)),
        getter=getter_home,
        state=HomeState.home
    )
)