import typing as t

from sqlalchemy.orm import Session
from percefons.domain.entities.user import Permission, User
from percefons.domain.repositories import UserPermissionRepository


class UserPermissionRepositoryImpl(UserPermissionRepository):
    def __init__(self, db: Session):
        self.db = db

    def grant(self, permission: Permission, user: User) -> User:
        ...

    def revoke(self, permission: Permission, user: User) -> User:
        ...
