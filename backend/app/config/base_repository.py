import uuid
from collections.abc import Callable
from typing import TypeVar, Generic

from sqlalchemy import BinaryExpression, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.model import Base

Model = TypeVar("Model")



class BaseRepository(Generic[Model]):
    def __init__(self, model: type[Model], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def create(self, data: dict) -> Model:
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: uuid.UUID) -> Model | None:
        return await self.session.get(self.model, pk)

    async def filter(
            self,
            *expressions: BinaryExpression
    ) -> list[Model]:
        query = select(self.model)
        if expressions:
            query = query.where(*expressions)
        return list(await self.session.execute(query))
