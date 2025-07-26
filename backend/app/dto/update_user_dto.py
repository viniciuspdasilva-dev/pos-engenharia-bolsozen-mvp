class UpdateUserDTO:
    def __init__(self, **kwargs):
        self._id = kwargs["id"]
        self._name = kwargs["name"]
        self._email = kwargs["email"]
        self._cpf = kwargs["cpf"]
        self._password = kwargs["password"]
