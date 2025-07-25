import uuid
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
    cpf: Mapped[str] = Column(String(11), unique=True)
    age: Mapped[int] = Column(types.Integer)
    address: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    is_active: Mapped[bool] = Column(types.Boolean, default=True)
    created_at: Mapped[DateTime] = Column(DateTime, default=text("now()"))
    updated_at: Mapped[DateTime] = Column(DateTime, default=text("now()"), onupdate=text("now()"))
