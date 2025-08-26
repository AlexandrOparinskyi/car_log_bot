from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Select

from states import HomeState, StartState, InstructionState, GarageState


async def home_button(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    await dialog_manager.start(state=HomeState.home,
                               mode=StartMode.RESET_STACK)


async def back_button(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    if callback.data == "start_back_button_to_car_edit_menu":
        await dialog_manager.switch_to(StartState.edit_car_menu)

    if callback.data == "back_button_to_instructions":
        await dialog_manager.switch_to(InstructionState.instructions)

    if callback.data == "back_button_to_garage":
        await dialog_manager.switch_to(GarageState.garage)


async def next_state(callback: CallbackQuery,
                     button: Button,
                     dialog_manager: DialogManager):
    await dialog_manager.next()


async def error_no_message_car_name(message: Message,
                                    widget: MessageInput,
                                    dialog_manager: DialogManager):
    dialog_manager.show_mode = ShowMode.NO_UPDATE
    i18n = dialog_manager.middleware_data.get("i18n")

    await message.answer(
        text=i18n.error.no.message.first.car.name()
    )


async def service_in_developing(callback: CallbackQuery,
                                button: Button,
                                dialog_manager: DialogManager):
    dialog_manager.show_mode = ShowMode.NO_UPDATE
    i18n = dialog_manager.middleware_data.get("i18n")

    await callback.answer(i18n.service.developing.text(),
                           show_alert=True)

