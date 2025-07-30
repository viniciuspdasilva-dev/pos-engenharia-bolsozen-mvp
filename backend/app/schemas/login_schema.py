from pydantic import BaseModel


class LoginSchema(BaseModel):
    email: str
    password: str

class TokenOAuth(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
    token_type: str