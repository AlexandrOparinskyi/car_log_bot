from datetime import datetime
from typing import Dict

from fluentogram import TranslatorHub

from database import Car, ServiceTypeEnum
from ..general import reduce_text_for_data
from ..database import get_car_by_id


async def get_service_data_text(
        i18n: TranslatorHub,
        data: Dict[str, str | Car | datetime | Dict]
) -> str:
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

    service_work_data = data.get("service_work_data")
    service_part_data = data.get("service_part_data")
    price = 0
    try:
        for i, j in service_work_data.items():
            for key, value in j.items():
                if key == "price":
                    price += float(value)
    except ValueError:
        pass
    except AttributeError:
        pass
    try:
        for i, j in service_part_data.items():
            for key, value in j.items():
                if key == "total_price":
                    price += float(value)
    except TypeError:
        pass
    except AttributeError:
        pass

    total_price = data.get("total_price")
    if total_price:
        text += f"💰 <b>Стоимость:</b> {total_price} ₽\n"
    elif price:
        text += f"💰 <b>Стоимость:</b> {price} ₽\n"
        data.update(total_price=str(price))

    if car:
        car = await get_car_by_id(int(car))
        text += f"🚗 <b>Автомобиль:</b> {car.name}\n"
        if car.mileage:
            text += f"🛣️ <b>Пробег:</b> {car.mileage}\n"

    description = data.get("description")
    if description:
        d_text = reduce_text_for_data(description, 15)
        text += f"📃 <b>Описание:</b> {d_text}\n"

    service_name = data.get("service_name")
    if service_name:
        text += f"🏢 <b>Сервис:</b> {service_name}\n"

    comment = data.get("comment")
    if comment:
        c_text = reduce_text_for_data(comment, 15)
        text += f"💬 <b>Комментарий:</b> {c_text}\n"

    text += f"🛠️ <b>Тип работ:</b> {ServiceTypeEnum[service_type].value}\n"
    text += f"🗓️ <b>Дата:</b> {date}\n"

    if service_part_data:
        text += f"🛞 <b>Добавлено запчастей:</b> {len(service_part_data)}\n"
    if service_work_data:
        text += f"🔧 <b>Добавлено работ:</b> {len(service_work_data)}\n"

    return text
