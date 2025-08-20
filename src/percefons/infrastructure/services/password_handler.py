from passlib.context import CryptContext
from percefons.application.services import PasswordHandler

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordHandlerImpl(PasswordHandler):
    def get_password_hash(self, password: str) -> str:
        result = pwd_context.hash(password)
        return result

    def verify_password(
        self,
        plain_password: str,
        hashed_password: str
    ) -> bool:
        is_verified = pwd_context.verify(plain_password, hashed_password)
        return is_verified
