from datetime import datetime

from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import MessageInput

from states import RefuelState


async def enter_total_price_refuel(message: Message,
                                   widget: MessageInput,
                                   dialog_manager: DialogManager):
    dialog_manager.dialog_data.update(total_price=message.text)

    await dialog_manager.switch_to(state=RefuelState.edit_menu)
