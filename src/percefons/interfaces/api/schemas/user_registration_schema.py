from datetime import datetime
from dataclasses import dataclass
# from pydantic import BaseModel, EmailStr, Field


# class UserRegistrationRequest(BaseModel):
#     username: str = Field(..., example="alice")  # noqa
#     password: str = Field(..., min_length=8, example="StrongPassw0rd!")  # noqa
#     email: EmailStr = Field(..., example="alice@email.com")  # noqa

@dataclass
class UserRegistrationRequest:
    username: str = "alice"
    password: str = "aX6/9p6XoY]o4$#"
    email: str = "alice@email.com"


# class UserRegistrationResponse(BaseModel):
@dataclass
class UserRegistrationResponse:
    userid: int = 12
    username: str = "alice"
    created_at: datetime = None
