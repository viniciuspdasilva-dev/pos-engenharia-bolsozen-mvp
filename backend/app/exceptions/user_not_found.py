class UserNotFound(Exception):
    def  __init__(self, message, id_user):
        pass

    def throws(self):
        raise self