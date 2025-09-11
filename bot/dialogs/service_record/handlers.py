from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Select

from bot.states import ServiceState


async def select_service_type(callback: CallbackQuery,
                              widget: Select,
                              dialog_manager: DialogManager,
                              item_id: str):
    dialog_manager.dialog_data.update(service_type=item_id)
    await dialog_manager.switch_to(state=ServiceState.edit_menu)
