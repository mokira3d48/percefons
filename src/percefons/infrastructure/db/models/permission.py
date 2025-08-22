from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from .base import BaseModel
from .user_perms import user_permission_association


class PermissionModel(BaseModel):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    code_name = Column(String(60), unique=True, nullable=False, index=True)

    users = relationship(
        argument="UserModel",
        secondary=user_permission_association,
        back_populates="permissions",
    )
