from backend.app.config.HashPassword import HashPassword


class CreateUserDTO:
    def __init__(self, **kwargs):
        self._name = kwargs["name"]
        self._email = kwargs["email"]
        self._cpf = kwargs["cpf"]
        self._hash_password = HashPassword(kwargs["password"])
        self._password = self._hash_password.crypt_password()

    def get_name(self) -> str:
        return self._name
    def get_email(self) -> str:
        return self._email
    def get_password(self) -> str:
        return self._password
    def get_cpf(self) -> str:
        return self._cpf

    def __repr__(self) -> str:
        return f"CreateUserDTO(name={self.get_name()}, email={self.get_email()})"
