from datetime import datetime
from typing import Dict

from sqlalchemy import insert

from database import Car, ServiceTypeEnum, get_async_session, ServiceRecord, ServiceWork


async def create_service_record(user_id: int,
                                service_type: str,
                                car: Car | None = None,
                                title: str | None = None,
                                description: str | None = None,
                                total_price: str | None = None,
                                service_name: str | None = None,
                                comment: str | None = None,
                                date: datetime | None = None,
                                **kwargs) -> int:
    """
    Создает объект сервиса в базе данных
    """
    updated_value = {"user_id": user_id,
                     "service_type": ServiceTypeEnum[service_type],
                     "title": title,
                     "service_date": date}

    if car:
        updated_value.update(car_id=car.id)
    if description:
        updated_value.update(description=description)
    if total_price:
        updated_value.update(total_price=float(total_price))
    if service_name:
        updated_value.update(service_center=service_name)
    if comment:
        updated_value.update(comment=comment)

    async with get_async_session() as session:
        query = await session.execute(insert(ServiceRecord).values(
            **updated_value
        ).returning(ServiceRecord.id))
        service_id = query.scalar()
        await session.commit()

        return service_id


async def create_service_work_record(model,
                                     data: Dict[int, Dict],
                                     service_id: int) -> None:
    """
    Создает объект сервисных работ или запчастей в базе данных
    """
    if data is None:
        return

    async with get_async_session() as session:
        records = []
        for key, value in data.items():
            records.append({"service_record_id": service_id, **value})

        await session.run_sync(
            lambda sync_session: sync_session.bulk_insert_mappings(
                model,
                records
            )
        )
        await session.commit()

