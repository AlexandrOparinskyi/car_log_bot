from aiogram.types import Message
from aiogram_dialog import DialogManager, ShowMode


async def check_enter_service_param(message: Message,
                                    dialog_manager: DialogManager):
    i18n = dialog_manager.middleware_data.get('i18n')
    service_param = dialog_manager.dialog_data.get("service_param")
    service_work_param = dialog_manager.dialog_data.get("service_work_param")
    m_text = i18n.service.edit.total.price.error.text()

    if service_param == "total_price" or service_work_param == "price":
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


    return True
