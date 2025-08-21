from typing import List, Optional

from sqlalchemy import select

from database import Instruction, get_async_session


async def get_all_instructions() -> List[Instruction]:
    """
    Возвращает все инструкции

    :return: Список инструкций
    """
    async with get_async_session() as session:
        return await session.scalars(select(Instruction).order_by(
            Instruction.id
        ))


async def get_instruction_by_id(i_id: int) -> Optional[Instruction]:
    """
    Возвращает инструкцию по выбранному ID

    :param i_id: ID инструкции
    :return: Выбранную инструкцию
    """
    async with get_async_session() as session:
        return await session.scalar(
            select(Instruction).where(Instruction.id == i_id)
        )
