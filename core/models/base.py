from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr
from sqlalchemy import Integer

class Base(DeclarativeBase):
    __abstract__= True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"symphony_market_{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)


