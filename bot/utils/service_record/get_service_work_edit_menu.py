from typing import Dict

from fluentogram import TranslatorHub


def get_service_work_data_edit_menu(
        i18n: TranslatorHub,
        data: Dict[str, str]
) -> str:
    """
    Генерирует текст и кнопки для обновления/добавления работ сервиса
    :param i18n: TranslatorHub
    :param data: Dict[str, str]
    :return: str
    """
    name = data.get("name")
    price = data.get("price")
    description = data.get("description")
    text = "\n"

    if name:
        text += f"🏷️ <b>Название:</b> {name}\n"
    if price:
        text += f"💰 <b>Стоимость:</b> {price}\n"
    if description:
        text += f"📋 <b>Описание:</b> {description}\n"

    return text
