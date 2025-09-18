from typing import List

from database import RefuelRecord, ServiceRecord, Purchase


def get_normal_title(title: str) -> str:
    if len(title) < 14:
        return title

    return f"{title[:11]}..."


def get_three_latest_records(lst: List) -> str:
    if not lst:
        return ("<b>🌱 История только начинается</b>\n"
                "Здесь появятся твои первые записи о заправках, "
                "сервисе и покупках")

    text = "<b>📅 Последние операции:</b>\n"

    records = list(sorted(
        lst,
        key=lambda record: record.created_at,
        reverse=True
    ))[:3]

    for record in records:
        price = (f"{round(record.total_price, 2)} ₽" if record.total_price
                 else "❓ ₽")
        if isinstance(record, RefuelRecord):
            text += (f"⛽ {record.refuel_date.strftime('%d.%m.%Y')} • "
                     f"Заправка • "
                     f"{price}\n")
        if isinstance(record, ServiceRecord):
            text += (f"🛠️ {record.service_date.strftime('%d.%m.%Y')} • "
                     f"{get_normal_title(record.title)} • "
                     f"{price}\n")
        if isinstance(record, Purchase):
            text += (f"💵 {record.purchase_date.strftime('%d.%m.%Y')} • "
                     f"{get_normal_title(record.title)} • "
                     f"{price}\n")

    return text
