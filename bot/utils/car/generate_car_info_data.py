from typing import Dict

from database import (Car,
                      EngineTypeEnum,
                      TransmissionTypeEnum)


def generate_car_info(car: Car, data: Dict[str, str]) -> str:
    """
    Возвращает информацию о машине. Изначально берет её из базы данных,
    а затем заполняет данными из словаря

    :param car: модель машины
    :param data: словарь dialog_data
    :return:
    """
    car_data = {}
    if car.mark:
        car_data["mark"] = f"• 🚗 <b>Производитель:</b> {car.mark}\n"
    if car.model:
        car_data["model"] = f"• 🚙 <b>Модельный ряд:</b> {car.model}\n"
    if car.year:
        car_data["year"] = f"• 📅 <b>Год выпуска:</b> {car.year}\n"
    if car.color:
        car_data["color"] = f"• 🎨 <b>Цветовое решение:</b> {car.color}\n"
    if car.mileage:
        car_data["mileage"] = f"• 🛣️ <b>Общий пробег:</b> {car.mileage}\n"
    if car.engine_type:
        car_data["engine"] = (f"• ⚙️ <b>Двигатель:</b> "
                              f"{car.engine_type.value}\n")
    if car.transmission_type:
        car_data["transmission"] = (f"• 🔄 <b>Трансмиссия:</b> "
                                    f"{car.transmission_type.value}\n")

    if data.get("mark"):
        car_data["mark"] = f"• 🚗 <b>Производитель:</b> {data.get('mark')}\n"
    if data.get("model"):
        car_data["model"] = f"• 🚙 <b>Модельный ряд:</b> {data.get('model')}\n"
    if data.get("year"):
        car_data["year"] = f"• 📅 <b>Год выпуска:</b> {data.get('year')}\n"
    if data.get("color"):
        car_data["color"] = (f"• 🎨 <b>Цветовое решение:</b>"
                             f" {data.get('color')}\n")
    if data.get("mileage"):
        car_data["mileage"] = (f"• 🛣️ <b>Общий пробег:</b> "
                               f"{data.get('mileage')}\n")
    if data.get("engine"):
        car_data["engine"] = (f"• ⚙️ <b>Двигатель:</b> "
                              f"{EngineTypeEnum[data.get('engine')].value}\n")
    if data.get("transmission"):
        transmission = TransmissionTypeEnum[data.get('transmission')].value
        car_data["transmission"] = f"• 🔄 <b>Трансмиссия:</b> {transmission}\n"

    return "\n" + "".join(car_data.values())
