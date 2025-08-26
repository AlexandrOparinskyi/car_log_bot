from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Group, Button, Row, Url
from aiogram_dialog.widgets.text import Format

from states import HomeState
from .getters import getter_home, getter_write_developer
from .handlers import developer_button
from ..garage import garage_button
from ..general import service_in_developing, home_button
from ..instruction import instruction_button

home_dialog = Dialog(
    Window(
        Format("{home_text}"),
        Group(Button(Format("{add_button}"),
                     id="add_button",
                     on_click=service_in_developing),
              Row(Button(Format("{garage_button}"),
                            id="garage_button",
                            on_click=garage_button),
                     Button(Format("{lk_button}"),
                            id="lk_button",
                            on_click=service_in_developing)),
              Row(Button(Format("{instructions_button}"),
                            id="instructions_button",
                            on_click=instruction_button),
                     Button(Format("{reviews_button}"),
                            id="reviews_button",
                            on_click=service_in_developing)),
              Button(Format("{support_project_button}"),
                     id="support_project_button",
                     on_click=service_in_developing),
              Button(Format("{write_developer_button}"),
                     id="write_developer_button",
                     on_click=developer_button)),
        getter=getter_home,
        state=HomeState.home
    ),
    Window(
        Format("{write_developer_text}"),
        Url(Format("{developer_button}"),
            Format("{developer_url}")),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_write_developer,
        state=HomeState.write_developer
    )
)