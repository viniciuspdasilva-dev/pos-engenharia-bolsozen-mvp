from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import Mapped

from backend.app.database import Base
from backend.app.model.entity_base import EntityModel


class LancamentoFinanceiro(Base, EntityModel):
    __tablename__ = "lancamento_financeiro"
    description: Mapped[str] = Column(String(255), nullable=False)
    value: Mapped[float] = Column(nullable=False)
    date: Mapped[DateTime] = Column(DateTime(timezone=True))