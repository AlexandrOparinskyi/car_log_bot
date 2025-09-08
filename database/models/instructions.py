from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Instruction(Base):
    __tablename__ = 'instructions'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    text: Mapped[str] = mapped_column(Text)

    def __repr__(self):
        return f"Инструкция {self.title}"
