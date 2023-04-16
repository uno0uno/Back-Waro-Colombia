#FastAPI
from fastapi import APIRouter, status, HTTPException
from fastapi import Query, Path, Depends

#DataBase encoders
from app.config.db import create_new_product

#Models app Waro Colombia(Internal)
from app.models.models import NewProduct

#creation token JWT
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

#FastAPI Security HTTP BEARER
from fastapi.security import HTTPBearer

# ============================================================
# Definitions Router:

product_router_app = APIRouter( prefix="/product",tags=["Product's managment"] )
token_auth_scheme = HTTPBearer()

# ======================================
# Path operations, Product - New product 
# ======================================

# New product
# ===================
@product_router_app.post( "/", status_code=status.HTTP_201_CREATED, summary="New product" )
def new_product(new_product:NewProduct):
    response = create_new_product(new_product.dict())
    if response:
        return response
    raise HTTPException(404,"Not found")







