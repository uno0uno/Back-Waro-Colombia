#FastAPI
from fastapi import APIRouter, status, HTTPException
from fastapi import Query, Path, Depends

#DataBase encoders
from app.config.db import check_parther
from app.config.db import create_parthner
from app.config.db import update_parthner
from app.config.db import get_parthner_info_bd
from app.config.db import fetch_all_garage_parthner
from app.config.db import fetch_all_payments

#Models app Waro Colombia(Internal)
from app.models.models import ParthnerInfoUpdate
from app.models.models import ParthnerInfo
from app.models.models import ParthnerLogin

#creation token JWT
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

#FastAPI Security HTTP BEARER
from fastapi.security import HTTPBearer



# ============================================================
# Definitions Router:

parthner_router_app = APIRouter(
    prefix="/parthner"  
)

token_auth_scheme = HTTPBearer()

# ============================================================
# Path operations, Parthner - information Bussines
# ============================================================

# Login parthner - Login
# ==============
@parthner_router_app.post(
    "/login",
    status_code=status.HTTP_201_CREATED,
    tags=["Parthner bussines"],
    summary="Login Parthner"  
    )
def login_parthner(parthner_login:ParthnerLogin):
    response = check_parther(parthner_login.dict())
    if response:
        return signJWT(response["email"])
    raise HTTPException(401,"Unauthorized")

# Create new parthner - singup
# ============================
@parthner_router_app.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    tags=["Parthner bussines"],
    summary="Create new bussines"  
    ) 
def create_new_parthner(parthner_info:ParthnerInfo):
    response = create_parthner(parthner_info.dict()) 
    if response:
        return response
    raise HTTPException(409,"Already Exists")

# Update parthner
# ===================
@parthner_router_app.put(
            "/{id}",
            status_code=status.HTTP_201_CREATED,
            dependencies=[Depends(JWTBearer())],
            tags=["Parthner bussines"],
            summary="Update bussines"  
            )
def update_parthner_db(Parthner_info_update:ParthnerInfoUpdate,
            id:str = Path(...,
            example="63543e411099e408d2c4e439", 
            description="Object _id Pathner",
            min_length=1)
            ):
    response = update_parthner(Parthner_info_update.dict(),id)
    if response:
        return response
    raise HTTPException(404,"Not found")

# Get all garage Parthner
# =====================
@parthner_router_app.get("/garage/{email}",
            status_code=status.HTTP_200_OK,
            dependencies=[Depends(JWTBearer())],
            tags=["Parthner bussines"],
            summary="Get all garage by name_bussines"
            )
def get_garage_parthner(
            email:str = Path(...,
            example="hola@warocol.com",
            description="Email bussines")
            ):
            response = fetch_all_garage_parthner(email) 
            if response:
                return response
            raise HTTPException(404,"Not found")

# Get all payments
# =====================
@parthner_router_app.get("/payments/",
            status_code=status.HTTP_200_OK,
            dependencies=[Depends(JWTBearer())],
            tags=["Parthner bussines"],
            summary="Get payments"
            )
def get_garage_parthner():
            response = fetch_all_payments() 
            if response:
                return response
            raise HTTPException(404,"Not found")

# Get Parthner information
# =====================
@parthner_router_app.get("/info/{email}",
            status_code=status.HTTP_200_OK,
            dependencies=[Depends(JWTBearer())],
            tags=["Parthner bussines"],
            summary="Get parthner info"
            )
def get_parthner_info(
            email:str = Path(...,
            example="hola@warocol.com",
            description="Email bussines")
            ):
    response = get_parthner_info_bd(email) 
    if response:
        return response
    raise HTTPException(404,"Not found")


