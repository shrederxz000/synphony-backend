from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from .base import Base


class Product(Base):
    name: Mapped[str] = mapped_column(String(100))
    description:Mapped[str | None] = mapped_column(String(10000))
    price: Mapped[int] = mapped_column(Integer)

