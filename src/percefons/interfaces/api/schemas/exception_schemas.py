import typing as t
from dataclasses import dataclass
from fastapi.responses import JSONResponse


@dataclass
class UserIsAlreadyExistsResponse:
    message: str = "The user you want to register is already exists."
    code: str = "already_exist"


@dataclass
class InvalidFieldResponse:
    message: str = "The value of this field is not valid."
    code: str = "invalid_value"
    field: str = 'field_name'


class InvalidUserPasswordResponse(InvalidFieldResponse):
    ...


@dataclass
class AuthenticationFailureResponse:
    message: str = "Authentication failed."


Response = t.Union[UserIsAlreadyExistsResponse]
RESPONSE_CLASSES = {
    'UserIsAlreadyExists': (UserIsAlreadyExistsResponse, 403),
    'InvalidUserPasswordError': (InvalidUserPasswordResponse, 400),
    'AuthenticationError': (AuthenticationFailureResponse, 401),
}


def _make_response(exc: Exception) -> t.Optional[JSONResponse]:
    """
    This function allow to make response if the exc is instance
    of exception_class.
    """
    exception_class = exc.__class__
    exception_class_name = exception_class.__name__
    if exception_class_name not in RESPONSE_CLASSES:
        return None

    response_cls, code = RESPONSE_CLASSES[exception_class_name]
    response = response_cls()

    for attr_name in response.__dict__:
        if attr_name in exc.__dict__:
            value = exc.__dict__[attr_name]
            response.__dict__[attr_name] = value

    return JSONResponse(content=response.__dict__, status_code=code)


def exception_handler(exc: Exception) -> t.Optional[Response]:
    """This function allows to handle the internal exceptions."""
    return _make_response(exc)
