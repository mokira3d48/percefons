import typing as t
from abc import ABC, abstractmethod
from .entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> t.Optional[User]:
        ...

    @abstractmethod
    def get_by_email(self, email: str) -> t.Optional[User]:
        ...

    @abstractmethod
    def create(self, user: User) -> User:
        ...
