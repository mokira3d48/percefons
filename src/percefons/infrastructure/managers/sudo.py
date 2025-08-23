import logging
from getpass import getpass

from percefons.domain.entities import User
from percefons.domain import validators
from percefons.infrastructure.services import password_handler as ph
from percefons.infrastructure.db.session import LocalSession
from percefons.infrastructure.repositories import user_repository as ur

LOGGER = logging.getLogger(__name__)


def main():
    """Main function to create the new user as superuser."""
    session = LocalSession()
    password_handler = ph.PasswordHandlerImpl()
    user_repos = ur.UserRepositoryImpl(session)
    try:
        username = input("Username: ")
        email = input("Email: ")
        password = getpass()

        # Value object validations:
        validators.validate_username(username)
        validators.validate_user_password(password)
        if email:
            validators.validate_email(email)

        # Command validation:
        if not username:
            raise ValueError("The username is required.")
        if not password:
            raise ValueError("The password is required.")

        # Creation of the user instance:
        hashed_password = password_handler.get_password_hash(password)
        user_inst = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            is_active=True,
            is_staff=True,
            is_superuser=True)

        # Add user instance into database:
        user_created = user_repos.create(user_inst)
        LOGGER.info("User info: " + str(user_created))
        LOGGER.info("User created successfully!")

    except Exception as e:
        LOGGER.error("Error: " + str(e))

    finally:
        session.close()
        LOGGER.info("Database local session is closed.")
