from sqlalchemy import select, insert, delete

from database import Car, get_async_session


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
