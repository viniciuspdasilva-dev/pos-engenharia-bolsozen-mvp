from passlib.context import CryptContext


"""
    Classe responsavel por realizar a criptografia e descriptografia da 
    senha do usuario
"""
class HashPassword:
    _pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    @classmethod
    def crypt(cls, password: str) -> str:
        return cls._pwd_context.encrypt(password)

    @classmethod
    def hash(cls, password: str) -> str:
        return cls._pwd_context.hash(password)

    @classmethod
    def verify(cls, password: str, hashed_password: str) -> bool:
        return cls._pwd_context.verify(password, hashed_password)