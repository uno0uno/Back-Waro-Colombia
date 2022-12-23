#FastAPI
from fastapi import APIRouter, status, HTTPException
from fastapi import Query, Path, Depends

#DataBase encoders
from app.config.db import new_order_bd
from app.config.db import get_all_order_db
from app.config.db import change_state_order_db


#Models app Waro Colombia(Internal)
from app.models.models import Payments

#creation token JWT
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

#FastAPI Security HTTP BEARER
from fastapi.security import HTTPBearer



# ============================================================
# Definitions Router:

payments_router_app = APIRouter(
    prefix="/order"  
)

token_auth_scheme = HTTPBearer()

# ============================================================
# Path operations, Payment - new and fetch
# ============================================================

# New Order
# ===================
@payments_router_app.post(
            "/",
            status_code=status.HTTP_201_CREATED,
            tags=["User order"],
            summary="New order"  
            )
def new_order(payments:Payments):
    response = new_order_bd(payments.dict())
    if response:
        return response
    raise HTTPException(404,"Not found")

# =========================
# Get all Orders
# =========================
@payments_router_app.get("/orders",
            status_code=status.HTTP_200_OK,
            dependencies=[Depends(JWTBearer())],
            tags=["User order"],
            summary="Get all orders"
            )
def get_all_order():
            response = get_all_order_db() 
            if response:
                return response
            raise HTTPException(404,"Not found")

@payments_router_app.post("/newstate/{id}",
            status_code=status.HTTP_200_OK,
            dependencies=[Depends(JWTBearer())],
            tags=["User order"],
            summary="change order status"
            )
def change_state_order(
            id:str = Path(...,
            example="63543e411099e408d2c4e439", 
            description="Object _id order",
            min_length=1),
            state:str = Query(...,
            example="Confirmado",
            description="state's order")
            ):
            response = change_state_order_db(id, state) 
            if response:
                return response
            raise HTTPException(404,"Not found")


