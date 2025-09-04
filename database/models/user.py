from datetime import datetime
from typing import Optional, List

from sqlalchemy import BigInteger, DateTime, func, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[Optional[str]] = mapped_column(nullable=True,
                                                    unique=True)
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 server_default=func.now(),
                                                 nullable=False)
    is_banned: Mapped[bool] = mapped_column(Boolean,
                                            default=False,
                                            nullable=False)
    is_premium: Mapped[bool] = mapped_column(default=False)
    is_admin: Mapped[bool] = mapped_column(default=False)
    bonus_points: Mapped[int] = mapped_column(default=0)

    cars = relationship("Car", back_populates="user", lazy="selectin")
    refuel_records = relationship("RefuelRecord",
                                  back_populates="user",
                                  lazy="selectin")

    @property
    def active_cars(self):
        return [car for car in self.cars if not car.is_deleted and car.is_active]

    @property
    def count_car(self) :
        return [car for car in self.cars if not car.is_deleted]

    @property
    def get_selected_main_car(self):
        selected_cars = list(
            filter(lambda car: car.is_selected_main == True, self.cars))
        return selected_cars[0] if selected_cars else None

    @property
    def get_total_cost(self):
        return sum([r.total_price for r in self.refuel_records])
