from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

# from sqlalchemy.dialects.postgresql import JSONB
# from sqlalchemy.orm import relationship

from percefons.infrastructure.db.models.base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
