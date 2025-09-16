import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, Text, DateTime, func, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class ServiceTypeEnum(enum.Enum):
    REPLACEMENT = "Замена"
    MAINTENANCE = "ТО"
    DIAGNOSTICS = "Диагностика"
    REPAIR = "Ремонт"
    BODY_WORK = "Кузовные работы"
    OTHER = "Другое"


class ServiceRecord(Base):
    __tablename__ = "service_records"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id",
                                                    ondelete="cascade"),
                                         nullable=False)
    car_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("cars.id",
                   ondelete="cascade"),
        nullable=True
    )

    title: Mapped[Optional[str]] = mapped_column(nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    total_price: Mapped[float] = mapped_column(Numeric(20, 2),
                                               nullable=True)
    service_type: Mapped[ServiceTypeEnum] = mapped_column(
        Enum(ServiceTypeEnum)
    )

    service_center: Mapped[Optional[str]] = mapped_column(nullable=True)
    comment: Mapped[Optional[str]] = mapped_column(nullable=True)
    service_date: Mapped[datetime] = mapped_column(DateTime,
                                                   nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 server_default=func.now(),
                                                 nullable=False)

    user = relationship("User", back_populates="service_records")
    car = relationship("Car", back_populates="service_records")
    service_works = relationship("ServiceWork",
                                 back_populates="service_record")
    service_parts = relationship("ServicePart",
                                 back_populates="service_record")


class ServiceWork(Base):
    __tablename__ = "service_works"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_record_id: Mapped[int] = mapped_column(
        ForeignKey("service_records.id",
                   ondelete="cascade"),
        nullable=False
    )

    name: Mapped[Optional[str]] = mapped_column(nullable=True)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    price: Mapped[float] = mapped_column(Numeric(20, 2),
                                         nullable=True)

    service_record = relationship("ServiceRecord",
                                  back_populates="service_works")


class ServicePart(Base):
    __tablename__ = "service_parts"

    id: Mapped[int] = mapped_column(primary_key=True)
    service_record_id: Mapped[int] = mapped_column(
        ForeignKey("service_records.id",
                   ondelete="cascade"),
        nullable=False
    )

    name: Mapped[Optional[str]] = mapped_column(nullable=True)
    part_number: Mapped[Optional[str]] = mapped_column(nullable=True)
    quantity: Mapped[int] = mapped_column(default=1)
    price_per_unit: Mapped[Optional[float]] = mapped_column(Numeric(20, 2),
                                                            nullable=True)
    total_price: Mapped[float] = mapped_column(Numeric(20, 2),
                                               nullable=True)
    comment: Mapped[Optional[str]] = mapped_column(nullable=True)

    service_record = relationship("ServiceRecord",
                                  back_populates="service_parts")
