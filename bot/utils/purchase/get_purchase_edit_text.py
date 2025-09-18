from typing import Dict, Tuple, List

from fluentogram import TranslatorHub

from database import Car


def get_purchase_edit_text(i18n: TranslatorHub,
                           data: Dict[str, str],
                           cars: List[Car]) -> Tuple[str, List]:
    text = i18n.purchase.edit.error.param.text()
    buttons = []
    purchase_param = data.get("purchase_param")

    if purchase_param == "title":
        text = i18n.purchase.edit.title.text()
    if purchase_param == "total_price":
        text = i18n.purchase.edit.total.price.text()
    if purchase_param == "price_per_unit":
        text = i18n.purchase.edit.price.per.unit.text()
    if purchase_param == "quantity":
        text = i18n.purchase.edit.quantity.text()
    if purchase_param == "date":
        text = i18n.purchase.edit.date.text()
    if purchase_param == "comment":
        text = i18n.purchase.edit.comment.text()

    if purchase_param == "car":
        text = i18n.purchase.edit.car.text()
        buttons = [(c.name, c.id) for c in cars]

    return text, buttons
