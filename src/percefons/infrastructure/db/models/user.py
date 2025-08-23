from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

# from sqlalchemy.dialects.postgresql import JSONB

from .base import BaseModel
from .user_perms import user_permission_association


class UserModel(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True, index=True)
    is_active = Column(Boolean, default=False)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    permissions = relationship(
        argument="PermissionModel",
        secondary=user_permission_association,
        back_populates="users")
