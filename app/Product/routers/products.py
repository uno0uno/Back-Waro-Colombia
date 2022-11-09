#FastAPI
from fastapi import APIRouter, UploadFile, status, HTTPException,Request
from fastapi import Query, Path, Depends
from pydantic import Field

#DataBase encoders
from app.config.db import create_product_and_ad_category
from app.config.db import remove_product,update_product_bd

#Models app Waro Colombia(Internal)
from app.models.models import ModelAd

#Function to validate id token expires yet
from app.auth.jwt_bearer import JWTBearer

# ============================================================
# Definitions Router:

product_router_app = APIRouter(
    prefix="/product"  
)

# ============================================================
# Path operations Products
# ============================================================

# Post a product 
# ===============
@product_router_app.post(
    "/{id_parthner}",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
    tags=["Parthner products"],
    summary="Post single ad"  
    ) 
def post_product(
                    model_ad:ModelAd,
                    id_parthner:str = Path(...,example="63543c1f1099e408d2c4e435", description="Object _id Parthner")
                    ):
    response = create_product_and_ad_category(model_ad.dict(),id_parthner) 
    if response:
        return response
    raise HTTPException(404,"Not found")

# Updates a product 
# ===============
@product_router_app.put(
                        "/{id}",
                        status_code=status.HTTP_201_CREATED,
                        dependencies=[Depends(JWTBearer())],
                        tags=["Parthner products"],
                        summary="Update a Single ad"  
                        )
def update_product(
                        model_ad:ModelAd,
                        id:str = Path(...,example="63543c1f1099e408d2c4e435", description="Id ad")
                        ):
    response = update_product_bd(model_ad.dict(),id)
    if response:
        return "updated"
    raise HTTPException(404,"Not found")


# Delete a product 
# ================
@product_router_app.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
    tags=["Parthner products"],
    summary="Delete ad"
    ) 
def delete_product(
                        id:str = Path(...,example="63543e411099e408d2c4e439", description="Object _id Pathner"),
                        uuid:str = Query(...,example="1f4eb576-1bbe-48f1-b179-9780656c8a86", description="uuid ad")
                        ):
    response = remove_product(id,uuid)
    if response:
        return "Deleted"
    raise HTTPException(404,"Not found")