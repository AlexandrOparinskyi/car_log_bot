from typing import Optional

from sqlalchemy import select, insert, delete, update, Engine

from database import Car, get_async_session
from database.models.cars import EngineTypeEnum, TransmissionTypeEnum


async def get_car_by_id(car_id: int) -> Car:
    """
    Возвращает машину по переданному ID
    :param car_id: ID машины
    :return: машину
    """
    async with get_async_session() as session:
        return await session.scalar(select(Car).where(Car.id == car_id))


async def create_new_car(name: str, user_id: int) -> int:
    """
    Создает машину в базе данных с одним именем
    :param user_id: ID пользователя
    :param name: название/кличка машины
    :return:
    """
    async with get_async_session() as session:
        result = await session.execute(insert(Car).values(
            name=name,
            user_id=user_id
        ).returning(Car.id))
        await session.commit()
        car_id = result.scalar()
        return car_id


async def delete_car_by_id(car_id: int) -> None:
    """
    Удаление машины из базу данных под выбранным ID
    :param car_id: ID машины
    :return:
    """
    async with get_async_session() as session:
        await session.execute(delete(Car).where(Car.id == car_id))
        await session.commit()


async def update_car_by_id(car_id: int,
                           car_name: str,
                           mark: Optional[str] = None,
                           model: Optional[str] = None,
                           year: Optional[str] = None,
                           color: Optional[str] = None,
                           mileage: Optional[str] = None,
                           engine: Optional[str] = None,
                           transmission: Optional[str] = None,) -> None:
    """
    Обновляет машину по тем данным, которые передали
    :param car_id: ID машины
    :param car_name: имя
    :param mark: марка
    :param model: модель
    :param year: год выпуска
    :param color: цвет
    :param mileage: пробег
    :param engine: тип двигателя
    :param transmission: тип коробки передач
    :return:
    """
    update_values = {
        "name": car_name,
        "mark": mark,
        "model": model,
        "color": color
    }

    if year:
        update_values.update(year=int(year))

    if mileage:
        update_values.update(mileage=int(mileage))

    if engine:
        update_values.update(engine_type=EngineTypeEnum[engine])

    if transmission:
        update_values.update(transmission_type=TransmissionTypeEnum[transmission])

    async with get_async_session() as session:
        await session.execute(update(Car).where(Car.id == car_id).values(
            **update_values
        ))

        await session.commit()
