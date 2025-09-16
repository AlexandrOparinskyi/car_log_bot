from typing import Dict

from fluentogram import TranslatorHub


def get_service_part_edit_text(i18n: TranslatorHub,
                               data: Dict[str, str]) -> str:
    text =i18n.service.edit.error.param.text()
    service_part_param = data.get("service_part_param")

    if service_part_param == "name":
        text = i18n.service.part.edit.name.text()
    if service_part_param == "total_price":
        text = i18n.service.part.edit.total.price.text()
    if service_part_param == "description":
        text = i18n.service.part.edit.description.text()
    if service_part_param == "quantity":
        text = i18n.service.part.edit.quantity.text()
    if service_part_param == "price_per_unit":
        text = i18n.service.part.edit.price.per.unit.text()
    if service_part_param == "part_number":
        text = i18n.service.part.edit.part.number.text()
    if service_part_param == "comment":
        text = i18n.service.part.edit.comment.text()

    return text
