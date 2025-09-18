from typing import Tuple

from fluentogram import TranslatorHub


def get_button_for_edit_purchase(i18n: TranslatorHub) -> Tuple:
    return (
        (i18n.edit.purchase.title.button(), "title"),
        (i18n.edit.purchase.car.button(), "car"),
        (i18n.edit.purchase.total.price.button(), "total_price"),
        (i18n.edit.purchase.quantity.button(), "quantity"),
        (i18n.edit.purchase.price.per.unit.button(), "price_per_unit"),
        (i18n.edit.purchase.date.button(), "date"),
        (i18n.edit.purchase.comment.button(), "comment"),
    )
