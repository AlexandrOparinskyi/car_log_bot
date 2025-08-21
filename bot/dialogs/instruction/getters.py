from typing import Dict

from aiogram_dialog import DialogManager
from fluentogram import TranslatorHub

from utils import get_all_instructions, get_instruction_by_id


async def getter_instructions(i18n: TranslatorHub,
                              **kwargs) -> Dict[str, str]:
    instructions = await get_all_instructions()
    instruction_buttons = ((i.id, i.title) for i in instructions)

    return {"instruction_text": i18n.instruction.text(),
            "home_button": i18n.home.button(),
            "instruction_buttons": instruction_buttons}


async def getter_select_instruction(i18n: TranslatorHub,
                                    dialog_manager: DialogManager,
                                    **kwargs) -> Dict[str, str]:
    instruction_id = int(dialog_manager.dialog_data.get("instruction_id"))
    instruction = await get_instruction_by_id(instruction_id)

    return {"instruction_text": str(instruction.text),
            "back_button": i18n.back.button()}
