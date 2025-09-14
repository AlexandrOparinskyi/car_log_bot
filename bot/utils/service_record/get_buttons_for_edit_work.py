from typing import Tuple

from fluentogram import TranslatorHub


def get_buttons_for_edit_work(i18n: TranslatorHub) -> Tuple:
    """
    Генерирует кнопки для изменения/добавления данных для работы
    :param i18n: TranslatorHub
    :return: Tuple[str, List]
    """
    return (
        (i18n.service.work.name.button(), "name"),
        (i18n.service.work.price.button(), "price"),
        (i18n.service.work.description.button(), "description"),
    )
