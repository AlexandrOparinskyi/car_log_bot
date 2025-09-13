from datetime import datetime
from typing import Dict

from fluentogram import TranslatorHub

from database import Car, ServiceTypeEnum


def get_service_data_text(i18n: TranslatorHub,
                          data: Dict[str, str | Car | datetime]) -> str:
    """
    Генерирует текст для подробного описания измененных характеристик
    :param i18n: TranslatorHub
    :param data: dialog_data
    :return: str
    """
    text = "\n"
    date = data.get("date")
    if date:
        if isinstance(date, str):
            year, month, day = map(int, date.split("-"))
            date = datetime(year, month, day).strftime("%d.%m.%Y")
        else:
            date = date.strftime("%d.%m.%Y")
    else:
        date = datetime.now().strftime("%d.%m.%Y")
    car = data.get("car")
    service_type = data.get("service_type")

    title = data.get("title")
    if not title:
        name = f"{ServiceTypeEnum[service_type].value} {date}"
        text += f"️🏷️ <b>Название:</b> {name}\n"
    else:
        text += f"️🏷️ <b>Название:</b> {title}\n"

    total_price = data.get("total_price")
    if total_price:
        text += f"💰 <b>Стоимость:</b> {total_price} ₽\n"

    if car:
        text += f"🚗 <b>Автомобиль:</b> {car.name}\n"
        if car.mileage:
            text += f"🛣️ <b>Пробег:</b> {car.mileage}\n"

    description = data.get("description")
    if description:
        text += f"📃 <b>Описание:</b> {description}\n"

    service_name = data.get("service_name")
    if service_name:
        text += f"🏢 <b>Сервис:</b> {service_name}\n"

    comment = data.get("comment")
    if comment:
        text += f"💬 <b>Комментарий:</b> {comment}\n"

    text += f"🛠️ <b>Тип работ:</b> {ServiceTypeEnum[service_type].value}\n"
    text += f"🗓️ <b>Дата:</b> {date}\n"

    return text
