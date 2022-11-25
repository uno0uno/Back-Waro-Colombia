#Python
import uuid, json

#FastAPI
from fastapi import FastAPI, APIRouter, status, HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File

#DataBase encoders
from app.config.db import fetch_one_ad,fetch_all_category_ads,fetch_one_song


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

# Get all products from category
# =============================
@user_router_app.get("/get/{category_}",
                    status_code=status.HTTP_200_OK,
                    summary="All ads products by category"  
                    )
def get_ad(
        category_:str = Path(...,example="events", description="Name of category"),
        ):
        response =  fetch_all_category_ads(category_)
        if response:
            return response
        raise HTTPException(404,"Not found")


# Get a product from category using id
# ==========================
@user_router_app.get(
        "/getad/{_id1}",
        status_code=status.HTTP_200_OK,
        summary="Single ad product"  
        )
def get_ads(
        _id1:str = Path(...,example="63543e411099e408d2c4e439", description="Object _id Ad")
        ):
        response = fetch_one_ad(_id1) 
        if response:
            return response
        raise HTTPException(404,"Not found")

# Get a song from category using Object Id
# ==========================
@user_router_app.get(
        "/getsong/{id}",
        status_code=status.HTTP_200_OK,
        summary="Single song"  
        )
def get_song(
        id:str = Path(...,example="63810b0569f2c6a4b77948f3", description="Object _id Song")
        ):
        response = fetch_one_song(id) 
        if response:
            return response
        raise HTTPException(404,"Not found")

