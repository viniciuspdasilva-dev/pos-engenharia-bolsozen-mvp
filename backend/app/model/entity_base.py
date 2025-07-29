import uuid

from sqlalchemy import DateTime, Column, func, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column


class EntityModel:
    pk: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
    created_at: Mapped[DateTime] = Column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = Column(DateTime(timezone=True), onupdate=func.now())
    version: Mapped[int] = Column(Integer, default=0)