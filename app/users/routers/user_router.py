#Python
import uuid, json

#FastAPI
from fastapi import FastAPI, APIRouter, status, HTTPException
from fastapi import Path

#DataBase encoders
from app.config.db import fetch_all_category_garage
from app.config.db import fetch_one_item_garage

# ============================================================
# Definitions Router:

user_router_app = APIRouter(
    prefix="/user",
    tags=["Get category and single ad"]
)
# ============================================================

# ============================================================
# Path operations, Parthner
# ============================================================

# Get garage item from category using id
# ==========================
@user_router_app.get(
        "/getgarageitem/{_id1}",
        status_code=status.HTTP_200_OK,
        summary="Single garage product"  
        )
def get_one_garage_item(
        _id1:str = Path(...,example="63543e411099e408d2c4e439", description="Object _id Ad")
        ):
        response = fetch_one_item_garage(_id1) 
        if response:
            return response
        raise HTTPException(404,"Not found")

# Get all garage sale from category
# =============================
@user_router_app.get("/getgarage/{category_}",
                    status_code=status.HTTP_200_OK,
                    summary="All garage products by category"  
                    )
def get_garage_item(
        category_:str = Path(...,example="events", description="Name of category"),
        ):
        response =  fetch_all_category_garage(category_)
        if response:
            return response
        raise HTTPException(404,"Not found")


