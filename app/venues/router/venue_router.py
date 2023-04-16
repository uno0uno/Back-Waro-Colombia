#FastAPI
from fastapi import APIRouter, status, HTTPException
from fastapi import Query, Path, Depends

#DataBase encoders
from app.config.db import create_new_venue

#Models app Waro Colombia(Internal)
from app.models.models import NewVenue


#creation token JWT
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

#FastAPI Security HTTP BEARER
from fastapi.security import HTTPBearer

# ============================================================
# Definitions Router:

venue_router_app = APIRouter( prefix="/venue",tags=["Venue's managment"] )
token_auth_scheme = HTTPBearer()

# =========================================
# Path operations, New Seller - information
# =========================================

# New Order
# ===================
@venue_router_app.post( "/", status_code=status.HTTP_201_CREATED, summary="New Owner" )
def new_venue(new_venue:NewVenue):
    response = create_new_venue(new_venue.dict())
    if response:
        return response
    raise HTTPException(404,"Not found")







