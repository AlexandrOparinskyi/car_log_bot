from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from states import StartState
from utils import exists_user, create_user

user_router = Router()


@user_router.message(Command(commands=["start", "home"]))
async def command_start(message: Message,
                        dialog_manager: DialogManager):
    if not await exists_user(message.from_user.id):
        await create_user(message.from_user.id,
                          message.from_user.username,
                          message.from_user.first_name,
                          message.from_user.last_name)
        await dialog_manager.start(state=StartState.start,
                                   mode=StartMode.RESET_STACK)
        return

    await dialog_manager.start(state=StartState.start,
                               mode=StartMode.RESET_STACK)
