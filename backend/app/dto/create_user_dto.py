from dataclasses import dataclass, field

from ..utils.password_utils import HashPassword


@dataclass
class CreateUserDTO:
    name: str
    cpf: str
    email: str
    password: str = field(repr=False)
    password_hash: str = field(init=False)

    def __post_init__(self):
        self.password_hash = HashPassword().hash(self.password)
