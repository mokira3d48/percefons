import typing as t
from dataclasses import dataclass
from datetime import datetime
from .permission import Permission


@dataclass
class User:
    username: str
    hashed_password: str
    email: str = None
    created_at: datetime = None
    is_active: bool = False
    is_staff: bool = False
    is_superuser: bool = False
    id: int = None
    permissions: t.List[Permission] = None

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
