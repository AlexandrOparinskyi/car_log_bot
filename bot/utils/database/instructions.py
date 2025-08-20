from typing import List, Optional

from sqlalchemy import select

from database import Instruction, get_async_session


async def get_all_instructions(for_start: bool = False) -> List[Instruction]:
    """
    Возвращает список всех инструкций отсортированные по ID
    :param for_start: Если передам параметр True, вернет только стартовые
    инструкции
    :return: Список инструкций
    """
    async with get_async_session() as session:
        stmt = select(Instruction)
        if for_start:
            stmt = stmt.where(Instruction.for_start == True)
        return await session.scalars(stmt.order_by(Instruction.id))


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
