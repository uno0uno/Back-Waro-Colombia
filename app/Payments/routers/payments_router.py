#FastAPI
from fastapi import APIRouter, UploadFile, status, HTTPException,Request
from fastapi import Query, Path, Depends
from pydantic import Field

#Models app Waro Colombia(Internal)
from app.models.models import ModelAd
from app.models.models import Payments

#Function to validate id token expires yet
from app.auth.jwt_bearer import JWTBearer

# Request Merlina payment
from app.Payments.routers.payments_config import preference_data_merlina


# ============================================================
# Definitions Router:

payment_router_app = APIRouter(
    prefix="/payments"  
)

# ============================================================
# Path operations Payments
# ============================================================

# Post a product 
# ===============
@payment_router_app.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
    tags=["payments membresy"],
    summary="Request new payment"  
    ) 
def payment_preference(payments:Payments):
    response = preference_data_merlina(payments)
    if response:
        return response
    raise HTTPException(404,"Not found")
