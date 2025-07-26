from sqlalchemy import DateTime
from sqlalchemy.orm import Session

from backend.app.model.address import Address
from backend.app.model.user import User
from backend.app.dto.create_user_dto import CreateUserDTO


def _create_address(user_dto: CreateUserDTO) -> Address:
    address: Address = Address()
    address.hash_password = user_dto.get_password()
    address.email = user_dto.get_email()
    return address


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(User).all()

    def get_by_id(self, id: str):
        return self.db.query(User).filter(User.id == id).first()

    def create(self, user_dto: CreateUserDTO):
        user: User = User()
        user.address = [_create_address(user_dto)]
        user.name = user_dto.get_name()
        user.cpf = user_dto.get_cpf()
        self.db.add(user)
        return user

    def update(self, id_user: str, user_dto: CreateUserDTO):
        user: User | None = self.db.query(User).filter(User.id == id_user).first()
        if not user:
            raise Exception("User not found : " + id_user)
        user.name = user_dto.get_name()
        user.cpf = user_dto.get_cpf()
        user.address = [_create_address(user_dto)]
        return user

