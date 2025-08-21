from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from states import InstructionState


async def instruction_button(callback: CallbackQuery,
                             button: Button,
                             dialog_manager: DialogManager):
    await dialog_manager.start(state=InstructionState.instructions)


async def select_instruction_button(callback: CallbackQuery,
                                    widget: Select,
                                    dialog_manager: DialogManager,
                                    item_id: str):
    dialog_manager.dialog_data.update(instruction_id=item_id)

    await dialog_manager.next()
