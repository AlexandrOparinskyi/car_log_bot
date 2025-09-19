from datetime import datetime
from typing import Dict

from fluentogram import TranslatorHub

from database import Car
from ..general import reduce_text_for_data
from ..database import get_car_by_id


async def get_purchase_data_text(i18n: TranslatorHub,
                           data: Dict[str, str | Car | datetime]):
    text = "\n"
    car = data.get("car")
    total_price = data.get("total_price")
    quantity = data.get("quantity")
    price_per_unit = data.get("price_per_unit")
    date = data.get("date")
    comment = data.get("comment")
    title = data.get("title")

    if not date:
        date = date=datetime.now()
        data.update(date=date)

    if not title:
        title = f"Покупка {date.strftime("%d.%m.%Y")}\n"
        data.update(title=title)

    if title:
        text += f"🏷️ <b>Название:</b> {title}"

    if car:
        car = await get_car_by_id(int(car))
        text += f"🚗 <b>Автомобиль:</b> {car.name}\n"

    if total_price:
        text += f"💵 <b>Общая сумма:</b> {total_price} ₽\n"
    elif price_per_unit and quantity:
        price = round(float(price_per_unit) * int(quantity), 2)
        text += f"💵 <b>Общая сумма:</b> {price} ₽\n"

    if quantity:
        text += f"🔢 <b>Количество:</b> {quantity}\n"

    if price_per_unit:
        text += f"💰 <b>Цена за единицу:</b> {price_per_unit} ₽\n"
    elif total_price and quantity:
        price = round(float(total_price) / int(quantity), 2)
        text += f"💰 <b>Цена за единицу:</b> {price} ₽\n"

    if date:
        text += f"📅 <b>Дата покупки:</b> {date.strftime("%d.%m.%Y")}\n"

    if comment:
        c_text = reduce_text_for_data(comment, 15)
        text += f"💬 <b>Комментарий:</b> {c_text}\n"

    return text
