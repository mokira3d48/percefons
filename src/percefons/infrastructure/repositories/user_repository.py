from sqlalchemy.orm import Session
from percefons.domain.entities.user import User
from percefons.infrastructure.db.models.user import UserModel


class SQLUserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_username(self, username: str):
        users = self.db.query(UserModel).filter(UserModel.username == username)
        first_user = users.first()
        return first_user

    def get_by_email(self, email: str):
        users = self.db.query(UserModel).filter(UserModel.email == email)
        first_user = users.first()
        return first_user

    def create(self, username: str, email: str, hashed_password: str):
        user = UserModel(
            username=username,
            email=email,
            hashed_password=hashed_password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
