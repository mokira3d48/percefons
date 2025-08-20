from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    username: str
    hashed_password: str
    email: str
    created_at: datetime
    is_active: bool = False
    is_staff: bool = False
    is_superuser: bool = False
    id: int = None
