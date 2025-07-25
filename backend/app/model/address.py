import uuid
from sqlalchemy import Column, String, types, text
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.config.database import Base


class Address(Base):
    __tablename__ = "address"
    id: Mapped[uuid.UUID] = mapped_column(
        types.UUID,
        primary_key=True,
        init=False,
        server_default=text("gen_random_uuid()")
    )
    email: Mapped[str] = Column(String(50), unique=True)
    password: Mapped[str] = Column(String(50), nullable=False)
