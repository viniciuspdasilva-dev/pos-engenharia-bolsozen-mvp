from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped

from backend.app.database import Base
from backend.app.model.entity_base import EntityModel


class Category(Base, EntityModel):
    __tablename__ = "category"
    name: Mapped[str] = Column(String(150), nullable=False)
    description: Mapped[str] = Column(String(255), nullable=False)
    is_actived: Mapped[bool] = Column(nullable=False)
    color: Mapped[str] = Column(String(10), nullable=False)
    priority: Mapped[int] = Column(nullable=False)
    is_principal: Mapped[bool] = Column(nullable=False)