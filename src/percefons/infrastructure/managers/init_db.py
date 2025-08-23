import logging

from percefons.domain.entities import Permission
from percefons.infrastructure.db.session import LocalSession
from percefons.infrastructure.repositories import permission_repository as pr

LOGGER = logging.getLogger(__name__)


def main():
    """Main function will be run to initialize the database."""
    session = LocalSession()
    try:
        permissions = [
            Permission("Can view user", "VIEW_USER"),
            Permission("Can create user", "CREATE_USER"),
            Permission("Can change user", "CHANGE_USER"),
            Permission("Can delete user", "DELETE_USER"),
        ]

        permission_repos = pr.PermissionRepositoryImpl(session)

        permissions_created = permission_repos.create_all(permissions)
        for perm in permissions_created:
            LOGGER.info("Permission created: " + str(perm))

    finally:
        session.close()
