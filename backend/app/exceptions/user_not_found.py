import uuid


class UserNotFound(Exception):
    def  __init__(self, identifier: str | uuid.UUID | None = None):
        super().__init__(f"User {identifier} not found")