import uuid
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from backend.app.dto.create_user_dto import CreateUserDTO
from backend.app.exceptions.user_not_found import UserNotFound
from backend.app.model.user import User


def create_user(user_dto: CreateUserDTO):
    user: User = User()
    user.email = user_dto.email.lower()
    user.cpf = user_dto.cpf.lower()
    user.name = user_dto.name.lower()
    user.cpf = user_dto.cpf
    user.hash_password = user_dto.password_hash
    return user


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> List[User]:
        result = await self.db.execute(select(User))
        return result.scalars().all()

    async def get_user_by_id(self, user_id: uuid.UUID) -> User:
        result = await self.db.execute(
            select(User).where(User.pk == user_id)
        )
        return result.scalar_one_or_none()

    async def get_user_by_cpf(self, cpf: str) -> User:
        result = await self.db.execute(
            select(User).where(User.cpf == cpf)
        )
        return result.scalar_one_or_none()

    async def get_user_by_email(self, email: str) -> User:
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def create(self, user: CreateUserDTO) -> User:
        user = create_user(user)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def update(self, user: CreateUserDTO) -> User:
        user = create_user(user)
        self.db.merge(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def delete(self, user_id: uuid.UUID) -> None:
        user = await self.get_user_by_id(user_id)
        if user:
            await self.db.delete(user_id)
            await self.db.commit()
        else:
            await self.db.rollback()
            raise UserNotFound(user_id)