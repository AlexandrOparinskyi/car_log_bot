from typing import Tuple

from fluentogram import TranslatorHub


def get_button_for_service_edit_menu(i18n: TranslatorHub) -> Tuple:
    """
    Генерирует кнопки для изменения данных сервиса
    :param i18n: TranslatorHub
    :return: Tuple
    """
    return (
        (i18n.service.car.button(), "car"),
        (i18n.service.total.price.button(), "total_price"),
        (i18n.service.title.button(), "title"),
        (i18n.service.description.button(), "description"),
        (i18n.service.date.button(), "date"),
        (i18n.service.type.button(), "service_type"),
        (i18n.service.service.name.button(), "service_name"),
        (i18n.service.comment.button(), "comment"),
    )
