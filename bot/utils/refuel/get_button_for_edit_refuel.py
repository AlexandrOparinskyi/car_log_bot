from typing import Tuple, Dict

from fluentogram import TranslatorHub


def get_refuel_button(i18n: TranslatorHub) -> Tuple:
    """
    Возвращает кнопки для изменения характеристик заправки

    :param i18n: словарь со словами
    :return: кортеж с кнопками
    """
    return (
        (i18n.edit.refuel.total.price.button(), "total_sum"),
        (i18n.edit.refuel.car.button(), "car"),
        (i18n.edit.refuel.liters.button(), "liters"),
        (i18n.edit.refuel.fuel.type.button(), "fuel_type"),
        (i18n.edit.refuel.gas.station.button(), "gas_station"),
        (i18n.edit.refuel.date.button(), "date"),
        (i18n.edit.refuel.comment.button(), "comment"),
    )
