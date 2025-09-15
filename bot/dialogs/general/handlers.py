from aiogram.enums import ContentType
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager, StartMode, ShowMode
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.states import (HomeState,
                        StartState,
                        InstructionState,
                        GarageState,
                        AddCarState,
                        RefuelState,
                        UserState,
                        ServiceState,
                        ServiceWorkState,
                        ServicePartState)


async def home_button(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    await dialog_manager.start(state=HomeState.home,
                               mode=StartMode.RESET_STACK)


async def back_button(callback: CallbackQuery,
                      button: Button,
                      dialog_manager: DialogManager):
    if callback.data == "start_back_button_to_car_edit_menu":
        await dialog_manager.switch_to(state=StartState.edit_car_menu)

    if callback.data == "back_button_to_instructions":
        await dialog_manager.switch_to(state=InstructionState.instructions)

    if callback.data == "back_button_to_garage":
        await dialog_manager.start(state=GarageState.garage)

    if callback.data == "back_button_to_edit_menu":
        await dialog_manager.switch_to(state=AddCarState.edit_car_menu)

    if callback.data == "garage_back_button_to_edit_menu":
        await dialog_manager.switch_to(state=GarageState.car_info)

    if callback.data == "back_button_to_edit_params_refuel":
        await dialog_manager.switch_to(state=RefuelState.edit_menu)

    if callback.data == "back_button_to_edit_params_service":
        await dialog_manager.switch_to(state=ServiceState.edit_menu)

    if callback.data == "back_button_to_user_home":
        await dialog_manager.switch_to(state=UserState.user_home)

    if callback.data == "back_button_to_select_record":
        await dialog_manager.start(state=HomeState.select_record)

    if (callback.data == "back_button_to_edit_params_service_at_work" or
        callback.data == "back_button_to_edit_params_service_at_part"):
        await dialog_manager.start(state=ServiceState.edit_menu,
                                   data={**dialog_manager.dialog_data})

    if callback.data == "back_button_to_edit_service_work_param":
        await dialog_manager.switch_to(state=ServiceWorkState.edit_menu)


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


async def error_enter_no_text(message: Message,
                              widget: MessageInput,
                              dialog_manager: DialogManager):
    dialog_manager.show_mode = ShowMode.NO_UPDATE
    i18n = dialog_manager.middleware_data.get("i18n")

    if message.content_type == ContentType.TEXT:
        return

    await message.answer(
        text=i18n.error.enter.no.text()
    )


async def service_in_developing(callback: CallbackQuery,
                                button: Button,
                                dialog_manager: DialogManager):
    dialog_manager.show_mode = ShowMode.NO_UPDATE
    i18n = dialog_manager.middleware_data.get("i18n")

    await callback.answer(i18n.service.developing.text(),
                          show_alert=True)
