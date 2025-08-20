
class UserIsAlreadyExists(Exception):
    default_message = "This user account is already exists."
    default_code = "user_exists"

    def __init__(self, message: str = None, code: str = None):
        self.message = message if message is not None else self.default_message
        self.code = code if code is not None else self.default_code
