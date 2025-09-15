from datetime import date, timedelta
from typing import Tuple, List, Optional

from fluentogram import TranslatorHub

from database import Car, ServiceTypeEnum


def get_service_edit_text_and_buttons(
        i18n: TranslatorHub,
        service_param: str,
        cars: List[Optional[Car]]
) -> Tuple[str, List]:
    text = i18n.service.edit.error.param.text()
    buttons = []

    if service_param == "title":
        text = i18n.service.edit.title.text()
    if service_param == "description":
        text = i18n.service.edit.description.text()
    if service_param == "service_name":
        text = i18n.service.service.name.text()
    if service_param == "total_price":
        text = i18n.service.edit.total.price.text()
    if service_param == "comment":
        text = i18n.service.edit.comment.text()

    if service_param == "car":
        text = i18n.service.edit.car.text()
        buttons = [(c.name, c.id) for c in cars]

    if service_param == "service_type":
        text = i18n.service.edit.type.text()
        buttons = [(g.value, str(g).split(".")[-1])
                   for g in ServiceTypeEnum]

    if service_param == "date":
        text = i18n.service.edit.date.text()
        buttons = [("Вчера", date.today() - timedelta(days=1)),
                   ("Сегодня", date.today()),
                   ("Выбрать дату", "select_date")]

    return text, buttons
