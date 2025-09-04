from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from bot.states import StartState, HomeState
from bot.utils import (exists_user,
                       create_user,
                       add_bonus_points)

user_router = Router()


@user_router.message(Command(commands=["start", "home"]))
async def command_start(message: Message,
                        command: CommandObject,
                        dialog_manager: DialogManager):
    ref_code = command.args

    if not await exists_user(message.from_user.id):
        if ref_code:
            user_id = await create_user(message.from_user.id,
                                        message.from_user.username,
                                        message.from_user.first_name,
                                        message.from_user.last_name,
                                        bonus_points=100)
        else:
            user_id = await create_user(message.from_user.id,
                                        message.from_user.username,
                                        message.from_user.first_name,
                                        message.from_user.last_name)


        if ref_code and user_id != int(ref_code):
            await add_bonus_points(int(ref_code))

        await dialog_manager.start(state=StartState.start,
                                   mode=StartMode.RESET_STACK)
        return

    await dialog_manager.start(state=HomeState.home,
                               mode=StartMode.RESET_STACK)
