import uuid
from datetime import datetime
from typing import List

from sqlalchemy import String, types, text, DateTime
from sqlalchemy.orm import Mapped, relationship, mapped_column

from . import Address
from . import Base


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(50), index=True)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(types.Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(types.Boolean, default=False)
    address: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User(name={self.name}, cpf={self.cpf}, age={self.age})>"

    def __eq__(self, other) -> bool:
        return (
                self.id == other.id
                and self.name == other.name
                and self.cpf == other.cpf
        )

    def __hash__(self) -> int:
        return hash((self.id, self.name, self.cpf))
