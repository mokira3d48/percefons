import typing as t
# from dataclasses import dataclass
from abc import ABC, abstractmethod


class PasswordHandler(ABC):
    @abstractmethod
    def get_password_hash(self, password: str) -> str:
        ...

    @abstractmethod
    def verify_password(
        self,
        plain_password: str,
        hashed_password: str
    ) -> bool:
        ...


class JWTAuth(ABC):
    SUCCESS: str = 'S'
    FAILED: str = 'F'
    EXPIRED: str = 'E'

    class Result:
        def __init__(
            self,
            status: t.Literal['S', 'F', 'E'],
            message: str = None,
            payload: dict = None
        ):
            self.status = status
            self.message = message
            self.payload = payload

    @abstractmethod
    def get_auth(self, subject: str) -> dict:
        ...

    @abstractmethod
    def refresh_auth(self, refresh_token: str) -> t.Optional[str]:
        ...

    @abstractmethod
    def verify_auth(self, token: str) -> Result:
        ...
