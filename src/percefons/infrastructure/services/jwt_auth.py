from datetime import datetime, timedelta
from typing import Optional
from percefons.application.services import JWTAuth

import jwt
from fastapi import HTTPException, status
from app.config import get_settings

settings = get_settings()

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

    def decode(self, token: str) -> dict:
        try:
            return jwt.decode(token, self.secret, algorithms=[self.algorithm])
        except jwt.PyJWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")