from typing import Dict

from fluentogram import TranslatorHub


def get_service_part_data_edit_menu(
        i18n: TranslatorHub,
        data: Dict[str, str]
) -> str:
    """
    Генерирует текст и кнопки для обновления/добавления pзапчастей сервиса
    :param i18n: TranslatorHub
    :param data: Dict[str, str]
    :return: str
    """
    name = data.get("name")
    total_price = data.get("total_price")
    part_number = data.get("part_number")
    price_per_unit = data.get("price_per_unit")
    quantity = data.get("quantity")
    comment = data.get("comment")
    text = "\n"

    if name:
        text += f"🏷️ <b>Название:</b> {name}\n"
    if total_price:
        text += f"💰 <b>Стоимость:</b> {total_price} ₽\n"
    elif quantity and price_per_unit:
        t_price = round(int(quantity) * float(price_per_unit), 2)
        text += f"💰 <b>Стоимость:</b> {t_price}\n ₽"
    if part_number:
        text += f"🔍 <b>Артикул:</b> {part_number}\n"
    if quantity:
        text += f"🔢 <b>Количество:</b> {quantity}\n"
    if price_per_unit:
        text += f"🧮 <b>Цена за единицу:</b> {price_per_unit} ₽\n"
    elif quantity and total_price:
        price_per_u = round(float(total_price) / int(quantity), 2)
        text += f"🧮 <b>Цена за единицу:</b> {price_per_u} ₽\n"
    if comment:
        text += f"💬 <b>Комментарий:</b> {comment}\n"

    return text


