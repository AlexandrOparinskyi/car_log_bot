from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Select, Group
from aiogram_dialog.widgets.text import Format

from bot.states import InstructionState
from .getters import getter_instructions, getter_select_instruction
from .handlers import select_instruction_button
from ..general import home_button, back_button

instruction_dialog = Dialog(
    Window(
        Format("{instruction_text}"),
        Group(Select(Format("{item[1]}"),
                     id="instruction",
                     item_id_getter=lambda x: x[0],
                     items="instruction_buttons",
                     on_click=select_instruction_button),
              width=2),
        Button(Format("{home_button}"),
               id="home_button",
               on_click=home_button),
        getter=getter_instructions,
        state=InstructionState.instructions
    ),
    Window(
        Format("{instruction_text}"),
        Button(Format("{back_button}"),
               id="back_button_to_instructions",
               on_click=back_button),
        getter=getter_select_instruction,
        state=InstructionState.select_instruction
    )
)
