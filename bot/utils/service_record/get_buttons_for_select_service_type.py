from typing import List

from database import ServiceTypeEnum


def get_buttons_for_select_service_type() -> List:
    """
    Создает кнопки для выбора типа сервисных работ

    :return: кортеж с кнопками
    """
    buttons = [(i.value, str(i).split(".")[-1]) for i in ServiceTypeEnum]
    return buttons
