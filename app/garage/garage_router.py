#FastAPI
from fastapi import APIRouter, status, HTTPException,Request
from fastapi import Query, Path, Depends
from pydantic import Field

#DataBase encoders
from app.config.db import create_garage_item_ad_category
from app.config.db import remove_garage_item

#Models app Waro Colombia(Internal)
from app.models.models import ModelGarage

#Function to validate id token expires yet
from app.auth.jwt_bearer import JWTBearer

# ============================================================
# Definitions Router:

garage_router_app = APIRouter(
    prefix="/garage"  
)

# ============================================================
# Path operations Products
# ============================================================

# Post a product 
# ===============
@garage_router_app.post(
    "/{id_parthner}",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
    tags=["Parthner garage"],
    summary="Post a garage item"  
    ) 
def post_item_garage(
                    model_garage:ModelGarage,
                    id_parthner:str = Path(...,example="63543c1f1099e408d2c4e435", description="Object _id Parthner")
                    ):
    response = create_garage_item_ad_category(model_garage.dict(),id_parthner) 
    if response:
        return response
    raise HTTPException(404,"Not found")
    
# Delete a product 
# ================
@garage_router_app.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
    tags=["Parthner garage"],
    summary="Delete a garage item"
    ) 
def delete_item_garage(
                        id:str = Path(...,example="63543e411099e408d2c4e439", description="Object _id Pathner"),
                        uuid:str = Query(...,example="1f4eb576-1bbe-48f1-b179-9780656c8a86", description="uuid ad")
                        ):
    response = remove_garage_item(id,uuid)
    if response:
        return "Deleted"
    raise HTTPException(404,"Not found")