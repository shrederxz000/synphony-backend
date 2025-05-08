from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from .base import Base


class Product(Base):
    
    name: Mapped[str] = mapped_column()
    description:Mapped[str | None] = mapped_column()
    price: Mapped[int] = mapped_column()

