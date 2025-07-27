import uuid

from sqlalchemy import String, types, text
from sqlalchemy.orm import Mapped, mapped_column

from . import Base


class Address(Base):
    __tablename__ = "address"
    email: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    hash_password: Mapped[str] = mapped_column(String(50), nullable=False)

    def __repr__(self):
        return f"<Address(email={self.email})>"
    def __eq__(self, other) -> bool:
        return self.email == other.email
    def __hash__(self) -> int:
        return hash(self.email)
