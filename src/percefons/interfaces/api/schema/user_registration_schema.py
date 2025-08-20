from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserRegistrationRequest(BaseModel):
    username: str = Field(..., example="alice")  # noqa
    password: str = Field(..., min_length=8, example="StrongPassw0rd!")  # noqa
    email: EmailStr = Field(..., example="alice@email.com")  # noqa


class UserRegistrationResponse(BaseModel):
    userid: int
    username: str
    created_at: datetime
