#FastAPI
from fastapi import APIRouter, status, HTTPException
from fastapi import Query, Path, Depends

#DataBase encoders
from app.config.db import create_new_owner

#Models app Waro Colombia(Internal)
from app.models.models import NewOwner


#creation token JWT
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

#FastAPI Security HTTP BEARER
from fastapi.security import HTTPBearer

# ============================================================
# Definitions Router:

owner_router_app = APIRouter( prefix="/owner",tags=["Owner's managment"] )
token_auth_scheme = HTTPBearer()

# ========================================
# Path operations, New owner - information
# ========================================

# New owner
# ===================
@owner_router_app.post( "/", status_code=status.HTTP_201_CREATED, summary="New Owner" )
def new_product(new_owner:NewOwner):
    response = create_new_owner(new_owner.dict())
    if response:
        return response
    raise HTTPException(404,"Not found")







