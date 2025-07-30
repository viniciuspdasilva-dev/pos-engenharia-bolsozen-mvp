
from sqlalchemy import String, types, Column, Table, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database import Base
from backend.app.model.entity_base import EntityModel


class User(Base, EntityModel):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(255), index=True)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=True)
    email: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    hash_password: Mapped[str] = mapped_column(String(150), nullable=False)
    is_active: Mapped[bool] = mapped_column(types.Boolean, default=True)
    is_superuser: Mapped[bool] = mapped_column(types.Boolean, default=False)
    roles: Mapped[list["Roles"]] = relationship(
        secondary="user_roles", back_populates="users"
    )

    def __repr__(self):
        return f"<User(name={self.name}, cpf={self.cpf}, email={self.email})>"

    def __eq__(self, other) -> bool:
        return (
                self.pk == other.pk
                and self.name == other.name
                and self.cpf == other.cpf
                and self.email == other.email
        )

    def __hash__(self) -> int:
        return hash((self.pk, self.name, self.cpf, self.email))
