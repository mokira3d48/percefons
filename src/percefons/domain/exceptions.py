class InvalidFieldError(ValueError):
    def __init__(self, message: str, code: str, field: str):
        super().__init__()
        self.message = message
        self.code = code
        self.field = field


class InvalidEmailError(InvalidFieldError):
    ...


class InvalidUsernameError(InvalidFieldError):
    ...


class InvalidNameError(InvalidFieldError):
    ...


class InvalidUserPasswordError(InvalidFieldError):
    ...


class AuthenticationError(RuntimeError):
    ...


class UserNotFoundError(AuthenticationError):
    ...
