import logging
import uuid
from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import async_session

from backend.app.dto.create_user_dto import CreateUserDTO
from backend.app.repositories.user.user_repository import UserRepository
from backend.app.schemas.user_schema import UserCreateSchema, UserReadSchema
from backend.app.utils.password_utils import HashPassword


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    async def find_all(self) -> List[UserReadSchema]:
        users = await self.repository.get_all()
        if len(users) == 0:
            return []
        return [
            UserReadSchema.model_validate(u) for u in users
        ]

    async def find_by_id(self, id_user: uuid.UUID) -> UserReadSchema:
        user = await self.repository.get_user_by_id(id_user)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return UserReadSchema.model_validate(user)

    async def find_by_cpf(self, cpf: str) -> UserReadSchema:
        user = await self.repository.get_user_by_cpf(cpf)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return UserReadSchema.model_validate(user)

    async def find_by_email(self, email: str) -> UserReadSchema:
        user = await self.repository.get_user_by_email(email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return UserReadSchema.model_validate(user)

    async def create_user(self, user: UserCreateSchema) -> None:
        user_dto: CreateUserDTO = CreateUserDTO(
            name=user.name,
            cpf=user.cpf,
            email=user.email,
            password=user.password
        )
        logging.info(f"Usuario a ser criado: {user_dto}")
        await self.repository.create(user_dto)


    async def update_user(self, id_user: uuid.UUID, user_update: UserCreateSchema) -> UserReadSchema:
        user = await self.repository.get_user_by_id(id_user)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        user.name = user.name or user_update.name
        if user_update.password:
            user.hashed_password = (
                HashPassword.hash(user_update.password)
            )
        user_new = await self.repository.update(user)
        return UserReadSchema.model_validate(user_new)

    async def delete_user(self, id_user: uuid.UUID) -> None:
        user = await self.repository.get_user_by_id(id_user)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        await self.repository.delete(id_user)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return HashPassword.verify(plain_password, hashed_password)


# Injeção de dependencias
async def get_user_service(
        db: Depends(async_session)
) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)
