from datetime import datetime

from sqlalchemy import ForeignKey, DateTime, func, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Purchase(Base):
    __tablename__ = 'purchases'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id',
                                                    ondelete="CASCADE"))
    car_id: Mapped[int] = mapped_column(ForeignKey('cars.id',
                                                   ondelete="CASCADE"),
                                        nullable=True)

    title: Mapped[str] = mapped_column(nullable=True)
    total_price: Mapped[float] = mapped_column(Numeric(20, 2),
                                               nullable=True)
    quantity: Mapped[int] = mapped_column(nullable=True)
    price_per_unit: Mapped[float] = mapped_column(Numeric(20, 2),
                                                  nullable=True)
    purchase_date: Mapped[datetime] = mapped_column(DateTime,
                                                    nullable=True)
    comment: Mapped[str] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime,
                                                 server_default=func.now(),
                                                 nullable=False)

    user = relationship('User', back_populates='purchases')