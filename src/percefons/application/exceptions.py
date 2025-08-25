
class UserIsAlreadyExists(Exception):
    default_message = "This user account is already exists."
    default_code = "user_exists"

    def __init__(self, message: str=None, code: str=None):
        self.message = message if message is not None else self.default_message
        self.code = code if code is not None else self.default_code


class InvalidCommandError(AssertionError):
    default_message = "This command is not valid."
    default_code = "invalid_command"

    def __init__(self, message: str=None, code: str=None, field: str=None):
        self.message = message if message is not None else self.default_message
        self.code = code if code is not None else self.default_code
        self.field = field



class AuthenticationError(RuntimeError):
    default_message: str = "Authentication failed."

    def __init__(self, message: str = None):
        self.message = message if message else self.default_message
