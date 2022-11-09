#FastAPI
from sys import maxsize
from fastapi import APIRouter, File, Query, UploadFile, status, Path
from fastapi import Depends, HTTPException

#Function to validate id token expires yet
from app.auth.jwt_bearer import JWTBearer

#INFURA upload photography product
from app.config.db import upload_a_photo_product_bd
from app.config.db import remove_file_bd

# ============================================================
# Definitions Router:

upload_file_app = APIRouter(
    prefix="/files"  
)

# ============================================================
# Path operations Opload file
# ============================================================

# upload a photo product 
# ======================
@upload_file_app.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(JWTBearer())],
    tags=["Parthner post file"],
    summary="upload a photo ad"  
    ) 
def upload_a_photo_product(img_ad:UploadFile = File(...),
                        id_parthner:str = Query(...,
                        example="63543c1f1099e408d2c4e435", 
                        description="Object _id Parthner")
                        ):
    response = upload_a_photo_product_bd(img_ad,id_parthner)
    return response

# Delete a photo product 
# ======================
@upload_file_app.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
    tags=["Parthner post file"],
    summary="Delete a photo ad"  
    ) 
def delete_file(
                id:str = Path(...,example="63543e411099e408d2c4e439", description="Object _id Pathner"),
                hash:str = Query(...,example="QmUn5zGL6M9UP9tZa8TSgUaDEpibsyBr2ADAiXj5HfMHTi", description="Hash file")
                ):
    response = remove_file_bd(id,hash)
    if response:
        return "Deleted"
    raise HTTPException(404,"Not found")
    
