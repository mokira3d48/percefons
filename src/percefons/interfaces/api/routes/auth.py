import logging

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from percefons.domain import validators
from percefons.infrastructure.repositories import user_repository
from percefons.infrastructure.services import password_handler, jwt_auth
from percefons.infrastructure.db.session import get_db
from percefons.interfaces.api.schemas import (
    UserRegistrationRequest, UserRegistrationResponse,
    LoginRequest, LoginResponse)

from percefons.interfaces.api.utils import get_current_user_id
from percefons.application.usecases import user_registration
from percefons.application.usecases import login

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
    user_repository_impl = user_repository.UserRepositoryImpl(db)
    operation = user_registration.UserRegistration(
        user_repository=user_repository_impl,
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


@router.post(
    path="/login",
    response_model=LoginResponse,
    summary="Login the user using its username and password."
)
def login_fn(payload: LoginRequest, db: Session = Depends(get_db)):
    user_repository_impl = user_repository.UserRepositoryImpl(db)
    auth = jwt_auth.JWTAuthImpl()
    operation = login.Login(
        user_repository=user_repository_impl,
        password_handler=_password_handler, jwt_service=auth,
    )
    cmd = login.LoginCommand(operation)
    cmd.username = payload.username
    cmd.password = payload.password

    cmd.validate()
    result = cmd.execute()

    response = LoginResponse(
        access_token=result.tokens['access_token'],
        refresh_token=result.tokens['refresh_token'],
    )
    return response
