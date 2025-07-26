from passlib.context import CryptContext


class HashPassword:

    def __init__(self, password):
        self.password = password
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def crypt_password(self) -> str:
        return self.pwd_context.hash(self.password)