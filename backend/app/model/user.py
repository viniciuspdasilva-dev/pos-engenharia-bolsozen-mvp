import uuid
from datetime import datetime
from typing import List

from sqlalchemy import Column, String, types, text, DateTime
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.testing.schema import mapped_column

from backend.app.model.address import Address
from backend.app.model.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        types.UUID,
        primary_key=True,
        init=False,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str] = Column(String(50))
    cpf: Mapped[str] = Column(String(11), unique=True, nullable=True)
    age: Mapped[int] = Column(types.Integer)
    address: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    is_active: Mapped[bool] = Column(types.Boolean, default=True)
    created_at: Mapped[DateTime] = Column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[DateTime] = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User(name={self.name}, cpf={self.cpf}, age={self.age})>"

    def __eq__(self, other) -> bool:
        return (
                self.id == other.id
                and self.name == other.name
                and self.cpf == other.cpf
                and self.age == other.age
        )

    def __hash__(self) -> int:
        return hash((self.id, self.name, self.cpf, self.age))
