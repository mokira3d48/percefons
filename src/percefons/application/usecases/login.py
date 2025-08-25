from typing import Literal
from dataclasses import dataclass

from percefons.domain.exceptions import AuthenticationError
from percefons.domain.repositories import UserRepository
from percefons.application.services import JWTAuth, PasswordHandler


class Login:
    @dataclass
    class Result:
        status: Literal['F', 'S']
        tokens: dict = None

    def __init__(
        self,
        user_repository: UserRepository,
        password_handler: PasswordHandler,
        jwt_service: JWTAuth
    ):
        self.user_repository = user_repository
        self.ph = password_handler
        self.jwt_service = jwt_service

    def execute(self, username: str, password: str) -> Result:
        user = self.user_repository.get_by_username(username)
        if not user:
            raise AuthenticationError("Username/password is incorrect.")
        pw_verif = self.ph.verify_password(password, user.hashed_password)
        if not pw_verif:
            raise AuthenticationError("Username/password is incorrect.")

        tokens = self.jwt_service.get_access_token(str(user.id))
        return self.Result(status='S', token=tokens)


class LoginCommand:
    def __init__(self, ops: Login):
        self.operation = ops
        self.username = None
        self.password = None

    def validate(self):
        ...

    def execute(self) -> Login.Result:
        result = self.operation.execute(self.username, self.password)
        return result
