import logging
import uuid
from typing import List, Union

from fastapi import APIRouter, Depends, HTTPException

from backend.app.config.security_config import get_current_user
from backend.app.schemas.user_schema import UserCreateSchema, UserReadSchema, MensagemResponse
from backend.app.services.user_service import UserService

router = APIRouter()


@router.post("/create", response_model=MensagemResponse)
async def register(
        user: UserCreateSchema,
        service: UserService = Depends()
) -> MensagemResponse:
    try:
        await service.create_user(user)
        return MensagemResponse(
            message="Usuario criado com sucesso.",
            success=True,
            status_code=201
        )
    except Exception as e:
        logging.error(e)
        return MensagemResponse(
            message="Ocorreu um erro ao cadastrar o cliente: " + str(e),
            success=False,
            status_code=500
        )

@router.put("/update/{id}", response_model=MensagemResponse)
async def update(
        id_user: uuid.UUID,
        user: UserCreateSchema,
        _: str = Depends(get_current_user),
        service: UserService = Depends()
):
    try:
        await service.update_user(id_user, user)
        return MensagemResponse(
            message="Usuario atualizado com sucesso.",
            success=True,
            status_code=200
        )
    except Exception as e:
        logging.error(e)
        return MensagemResponse(
            message="Ocorreu um erro ao atualizar o cliente: " + str(e),
            success=False,
            status_code=500
        )


@router.get("/list/all", response_model=List[UserReadSchema])
async def find_all(
        service: UserService = Depends(),
        _: str = Depends(get_current_user)
) -> List[UserReadSchema]:
    return await service.find_all()


@router.get("/find/id/{id}", response_model=UserReadSchema)
async def read(
        id: uuid.UUID,
        service: UserService = Depends(),
        _: str = Depends(get_current_user)
) -> UserReadSchema:
    user = await service.find_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/find/cpf/{cpf}", response_model=UserReadSchema)
async def find_by_cpf(
        cpf: str,
        service: UserService = Depends(),
        _: str = Depends(get_current_user)
):
    user = await service.find_by_cpf(cpf)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/find/email/{email}", response_model=UserReadSchema)
async def find_by_email(
        email: str,
        service: UserService = Depends(),
        _: str = Depends(get_current_user)
):
    user = await service.find_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
