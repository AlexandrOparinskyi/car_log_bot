from typing import Tuple

from fluentogram import TranslatorHub


def get_buttons_for_edit_part(i18n: TranslatorHub) -> Tuple:
    """
    Генерирует кнопки для изменения/добавления данных для запчастей
    :param i18n: TranslatorHub
    :return: Tuple[str, List]
    """
    return (
        (i18n.service.work.name.button(), "name"),
        (i18n.service.work.price.button(), "total_price"),
        (i18n.service.work.description.button(), "description"),
        (i18n.service.part.price.per.unit.button(), "price_per_unit"),
        (i18n.service.part.number.button(), "part_number"),
        (i18n.service.part.comment.button(), "comment")
    )
