from dataclasses import dataclass


@dataclass
class LoginRequest:
    username: str = "alice"
    password: str = "aX6/9p6XoY]o4$#"


@dataclass
class LoginResponse:
    access_token: str
    refresh_token: str
