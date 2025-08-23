import typing as t
from abc import ABC, abstractmethod
from .entities.user import User
from .entities.permission import Permission


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


class PermissionRepository(ABC):
    @abstractmethod
    def get_by_code_name(self, code_name: str) -> t.Optional[Permission]:
        ...

    @abstractmethod
    def create(self, permission: Permission) -> Permission:
        ...

    @abstractmethod
    def create_all(
        self,
        permissions: t.List[Permission]
    ) -> t.List[Permission] | None:
        ...

    @abstractmethod
    def all(self) -> t.Iterator[Permission] | None:
        ...


class UserPermissionRepository(ABC):
    @abstractmethod
    def grant(self, permission: Permission, user: User) -> User:
        ...

    @abstractmethod
    def revoke(self, permission: Permission, user: User) -> User:
        ...
