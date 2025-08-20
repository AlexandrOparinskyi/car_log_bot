from typing import Optional

from sqlalchemy import select, insert

from database import get_async_session, User


async def exists_user(user_id: int) -> bool:
    """
    Проверка на существование пользователя по ID
    :param user_id: ID пользователя
    :return Наличие пользователя в базе данных:
    """
    async with get_async_session() as session:
        user = await session.scalar(select(User).where(
            User.id == user_id,
        ))

    return user is not None


async def create_user(user_id: int,
                      username: Optional[str],
                      first_name: str,
                      last_name: Optional[str]) -> None:
    """
    Создает пользователя
    :param user_id: ID пользователя
    :param username: username пользователя
    :param first_name: имя пользователя
    :param last_name: фамилия пользователя
    :return:
    """
    async with get_async_session() as session:
        await session.execute(insert(User).values(
            id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        ))
        await session.commit()


async def get_user_by_id(user_id: int) -> User:
    """
    Возвращает пользователя под переданным ID
    :param user_id: ID пользователя
    :return: пользователя
    """
    async with get_async_session() as session:
        return await session.scalar(select(User).where(User.id == user_id))
