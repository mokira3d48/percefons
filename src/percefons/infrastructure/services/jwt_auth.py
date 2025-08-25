import typing as t
from datetime import datetime, timedelta

import jwt
# from fastapi import HTTPException, status

from percefons.core import  settings
from percefons.application.services import JWTAuth


class JWTAuthImpl(JWTAuth):
    def __init__(
        self,
        access_secret_key: str = settings.JWT_ACCESS_SECRET,
        refresh_secret_key: str = settings.JWT_ACCESS_SECRET,
        algorithm: str = settings.JWT_ALG
    ):
        self.access_secret_key = access_secret_key
        self.refresh_secret_key = refresh_secret_key
        self.algorithm = algorithm
        self.access_token_delay = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.refresh_token_delay = settings.REFRESH_TOKEN_EXPIRE_MINUTES

    def verify_refresh_token(self, token: str) -> JWTAuth.Result:
        """
        Function to verify if the refresh token is valid or not.
        """
        try:
            payload = jwt.decode(
                jwt=token,
                key=self.refresh_secret_key,
                algorithms=[self.algorithm]
            )
            result = self.Result(
                status=JWTAuth.SUCCESS,  # noqa
                message="The refresh token is verified successfully.",
                payload=payload
            )
            return result

        except jwt.ExpiredSignatureError:
            result = self.Result(
                status=JWTAuth.EXPIRED,  # noqa
                message="The refresh token is expired."
            )
            return result

        except jwt.PyJWTError | jwt.InvalidTokenError as e:
            result = self.Result(
                status=JWTAuth.FAILED,  # noqa
                message=str(e),
            )
            return result

    def get_auth(self, subject: str) -> dict:
        """
        Build and returns the authentication data (access and refresh tokens).

        :param subject: Data formatted as string as subject.
        :returns: A dictionary that contents the access and refresh tokens.
        """

        current_dt = datetime.now()
        expiration =  current_dt + timedelta(minutes=self.access_token_delay)
        payload = {"sub": subject, "iat": current_dt, "exp": expiration}
        access_token = jwt.encode(
            payload=payload, key=self.access_secret_key,
            algorithm=self.algorithm
        )
        refresh_token = jwt.encode(
            payload=payload, key=self.refresh_secret_key,
            algorithm=self.algorithm
        )
        return {"access_token": access_token, "refresh_token": refresh_token}

    def refresh_auth(self, refresh_token: str) -> t.Optional[str]:
        """
        Build the access token from refresh token to reset authentication.
        """
        result = self.verify_refresh_token(refresh_token)
        if result.status != JWTAuth.SUCCESS:
            return None
        payload = result.payload
        access_token = jwt.encode(
            payload=payload, key=self.access_secret_key,
            algorithm=self.algorithm
        )
        return access_token

    def verify_auth(self, token: str) -> JWTAuth.Result:  # noqa
        """
        Function to verify access token for authentication.
        """
        try:
            payload = jwt.decode(
                jwt=token,
                key=self.access_secret_key,
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
