from datetime import datetime
from dataclasses import dataclass
# from pydantic import BaseModel, EmailStr, Field


# class UserRegistrationRequest(BaseModel):
#     username: str = Field(..., example="alice")  # noqa
#     password: str = Field(..., min_length=8, example="StrongPassw0rd!")  # noqa
#     email: EmailStr = Field(..., example="alice@email.com")  # noqa

@dataclass
class UserRegistrationRequest:
    username: str
    password: str
    email: str



# class UserRegistrationResponse(BaseModel):
@dataclass
class UserRegistrationResponse:
    userid: int
    username: str
    created_at: datetime
