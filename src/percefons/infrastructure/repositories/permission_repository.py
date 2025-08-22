import typing as t

from sqlalchemy.orm import Session
from percefons.domain.entities.user import Permission
from percefons.domain.repositories import PermissionRepository
from percefons.infrastructure.db.models.permission import PermissionModel


class PermissionRepositoryImpl(PermissionRepository):
    def __init__(self, db: Session):
        self.db = db

    @staticmethod
    def convert_to_permission_model(permission: Permission) -> PermissionModel:
        """
        This function allows to convert a user entity into permission model
        for SQL alchemy.

        :param permission: The instance of the permission entity.
        :returns: An instance of permission model.
        """
        perm_model_instance = PermissionModel(
            id=permission.id,
            name=permission.name,
            code_name=permission.code_name,
        )
        return perm_model_instance

    @staticmethod
    def convert_to_permission_entity(
        permission: PermissionModel
    ) -> Permission:
        """
        This function allows to convert a user model into permission entity.

        :param permission: The instance of the permission model.
        :returns: An instance of permission entity.
        """
        user_instance = Permission(
            id=permission.id,
            name=permission.name,
            code_name=permission.code_name,
        )
        return user_instance

    def get_by_code_name(self, code_name: str) -> t.Optional[Permission]:
        permission_query = self.db.query(PermissionModel)
        perms = permission_query.filter(PermissionModel.code_name == code_name)
        first_permission = perms.first()
        if not first_permission:
            return None
        user_ent = self.convert_to_permission_entity(first_permission)
        return user_ent

    def create(self, permission: Permission) -> Permission:
        perm_model_instance = self.convert_to_permission_model(permission)
        self.db.add(perm_model_instance)
        self.db.commit()
        self.db.refresh(perm_model_instance)
        permission.id = perm_model_instance.id
        return permission

    def all(self) -> t.Generator[Permission] | None:
        permission_query = (self.db.query(PermissionModel)
            .order_by(PermissionModel.name))
        permissions = permission_query.all()
        if not permissions:
            return None
        return (self.convert_to_permission_entity(perm)
                for perm in permissions)
