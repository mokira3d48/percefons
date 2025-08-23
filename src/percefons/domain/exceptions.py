class InvalidFieldError(ValueError):
    def __init__(self, message: str, code: str, field: str):
        super().__init__()
        self.message = message
        self.code = code
        self.field = field

    def __str__(self):
        return self.message


class InvalidEmailError(InvalidFieldError):
    ...


class InvalidUsernameError(InvalidFieldError):
    ...


class InvalidNameError(InvalidFieldError):
    ...


class InvalidUserPasswordError(InvalidFieldError):
    ...

class AuthenticationError(RuntimeError):
    default_message: str = "Authentication failed."

    def __init__(self, message: str = None):
        self.message = message if message else self.default_message
