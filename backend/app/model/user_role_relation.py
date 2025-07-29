from sqlalchemy import Table, Column, Integer, String, ForeignKey

from backend.app.database import Base

user_roles = Table(
    'user_roles',
    Base.metadata,
    Column("user_id", ForeignKey("users.pk"), primary_key=True),
    Column("role_id", ForeignKey("roles.pk"), primary_key=True),
)