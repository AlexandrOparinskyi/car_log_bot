import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import func, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .user import User


class EngineTypeEnum(enum.Enum):
    PETROL = "Бензин"
    DIESEL = "Дизель"
    ELECTRO = "Электро"
    HYBRID = "Гибрид"
    GAS = "Газ"


class TransmissionTypeEnum(enum.Enum):
    AUTOMATIC = "Автоматическая"
    MANUAL = "Механическая"
    CVT = "Вариатор"
    ROBOTIC = "Робот"


class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    mark: Mapped[Optional[str]] = mapped_column(nullable=True)
    model: Mapped[Optional[str]] = mapped_column(nullable=True)
    year: Mapped[Optional[int]] = mapped_column(nullable=True)
    color: Mapped[Optional[str]] = mapped_column(nullable=True)
    engine_type: Mapped[
        Optional[EngineTypeEnum]
    ] = mapped_column(nullable=True)
    transmission_type: Mapped[
        Optional[TransmissionTypeEnum]
    ] = mapped_column(nullable=True)
    mileage: Mapped[Optional[int]] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 server_default=func.now(),
                                                 nullable=False)
    user_id: Mapped[User] = mapped_column(ForeignKey('users.id',
                                                     ondelete='CASCADE'))
    is_deleted: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    is_selected_main: Mapped[bool] = mapped_column(default=False)

    user = relationship("User", back_populates="cars")
    refuel_record = relationship("RefuelRecord",
                                 back_populates="car",
                                 lazy="selectin")
