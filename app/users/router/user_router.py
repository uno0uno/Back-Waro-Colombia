#FastAPI
from fastapi import APIRouter, status, HTTPException
from fastapi import Query, Path, Depends

#DataBase encoders
from app.config.db import fetch_all_product_by_filter


#creation token JWT
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

#FastAPI Security HTTP BEARER
from fastapi.security import HTTPBearer

# ============================================================
# Definitions Router:

user_router_app = APIRouter( prefix="/user",tags=["Queries user"] )
token_auth_scheme = HTTPBearer()

# ===============================================
# Path operations, GEL ALL PRODUCTS - information
# ===============================================

# Get all products by 3 filters (Category,)
# ===================
@user_router_app.get("/filter/{name}",status_code=status.HTTP_200_OK,summary="All products by category")

def new_product(
    category:str = Query(example="dancehall", description="Name of category"),
    citie_product:str = Query(example="Bogotá", description="Name of city"),
    date_limit_product:str = Query(example="2021-04-31", description="Date product")
    ):
    response = fetch_all_product_by_filter(category,citie_product,date_limit_product)
    if response:
        return response
    raise HTTPException(404,"Not found")







