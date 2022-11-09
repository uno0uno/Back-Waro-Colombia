# The function of this file is to check whether the request is
# authorized or not [verification of the of the protected route]

#FastAPI
from fastapi import Request, HTTPException

#FastAPI Security HTTP BEARER
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

#Function to validate id token expires yet
from app.auth.jwt_handler import decodeJWT

class JWTBearer(HTTPBearer):
    
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(403,"Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(403,"Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(403,"Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid
