from sqlalchemy import Column, Text, Boolean
from sqlalchemy.orm import Mapped, relationship

from backend.app.database import Base
from backend.app.model.entity_base import EntityModel
from backend.app.model.user import User
from backend.app.model.user_role_relation import user_roles


class Roles(Base, EntityModel):
    __tablename__ = 'roles'
    name: Mapped[str] = Column(Text, nullable=False)
    is_actived: Mapped[bool] = Column(Boolean, nullable=False)
    users: Mapped[list["User"]] = relationship(
        secondary=user_roles, back_populates="roles"
    )