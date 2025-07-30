import logging
import os
from datetime import timedelta, datetime
from typing import Optional

from fastapi import HTTPException, status, Depends
from jose import JWTError, jwt

from backend.app.model.roles import Roles

from fastapi.security import OAuth2PasswordBearer

from backend.app.schemas.user_schema import UserLoginSchema
from backend.app.services.user_service import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/oauth/token")

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES: float = float(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

async def authenticate_user(username: str, password: str, user_service: UserService):
    db_user: UserLoginSchema = await user_service.find_by_username(username)
    if not db_user or not user_service.verify_password(password, db_user.hash_password):
        raise credentials_exception
    return db_user


def create_access_token(data: dict, roles=None, expires_delta: timedelta = None) -> str:
    if roles is None:
        roles = []
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    to_encode.update({"iat": datetime.utcnow()})
    to_encode.update({"roles": roles})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict, roles=None, expires_delta: timedelta = None) -> str:
    if roles is None:
        roles = []
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": expire})
    to_encode.update({"iat": datetime.utcnow()})
    to_encode.update({"roles": roles})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload =  verify_token(token)
    if not payload:
        raise credentials_exception
    return payload

def decode_token(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)