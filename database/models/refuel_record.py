import enum
from datetime import datetime

from sqlalchemy import ForeignKey, Enum, values, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class FuelTypeEnum(enum.Enum):
    PETROL_92 = "92"
    PETROL_95 = "95"
    PETROL_98 = "98"
    PETROL_100 = "100"
    DIESEL = "Дизель"
    GAS = "Газ"
    ELECTRIC = "Электро"


class GasStationTypeEnum(enum.Enum):
    LUKOIL = "Лукойл"
    ROSNEFT = "Роснефть"
    GAZPROMNEFT = "Газпромнефть"
    TATNEFT = "Татнефть"
    SHELL = "Shell"
    BP = "BP"
    OTHER = "Другая"


class RefuelRecord(Base):
    __tablename__ = 'refuel_records'

    id: Mapped[int] = mapped_column(primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey('cars.id',
                                                   ondelete="cascade"),
                                        nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id',
                                                    ondelete="cascade"),
                                         nullable=False)
    mileage: Mapped[int] = mapped_column(nullable=True)
    total_price: Mapped[float] = mapped_column(nullable=False)
    liters: Mapped[float] = mapped_column(nullable=True)
    price_per_liter: Mapped[float] = mapped_column(nullable=True)
    fuel_type: Mapped[FuelTypeEnum] = mapped_column(
        Enum(FuelTypeEnum,
             values_callable=lambda x: [x.value for x in FuelTypeEnum]),
        nullable=True
    )
    gas_station: Mapped[GasStationTypeEnum] = mapped_column(
        Enum(GasStationTypeEnum,
             values_callable=lambda x: [x.value for x in GasStationTypeEnum]),
        default=GasStationTypeEnum.OTHER
    )
    time: Mapped[float] = mapped_column(nullable=True)
    full_tank: Mapped[bool] = mapped_column(nullable=True)
    comment: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 server_default=func.now(),
                                                 nullable=False)

    car = relationship("Car", back_populates="refuel_record")
    user = relationship("User", back_populates="refuel_records")
