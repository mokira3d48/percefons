"""
username: str
hashed_password: str
email: str
created_at: datetime
is_active: bool = False
is_staff: bool = False
is_superuser: bool = False
id: int = None
"""
import logging
from datetime import datetime
from dataclasses import dataclass

from percefons.domain.entities.user import User
from percefons.domain.repositories import UserRepository
from percefons.application.services import PasswordHandler
from percefons.application.exceptions import UserIsAlreadyExists

LOGGER = logging.getLogger(__name__)


class UserRegistration:
    @dataclass
    class Result:
        userid: int
        username: str
        created_at: datetime

    def __init__(
        self,
        user_repository: UserRepository,
        password_handler: PasswordHandler
    ):
        self.user_repository = user_repository
        self.password_handler = password_handler

    def execute(self, username: str, password: str, email: str = None):
        """
        :raises UserIsAlreadyExists: When the user with this username
          is already exists.
        """
        # Verify if the new user is already exists in database:
        existing_user = self.user_repository.get_by_username(username)
        if existing_user is not None:
            raise UserIsAlreadyExists()

        password_hashed = self.password_handler.get_password_hash(password)

        user_instance = User(
            username=username,
            hashed_password=password_hashed,
            email=email,
            created_at=datetime.now(),
        )
        user_instance.activate()
        user_instance = self.user_repository.create(user_instance)
        LOGGER.info("A new user account with " + username + " is created.")
        LOGGER.debug("User ID: " + str(user_instance.id))

        result = self.Result(
            userid=user_instance.id,
            username=username,
            created_at=user_instance.created_at
        )
        return result


class UserRegistrationCommand:
    def __init__(self, ops: UserRegistration):
        self.operation = ops
        self.username = None
        self.password = None
        self.email = None

    def validate(self):
        ...

    def execute(self) -> UserRegistration.Result:
        """
        :raises UserIsAlreadyExists: When the user with this username
          is already exists.
        """
        result = self.operation.execute(
            username=self.username,
            password=self.password,
            email=self.email
        )
        return result
