from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import BaseModel

user_permission_association = Table(
    'student_courses',
    BaseModel.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('perm_id', Integer, ForeignKey('permissions.id'), primary_key=True)
)
