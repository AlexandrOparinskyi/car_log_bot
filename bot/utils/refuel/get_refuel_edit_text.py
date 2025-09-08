from datetime import timedelta, date
from typing import Tuple, List, Optional

from fluentogram import TranslatorHub

from database import Car, FuelTypeEnum, GasStationTypeEnum


def get_refuel_edit_text_and_buttons(
        i18n: TranslatorHub,
        refuel_param: str,
        cars: List[Optional[Car]]
) -> Tuple[str, List]:
    text = i18n.refuel.edit.error.param.text()
    buttons = []

    if refuel_param == "total_price":
        text = i18n.refuel.edit.total.price.text()
    if refuel_param == "liters":
        text = i18n.refuel.edit.liters.text()
    if refuel_param == "comment":
        text = i18n.refuel.edit.comment.text()

    if refuel_param == "car":
        text = i18n.refuel.edit.car.text()
        buttons = [(c.name, c.id) for c in cars]

    if refuel_param == "fuel_type":
        text = i18n.refuel.edit.fuel.type.text()
        buttons = [(f.value, str(f).split(".")[-1])
                   for f in FuelTypeEnum]

    if refuel_param == "gas_station":
        text = i18n.refuel.edit.gas.station.text()
        buttons = [(g.value, str(g).split(".")[-1])
                   for g in GasStationTypeEnum]

    if refuel_param == "date":
        text = i18n.refuel.edit.date.text()
        buttons = [("Вчера", date.today() - timedelta(days=1)),
                   ("Сегодня", date.today()),
                   ("Выбрать дату", "select_date")]

    return text, buttons
