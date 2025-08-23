import logging

from sqlalchemy.orm import Session
from percefons.domain.entities.user import Permission, User
from percefons.domain.repositories import UserPermissionRepository
from percefons.infrastructure.db.models.user import UserModel
from percefons.infrastructure.db.models.permission import PermissionModel
from .user_repository import UserRepositoryImpl as Ur
from .permission_repository import PermissionRepositoryImpl as Pr

LOGGER = logging.getLogger(__name__)


class UserPermissionRepositoryImpl(UserPermissionRepository):
    def __init__(self, db: Session):
        self.db = db
        self.to_permission_model = Pr.convert_to_permission_model
        self.to_user_model = Ur.convert_to_user_model
        self.to_user_entity = Ur.convert_to_user_entity
        self.user_repos = Ur(self.db)
        self.perm_repos = Pr(self.db)

    def grant(self, permission: Permission, user: User) -> User:
        # perm_model = self.to_permission_model(permission)
        # user_model = self.to_user_model(user)
        perm_model = self.db.query(PermissionModel).get(permission.id)
        user_model = self.db.query(UserModel).get(user.id)

        if not perm_model:
            perm_model = self.to_permission_model(permission)
            self.db.add(perm_model)
            self.db.commit()
        if not user_model:
            user_model = self.to_user_model(user)
            self.db.add(user_model)
            self.db.commit()

        user_model.permissions.extend([perm_model])
        self.db.commit()

        user = self.to_user_entity(user_model)
        return user

    def revoke(self, permission: Permission, user: User) -> User:
        perm_model = self.db.query(PermissionModel).get(permission.id)
        user_model = self.db.query(UserModel).get(user.id)

        if not perm_model:
            LOGGER.warning(
                "No permission named: " + permission.name + " found."
            )
            return user
        if not user_model:
            LOGGER.warning(
                "No user named: " + user.username + " found."
            )
            return user

        user_model.permissions.remove(perm_model)
        self.db.commit()

        user = self.to_user_entity(user_model)
        return user
