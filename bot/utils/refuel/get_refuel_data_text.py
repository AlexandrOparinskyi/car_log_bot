from datetime import datetime
from typing import Dict

from fluentogram import TranslatorHub

from database import (User,
                      Car,
                      EngineTypeEnum,
                      FuelTypeEnum,
                      GasStationTypeEnum)


def get_price_per_liter(total_price: float,
                        liters: float,) -> float | int:
    """
    Возвращает int или float

    :param total_price: цена
    :param liters: кол-во литров
    "return: значение int или float
    """
    price = round(total_price / liters, 2)

    if str(price)[-1] == "0":
        return int(price)

    return price


def get_comment(comment: str) -> str:
    """
    Возвращает комментарий в зависимости от его длинны
    Если больше 10 символов, то в конце идет троеточие

    :param comment: комментарий
    :return: комментарий с троеточием или без
    """
    if len(comment) > 10:
        return f"{comment[:10]}..."

    return comment


def get_refuel_data(i18n: TranslatorHub,
                    data: Dict[str, str | Car | datetime],
                    user: User) -> str:
    """
    Возвращает текст для информации о внесении данных о заправке
    :param i18n: словарь с текстами
    :param data: dialog_data
    :param user: User
    :return: текст
    """
    text = "\n\n"
    car = data.get("car")
    now_date = datetime.now().strftime("%d.%m.%Y")
    fuel_type = None

    if car:
        text += f"🚗 <b>Автомобиль:</b> {car.name}\n"
        if car.mileage:
            text += f"🛣️ <b>Пробег:</b> {car.mileage}км\n"
        if car.engine_type == EngineTypeEnum.PETROL:
            fuel_type = FuelTypeEnum.PETROL_95.value
        if car.engine_type == EngineTypeEnum.DIESEL:
            fuel_type = FuelTypeEnum.DIESEL.value
        if car.engine_type == EngineTypeEnum.GAS:
            fuel_type = FuelTypeEnum.GAS.value

    if data.get("fuel_type"):
        fuel_type = FuelTypeEnum[data.get("fuel_type")].value

    if fuel_type:
        text += f"🔧 <b>Тип топлива:</b> {fuel_type}\n"

    price = data.get("total_price")
    try:
        total_price = int(price)
    except ValueError:
        total_price = round(float(price), 2)
    text += f"💵 <b>Общая сумма:</b> {total_price} ₽\n"

    liters = data.get("liters")
    if liters:
        price_per_liter = get_price_per_liter(total_price, float(liters))
        text += (f"💧 <b>Литры:</b> {liters}\n"
                 f"💰 <b>Цена за литр:</b> {price_per_liter} ₽\n")

    gas_station = data.get("gas_station")
    if gas_station:
        text += f"⛽ <b>АЗС:</b> {GasStationTypeEnum[gas_station].value}\n"

    if data.get("comment"):
        comment = get_comment(data.get("comment"))
        text += f"📝 <b>Комментарий:</b> {comment}\n"

    data_date = data.get("date")
    if data_date:
        now_date = data_date.strftime("%d.%m.%Y")
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
