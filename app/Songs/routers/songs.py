#FastAPI
from fastapi import APIRouter, UploadFile, status, HTTPException,Request
from fastapi import Query, Path, Depends
from pydantic import Field

#DataBase encoders
from app.config.db import create_song_and_ad_category
from app.config.db import create_product_and_ad_category
from app.config.db import remove_product,update_product_bd
from app.config.db import new_dowland_song_db
from app.config.db import new_play_song_db

#Models app Waro Colombia(Internal)
from app.models.models import ModelSong

#Function to validate id token expires yet
from app.auth.jwt_bearer import JWTBearer

# ============================================================
# Definitions Router:

songs_router_app = APIRouter(
    prefix="/songs"  
)

# ============================================================
# Path operations Products
# ============================================================

# Post a product 
# ===============
@songs_router_app.post(
    "/{id_parthner}",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
    tags=["Parthner songs"],
    summary="Post a song"  
    ) 
def post_song(
                    model_song:ModelSong,
                    id_parthner:str = Path(...,example="63543c1f1099e408d2c4e435", description="Object _id Parthner")
                    ):
    response = create_song_and_ad_category(model_song.dict(),id_parthner) 
    if response:
        return response
    raise HTTPException(404,"Not found")

# New Dowland song 
# ===============
@songs_router_app.post(
    "/dowlands/{id_song}",
    status_code=status.HTTP_201_CREATED,
    tags=["Parthner songs"],
    summary="New Dowland song"  
    ) 
def new_dowland_song(
    id_song:str = Path(...,example="63543c1f1099e408d2c4e435", description="Object _id Song"),
    number_dowlands:int = Query(...,example="10", description="Number dowlands")
    ):
    response = new_dowland_song_db(id_song,number_dowlands) 
    if response:
        return response
    raise HTTPException(404,"Not found")

# New Play song 
# ===============
@songs_router_app.post(
    "/play/{id_song}",
    status_code=status.HTTP_201_CREATED,
    tags=["Parthner songs"],
    summary="New play song"  
    ) 
def new_play_song(
    id_song:str = Path(...,example="63543c1f1099e408d2c4e435", description="Object _id Song"),
    number_plays:int = Query(...,example="10", description="Number plays")
    ):
    response = new_play_song_db(id_song,number_plays) 
    if response:
        return response
    raise HTTPException(404,"Not found")