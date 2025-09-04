from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Format

from .getters import (getter_user_home,
                      getter_invite_friend,
                      getter_copy_link)
from bot.states import UserState
from .handlers import invite_friends, copy_invite_link
from ..general import (home_button,
                       service_in_developing,
                       back_button)

user_dialog = Dialog(
    Window(
        Format("{user_home_text}"),
        Button(Format("{invite_friend_button}"),
               id="invite_friend_button",
               on_click=invite_friends),
        Row(Button(Format("{user_settings_button}"),
                   id="user_settings_button",
                   on_click=service_in_developing),
            Button(Format("{achievements_button}"),
                   id="achievements_button",
                   on_click=service_in_developing),
            ),
        Button(Format("{connect_premium_button}"),
               id="connect_premium_button",
               on_click=service_in_developing),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_user_home,
        state=UserState.user_home
    ),
    Window(
        Format("{invite_friend_text}"),
        Button(Format("{copy_link_button}"),
               id="copy_link_button",
               on_click=copy_invite_link),
        Button(Format("{back_button}"),
               id="back_button_to_user_home",
               on_click=back_button),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_invite_friend,
        state=UserState.invite_friends
    ),
    Window(
        Format("{copy_link_text}"),
        Button(Format("{copy_text_link_button}"),
               id="copy_text_link_button",
               on_click=invite_friends),
        Button(Format("{back_button}"),
               id="back_button_to_user_home",
               on_click=back_button),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_copy_link,
        state=UserState.copy_link
    )
)
