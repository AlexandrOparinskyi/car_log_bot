from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def check_enter_purchase_param(message: Message,
                                     dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get("i18n")
    purchase_param = dialog_manager.dialog_data.get("purchase_param")

    if purchase_param in ("title", "comment"):
        return True

    if purchase_param == "quantity":
        try:
            int(message.text)
        except ValueError:
            dialog_manager.show_mode = ShowMode.NO_UPDATE
            await message.answer(
                text=i18n.purchase.error.enter.quantity.text()
            )
            return False

    try:
        text = message.text.replace(",", ".")
        float(text)
        return True
    except ValueError:
        dialog_manager.show_mode = ShowMode.NO_UPDATE
        await message.answer(
            text=i18n.error.enter.purchase.total.price.text()
        )
        return False
