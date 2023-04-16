#FastAPI
from fastapi import HTTPException

#MondoDB Drivers
from pymongo import MongoClient

# env configuration
from app.config.config import settings

#Dump the loaded BSON to valid JSON
from bson import ObjectId

#FastApi
from fastapi import HTTPException,UploadFile

#HTTPS for humans INFURA
import requests

#certify SSL 
import certifi

#ENV INFURA
from app.config.config import PROJECT_ID_INFURA
from app.config.config import PROJECT_SECRET_INFURA
from app.config.config import END_POINT_INFURA

# ============================================================
# Conection with de Database
# ============================================================

client = MongoClient(settings.URL_CLUSTER_MONGO_DB, tlsCAFile=certifi.where())

class Validator(object):
    def __init__(self) -> None:
        pass
    
    @classmethod
    def is_valid(cls, oid):
        if ObjectId.is_valid(oid):
            return True
        raise HTTPException(422,"Unprocessable Entity")

def select_db():
    __category = "MagicV2.0"
    products = client.products[__category]
    owner = client.owner[__category]
    seller = client.seller[__category]
    return [products,owner,seller]

def Validator_email(plain_email, email_bd):
    if plain_email != email_bd : 
        result = True
        return result
    raise HTTPException(409,"Unauthorized")



