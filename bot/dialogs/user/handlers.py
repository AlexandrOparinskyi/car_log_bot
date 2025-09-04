from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states import UserState


async def user_home_button(callback: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager):
    await dialog_manager.start(state=UserState.user_home)


async def invite_friends(callback: CallbackQuery,
                         button: Button,
                         dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=UserState.invite_friends)


async def copy_invite_link(callback: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager):
    await dialog_manager.switch_to(state=UserState.copy_link)
