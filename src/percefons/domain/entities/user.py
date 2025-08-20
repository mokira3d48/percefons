from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    username: str
    hashed_password: str
    created_at: datetime
    email: str = None
    is_active: bool = False
    is_staff: bool = False
    is_superuser: bool = False
    id: int = None

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False
