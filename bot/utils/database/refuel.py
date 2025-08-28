from typing import Optional

from sqlalchemy import insert

from database import Car, get_async_session, RefuelRecord


async def create_refuel_record(car: Optional[Car] = None):
    async with get_async_session() as session:
        await session.execute(insert(RefuelRecord).values(
        ))

