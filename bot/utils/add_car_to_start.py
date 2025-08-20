from typing import Dict

from database.models.cars import EngineTypeEnum, TransmissionTypeEnum


def generate_text_for_car_edit_menu(data: Dict[str, str]) -> str:
    if len(data) < 3:
        return ""

    text = "\n"

    if data.get("mark"):
        text += f"• 🚗 <b>Производитель:</b> {data.get('mark')}\n"
    if data.get("model"):
        text += f"• 🚙 <b>Модельный ряд:</b> {data.get('model')}\n"
    if data.get("year"):
        text += f"• 📅 <b>Год выпуска:</b> {data.get('year')}\n"
    if data.get("color"):
        text += f"• 🎨 <b>Цветовое решение:</b> {data.get('color')}\n"
    if data.get("mileage"):
        text += f"• 🛣️ <b>Общий пробег:</b> {data.get('mileage')}\n"
    if data.get("engine"):
        text += (f"• ⚙️ <b>Двигатель:</b> "
                 f"{EngineTypeEnum[data.get('engine')].value}\n")
    if data.get("transmission"):
        text += (f"• 🔄 <b>Трансмиссия:</b> "
                 f"{TransmissionTypeEnum[data.get('transmission')].value}\n")

    return text

# • 🏷️ <b>Идентификационное имя:</b> Моя Ласточка
# • 🚗 <b>Производитель:</b> Toyota
# • 🚙 <b>Модельный ряд:</b> Camry
# • 📅 <b>Год выпуска с конвейера:</b> 2020
# • 🎨 <b>Цветовое решение:</b> Чёрный
# • 🛣️ <b>Общий пробег:</b> 75 000 км
# • ⚙️ <b>Двигатель:</b> Бензин
# • 🔄 <b>Трансмиссия:</b> Автоматическая коробка передач
