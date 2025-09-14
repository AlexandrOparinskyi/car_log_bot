from typing import Tuple, Dict

from fluentogram import TranslatorHub

from database.models.cars import EngineTypeEnum, TransmissionTypeEnum


def get_button_for_add_components(i18n: TranslatorHub) -> Tuple:
    """
    Функция для генерации кнопок изменения параметров машины
    :param i18n: словарь слов
    :return: кортеж с кнопками вида (кнопка, id кнопки)
    """
    return ((i18n.mark.button(), "mark"),
            (i18n.model.button(), "model"),
            (i18n.year.button(), "year"),
            (i18n.color.button(), "color"),
            (i18n.mileage.button(), "mileage"),
            (i18n.engine.type.button(), "engine"),
            (i18n.transmission.type.button(), "transmission"))


def get_text_for_select_part(i18n: TranslatorHub) -> Dict[str, Tuple]:
    """
    Функция для генерации текста при добавлении определенного параметра.
    При изменении двигателя или коробки так же передаются кнопки
    :param i18n: словарь слов
    :return: словарь с текстами и кнопками
    """
    engine_buttons = [(i.value, str(i).split(".")[-1])
                      for i in EngineTypeEnum]
    transmission_buttons = [(i.value, str(i).split(".")[-1])
                            for i in TransmissionTypeEnum]

    return {"mark": (i18n.edit.mark.text(), []),
            "model": (i18n.edit.model.text(), []),
            "year": (i18n.edit.year.text(), []),
            "color": (i18n.edit.color.text(), []),
            "mileage": (i18n.edit.mileage.text(), []),
            "engine": (i18n.edit.engine.text(), engine_buttons),
            "transmission": (i18n.edit.transmission.text(),
                             transmission_buttons)}


def replace_dot_at_comma(text: str) -> str:
    """
    Заменяет запятую на точку для правильной цены

    :param text: ввод пользователя
    "return" текст
    """
    if "," in text:
        return text.replace(",", ".")

    return text


def get_paginator_buttons(many: bool,
                          selected: int,
                          length_data: int) -> Tuple:
    """
    Генерирует кнопки для пагинации
    :param many: bool
    :param selected: int
    :param length_data: int
    :return: Tuple
    """
    if many:
        return (
            ("<<", "prev"),
            (f"{selected}/{length_data}", "selected_work"),
            (">>", "next")
        )
    return ()


def reduce_text_for_data(text: str, num: int) -> str:
    """
    Сокращает текст на заданную длину
    :param text: str
    :param num: int
    :return: str
    """
    if len(text) < num:
        return text

    return text[:num] + "..."
