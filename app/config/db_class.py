#FastAPI
from ast import Return
from fastapi import HTTPException

#MondoDB Drivers
from pymongo import MongoClient

#Certidy SSL (Mac set)  
import certifi

# env configuration
from app.config.config import settings

#Dump the loaded BSON to valid JSON
from bson import ObjectId

#FastApi
from fastapi import HTTPException,UploadFile

#HTTPS for humans INFURA
import requests

#ENV INFURA
from app.config.config import PROJECT_ID_INFURA
from app.config.config import PROJECT_SECRET_INFURA
from app.config.config import END_POINT_INFURA

from starlette.background import BackgroundTask

# ============================================================
# Conection with de Database
# ============================================================

client = MongoClient(settings.URL_CLUSTER_MONGO_DB,tlsCAFile=certifi.where())

class Validator(object):
    def __init__(self) -> None:
        pass
    
    @classmethod
    def is_valid(cls, oid):
        if ObjectId.is_valid(oid):
            return True
        raise HTTPException(422,"Unprocessable Entity")

def select_db():
    __category = "MagicV1"
    products = client.products[__category]
    parthner = client.parthner[__category]
    return [products, parthner]

def Validator_email(plain_email, email_bd):
    if plain_email != email_bd : 
        result = True
        return result
    raise HTTPException(409,"Unauthorized")

def infura_file(img_ad:UploadFile):
        files = {'file': img_ad.file}           
        # if len(img_ad.file.read()) > 10000000:
        #     raise HTTPException(409,"File size not allowed")
        if img_ad.content_type not in ["image/png", "image/jpg", "image/jpeg"]:
            raise HTTPException(409,"File extension not allowed")
        response = requests.post(END_POINT_INFURA + '/api/v0/add', files=files, auth=(PROJECT_ID_INFURA, PROJECT_SECRET_INFURA))
        hash = response.text.split(",")[1].split(":")[1].replace('"','')
        return hash
        

def infura_fire_delete(hash:str):
    params = {'arg': hash}
    response3 = requests.post(END_POINT_INFURA + '/api/v0/pin/rm', params=params, auth=(PROJECT_ID_INFURA, PROJECT_SECRET_INFURA))
    return response3



