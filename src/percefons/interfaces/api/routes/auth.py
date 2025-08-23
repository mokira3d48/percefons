import logging

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from percefons.domain import validators
from percefons.infrastructure.repositories import user_repository
from percefons.infrastructure.services import password_handler
from percefons.infrastructure.db.session import get_db
from percefons.interfaces.api.schemas import (
    UserRegistrationRequest, UserRegistrationResponse)

from percefons.interfaces.api.utils import get_current_user_id
from percefons.application.usecases import user_registration

LOGGER = logging.getLogger(__name__)
# _db_connection = Depends(get_db)
# _user_repository = user_repository.UserRepositoryImpl(_db_connection)
_password_handler = password_handler.PasswordHandlerImpl()

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    path="/register",
    response_model=UserRegistrationResponse,
    summary="Register a new user into the database."
)
def register(
    payload: UserRegistrationRequest,
    #_user_id: int = Depends(get_current_user_id)
    db: Session = Depends(get_db)
):
    # Value object validations:
    validators.validate_username(payload.username)
    validators.validate_user_password(payload.password)
    validators.validate_email(str(payload.email))

    # Command creation:
    _user_repository = user_repository.UserRepositoryImpl(db)
    operation = user_registration.UserRegistration(
        user_repository=_user_repository,
        password_handler=_password_handler
    )
    cmd = user_registration.UserRegistrationCommand(operation)
    cmd.username = payload.username
    cmd.password = payload.password
    cmd.email = payload.email

    cmd.validate()
    result = cmd.execute()

    response = UserRegistrationResponse(
        username=result.username,
        userid=result.userid,
        created_at=result.created_at,
    )
    return response
