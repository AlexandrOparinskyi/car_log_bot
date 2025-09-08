from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def check_enter_refuel_param(message: Message,
                                   dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get('i18n')
    m_text = i18n.error.enter.refuel.total.price.text()
    refuel_param = dialog_manager.dialog_data.get("refuel_param")

    if refuel_param == "comment":
        return True

    if refuel_param == "liters":
        m_text = i18n.error.refuel.edit.liters.text()

    if "-" in message.text or "+" in message.text:
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=m_text
        )
        return False

    try:
        text = message.text.replace(",", ".")
        float(text)
        return True
    except ValueError:
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=m_text
        )
        return False
