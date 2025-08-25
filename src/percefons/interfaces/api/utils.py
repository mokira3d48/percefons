from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
from percefons.infrastructure.services.jwt_auth import JWTAuthImpl

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
_auth = JWTAuthImpl()


def get_current_user_id(token: str = Depends(oauth2_scheme)) -> int:
    """
    This function is used to retrieve the current user ID which is connected.
    """
    result = _auth.verify_access_token(token)

    if result.status != JWTAuthImpl.SUCCESS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=result.message
        )

    payload = result.payload
    sub = payload.get("sub")
    if not sub:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid payload subject."
        )
    return int(sub)
