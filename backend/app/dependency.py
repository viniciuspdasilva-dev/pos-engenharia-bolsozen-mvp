from typing import Callable

from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.config.base_repository import BaseRepository
from backend.app.model import Base


def get_repository(
        model: type[Base],
) -> Callable[[AsyncSession], BaseRepository[model]]:
    def func(session: AsyncSession) -> BaseRepository[model]:
        return BaseRepository(model, session)
    return func