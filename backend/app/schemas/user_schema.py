import uuid

from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    name: str
    cpf: str
    email: str
    password: str

class UserReadSchema(BaseModel):
    id: uuid.UUID
    name: str
    cpf: str
    email: str
    class Config:
        orm_mode = True
        from_attributes = True

class MensagemResponse(BaseModel):
    message: str
    success: bool
    status_code: int