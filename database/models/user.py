from datetime import datetime
from typing import Optional

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

    cars = relationship("Car", back_populates="user", lazy="selectin")

    @property
    def active_cars(self):
        return [car for car in self.cars if not car.is_deleted and car.is_active]

    @property
    def count_car(self):
        return [car for car in self.cars if not car.is_deleted]
