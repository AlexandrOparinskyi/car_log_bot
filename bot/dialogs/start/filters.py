from datetime import datetime

from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def check_user_enter_edit_car(message: Message,
                                    dialog_manager: DialogManager):
    part = dialog_manager.dialog_data.get("part")
    i18n = dialog_manager.middleware_data.get("i18n")

    if part == "year":
        year = message.text
        current_year = datetime.now().year

        try:
            if 1900 > int(year) or int(year) > current_year:
                dialog_manager.show_mode = ShowMode.NO_UPDATE
                await message.answer(
                    text=i18n.error.enter.car.year(
                        user_input=message.text,
                        current_year=str(current_year)
                    )
                )
                return
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.error.enter.car.year(
                    user_input=message.text,
                    current_year=str(current_year)
                )
            )
            return

    if part == "mileage":
        mileage = message.text

        if not mileage.isdigit():
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.error.enter.car.mileage(user_input=message.text)
            )
            return

    return True
