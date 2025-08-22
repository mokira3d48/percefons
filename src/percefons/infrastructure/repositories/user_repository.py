import typing as t

from sqlalchemy.orm import Session
from percefons.domain.entities.user import User
from percefons.domain.repositories import UserRepository
from percefons.infrastructure.db.models.user import UserModel


class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def convert_to_user_model(user: User) -> UserModel:
        """
        This function allows to convert a user entity into user model
        for SQL alchemy.

        :param user: The instance of the user entity.
        :returns: An instance of user model.
        """
        user_model_instance = UserModel(
            id=user.id,
            username=user.username,
            email=user.email,
            hashed_password=user.hashed_password,
            is_active=user.is_active,
            is_staff=user.is_staff,
            is_superuser=user.is_superuser,
            created_at=user.created_at,
        )
        return user_model_instance

    @staticmethod
    def convert_to_user_entity(user: UserModel) -> User:
        """
        This function allows to convert a user model into user entity.

        :param user: The instance of the user model.
        :returns: An instance of user entity.
        """
        user_instance = User(
            id=user.id,
            username=user.username,
            email=user.email,
            hashed_password=user.hashed_password,
            is_active=user.is_active,
            is_staff=user.is_staff,
            is_superuser=user.is_superuser,
            created_at=user.created_at,
        )
        return user_instance

    def get_by_username(self, username: str) -> t.Optional[User]:
        users_query = self.db.query(UserModel)
        users = users_query.filter(UserModel.username == username)
        first_user = users.first()
        if not first_user:
            return None
        user_ent = self.convert_to_user_entity(first_user)
        return user_ent

    def get_by_email(self, email: str) -> t.Optional[User]:
        users_query = self.db.query(UserModel)
        users = users_query.filter(UserModel.email == email)
        first_user = users.first()
        if not first_user:
            return None
        user_ent = self.convert_to_user_entity(first_user)
        return user_ent

    def create(self, user: User) -> User:
        user_model_instance = self.convert_to_user_model(user)
        self.db.add(user_model_instance)
        self.db.commit()
        self.db.refresh(user_model_instance)
        user.id = user_model_instance.id
        return user
