from datetime import datetime
from typing import Dict

from fluentogram import TranslatorHub

from database import User, Car


def get_refuel_data(i18n: TranslatorHub,
                    data: Dict[str, str | Car],
                    user: User) -> str:
    """
    Возвращает текст для информации о внесении данных о заправке
    :param i18n: словарь с текстами
    :param data: dialog_data
    :param user: User
    :return: текст
    """
    text = f"\n\n"
    car = data.get("car")
    now_date = datetime.now().strftime("%d.%m.%Y")

    if car:
        text += f"🚗 <b>Автомобиль:</b> {car.name}\n"
        if car.mileage:
            text += f"🛣️ <b>Пробег:</b> {car.mileage}км\n"

    if data.get("total_price"):
        price = data.get("total_price")
        if "," in price:
            price = price.replace(",", ".")
        total_price = round(float(price), 2)
        text += f"💵 <b>Общая сумма:</b> {total_price} ₽\n"

    text += f"📅 <b>Дата заправки:</b> {now_date}\n"

    return text


# 🚗 <b>Автомобиль:</b> {car_name}
# ⛽ <b>АЗС:</b> {gas_station}
# 🛣️ <b>Пробег:</b> {mileage} км
# 💧 <b>Литры:</b> {liters} л
# 💰 <b>Цена за литр:</b> {price_per_liter} ₽
# 💵 <b>Общая сумма:</b> {total_cost} ₽
# 🔧 <b>Тип топлива:</b> {fuel_type}
# 🎯 <b>Полный бак:</b> {full_tank_status}
# 📅 <b>Дата заправки:</b> {date}
# 📝 <b>Комментарий:</b> {comment}
