import typing as t
from datetime import datetime, timedelta

import jwt
# from fastapi import HTTPException, status

from percefons.core import  settings
from percefons.application.services import JWTAuth


class JWTAuthImpl(JWTAuth):
    def __init__(
        self,
        secret_key: str = settings.JWT_SECRET,
        algorithm: str = settings.JWT_ALG
    ):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def get_access_token(
        self,
        subject: str,
        expires_minutes: int = settings.ACCESS_TOKEN_EXPIRE_MINUTES
    ) -> str:
        current_dt = datetime.now()
        expiration =  current_dt + timedelta(minutes=expires_minutes)
        payload = {"sub": subject,
                   "iat": current_dt,
                   "exp": expiration}
        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token

    def verify_access_token(self, token: str) -> JWTAuth.Result:  # noqa
        try:
            payload = jwt.decode(
                jwt=token,
                key=self.secret_key,
                algorithms=[self.algorithm]
            )
            result = self.Result(
                status=JWTAuth.SUCCESS,  # noqa
                message="The access token is verified successfully.",
                payload=payload
            )
            return result
        except jwt.ExpiredSignatureError:
            # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
            result = self.Result(
                status=JWTAuth.EXPIRED,  # noqa
                message="The access token is expired."
            )
            return result
        except jwt.PyJWTError | jwt.InvalidTokenError as e:
            result = self.Result(
                status=JWTAuth.FAILED,  # noqa
                message=str(e),
            )
            return result