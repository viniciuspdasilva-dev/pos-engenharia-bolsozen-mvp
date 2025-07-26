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
    hash_password: Mapped[str] = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Address(email={self.email})>"
    def __eq__(self, other) -> bool:
        return self.email == other.email
    def __hash__(self) -> int:
        return hash(self.email)
