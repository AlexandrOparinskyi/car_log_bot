from aiogram.types import Message
from aiogram_dialog import DialogManager


async def check_enter_refuel_total_price(message: Message,
                                         dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get('i18n')
    if "-" in message.text or "+" in message.text:
        await message.answer(
            text=i18n.error.enter.refuel.total.price.text()
        )
        return False

    try:
        text = message.text.replace(",", ".")
        float(text)
        return True
    except ValueError:
        i18n = dialog_manager.middleware_data.get('i18n')
        await message.answer(
            text=i18n.error.enter.refuel.total.price.text()
        )
        return False