from datetime import datetime

from sqlalchemy import insert

from database import Car, get_async_session, Purchase


async def save_purchase(user_id: int,
                        title: str,
                        total_price: str,
                        quantity: str | None = None,
                        price_per_unit: str | None = None,
                        date: datetime | None = None,
                        car: Car | None = None,
                        comment: str | None = None,
                        **kwargs) -> None:
    """
    Сохраняет покупку в базу данных
    :param user_id: int
    :param title: str
    :param total_price: str
    :param quantity: str
    :param price_per_unit: str
    :param date: datetime
    :param car: Car
    :param comment: str
    :return: None
    """
    updated_data = {"user_id": user_id,
                    "title": title,
                    "total_price": total_price,
                    "quantity": int(quantity),
                    "purchase_date": date}

    if price_per_unit:
        updated_data.update(price_per_unit=price_per_unit)
    else:
        price = float(total_price) / int(quantity)
        updated_data.update(price_per_unit=price)

    if car:
        updated_data.update(car_id=car.id)

    if comment:
        updated_data.update(comment=comment)

    async with get_async_session() as session:
        await session.execute(insert(Purchase).values(
            **updated_data
        ))
        await session.commit()
