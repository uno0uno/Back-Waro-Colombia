#FastAPI
from fastapi import APIRouter, status, HTTPException
from fastapi import Query, Path, Depends

#DataBase encoders
from app.config.db import create_new_seller

#Models app Waro Colombia(Internal)
from app.models.models import NewSeller


#creation token JWT
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

#FastAPI Security HTTP BEARER
from fastapi.security import HTTPBearer

# ============================================================
# Definitions Router:

seller_router_app = APIRouter( prefix="/seller",tags=["Seller's managment"] )
token_auth_scheme = HTTPBearer()

# =========================================
# Path operations, New Seller - information
# =========================================

# New Order
# ===================
@seller_router_app.post( "/", status_code=status.HTTP_201_CREATED, summary="New Owner" )
def new_product(new_seller:NewSeller):
    response = create_new_seller(new_seller.dict())
    if response:
        return response
    raise HTTPException(404,"Not found")







