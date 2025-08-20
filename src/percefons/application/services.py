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


class Authentication(ABC):
    ...
