from datetime import datetime
from typing import Optional

from sqlalchemy import insert

from database import (Car,
                      get_async_session,
                      RefuelRecord,
                      FuelTypeEnum, GasStationTypeEnum, EngineTypeEnum)
from ..refuel_record import get_price_per_liter


async def create_refuel_record(user_id: int,
                               total_price: float,
                               car: Optional[Car] = None,
                               liters: Optional[str] = None,
                               price_per_liter: Optional[str] = None,
                               fuel_type: Optional[str] = None,
                               gas_station: Optional[str] = None,
                               time: Optional[float] = None,
                               full_tank: Optional[bool] = False,
                               comment: Optional[str] = None,
                               date: Optional[datetime] = None,
                               **kwargs):
    updated_values = {"user_id": user_id,
                      "total_price": float(total_price),
                      "full_tank": full_tank}

    if car:
        updated_values.update(car_id=car.id,
                              mileage=car.mileage)
        if car.engine_type == EngineTypeEnum.PETROL:
            updated_values.update(fuel_type=FuelTypeEnum.PETROL_95)
        if car.engine_type == EngineTypeEnum.DIESEL:
            updated_values.update(fuel_type=FuelTypeEnum.DIESEL)
        if car.engine_type == EngineTypeEnum.GAS:
            updated_values.update(fuel_type=FuelTypeEnum.GAS)

    if liters:
        price_per_liter = get_price_per_liter(float(total_price),
                                              float(liters))
        updated_values.update(liters=float(liters),
                              price_per_liter=float(price_per_liter))
    if price_per_liter:
        updated_values.update(price_per_liter=float(price_per_liter))
    if fuel_type:
        updated_values.update(fuel_type=FuelTypeEnum[fuel_type])
    if gas_station:
        updated_values.update(gas_station=GasStationTypeEnum[gas_station])
    if time:
        updated_values.update(time=float(time))
    if comment:
        updated_values.update(comment=comment)
    if date:
        updated_values.update(refuel_date=date)
    else:
        updated_values.update(refuel_date=datetime.now())

    async with get_async_session() as session:
        await session.execute(insert(RefuelRecord).values(
            **updated_values
        ))
        await session.commit()
