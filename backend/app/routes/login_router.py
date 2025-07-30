from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from jwt import jwt

from backend.app.config.security_config import create_access_token, authenticate_user, create_refresh_token, \
    decode_token
from backend.app.services.user_service import UserService

router = APIRouter()


@router.post("/token")
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: UserService = Depends()
):
    user = await authenticate_user(form_data.username, form_data.password, service)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    sub = {"sub": user.email, "id": str(user.id), "cpf": user.cpf}
    token = create_access_token(sub)
    refresh_token = create_refresh_token(sub)
    return {'access_token': token, 'refresh_token': refresh_token, 'token_type': 'bearer'}

async def refresh(
        refresh_token: str,
        service: UserService = Depends()
):
    try:
        payload = decode_token(refresh_token)
        username = payload.get("sub")
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = await service.find_by_username(username["username"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    sub = {"sub": user.email, "id": str(user.id), "cpf": user.cpf}
    return {'access_token': create_access_token(sub), refresh_token: '', 'token_type': 'bearer'}
