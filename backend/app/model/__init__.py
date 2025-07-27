from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .address import Address
from .user import User