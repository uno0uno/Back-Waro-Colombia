#Python
from http.client import OK
from urllib import response
import uuid

#FastApi
from fastapi import HTTPException,UploadFile
import bson

#Models app Waro Colombia(Internal-post)
from app.models.models import ParthnerLogin
from app.models.models import ParthnerInfoUpdate
from app.models.models import ParthnerInfo
from app.models.models import ModelAd

#Dump the loaded BSON to valid JSON
from bson import json_util
import json

#Function db
from app.config.db_class import select_db
from app.config.db_class import Validator
from app.config.db_class import infura_file
from app.config.db_class import infura_fire_delete

#Creation token JWT
from app.auth.jwt_handler import signJWT

#Hash password
from app.auth.hash_class import Hasher



# =============================================================
# User functions. Fetch a single product and categories product
# =============================================================

#Retrieve all ads category Body Request
def fetch_all_category_ads(category_:str):
    category = select_db()
    document = category[0].find({"category":category_,"status_ad":True},{"name_ad":1,"deadline_ad":1, "city_ad":1, "id_ad":1, "img_ad":1, "off_price":1})
    return json.loads(json_util.dumps(document))

#Retrieve an ad using ID PATH PARAMETER
def fetch_one_ad( _id1:str):
    Validator.is_valid(_id1)
    category = select_db()
    document = category[0].find_one({"_id":bson.ObjectId(_id1)})
    return json.loads(json_util.dumps(document))

# =============================================
# Parthner functions. Upload file and delete
# =============================================

#Upload file, generate hash and push to parthner
def upload_a_photo_product_bd(img_ad:UploadFile, id_parthner:str):
    Validator.is_valid(id_parthner)
    category_bdd = select_db()
    hash = infura_file(img_ad)
    category_bdd[1].update_one({"_id":bson.ObjectId(id_parthner)},{"$addToSet":{"files":hash}})
    return hash

def remove_file_bd(id:str,hash:str):
    Validator.is_valid(id)
    category_bdd = select_db()
    response = infura_fire_delete(hash)
    category_bdd[1].update_one({'_id':bson.ObjectId(id)},{"$pull":{"files":hash}})
    return response

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Products functions. Post, update and delete
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Post a product, generate an uuid and push to parthner and products
def create_product_and_ad_category(model_ad:ModelAd,
                                        id_parthner:str
                                        ):
    Validator.is_valid(id_parthner)
    category_bdd = select_db()
    is_ad = str(uuid.uuid4())
    model_ad["id_ad"] = is_ad
    category_bdd[0].insert_one(dict(model_ad)) #add to products
    category_bdd[1].update_one({"_id":bson.ObjectId(id_parthner)},{"$push":{"ads":is_ad}}) # add to ads category
    return model_ad

#Update a product 
def update_product_bd(
                    model_ad:ModelAd,
                    id:str
                    ):
    Validator.is_valid(id)
    category_bdd = select_db()
    category_bdd[0].update_one({'_id':bson.ObjectId(id)},{"$set":dict(model_ad)})
    return True

#Delete a product, Integrate to category ads
def remove_product(id:str,uuid:str):
    Validator.is_valid(id)
    category_bdd = select_db()
    category_bdd[0].update_one({"id_ad":uuid},{"$set":{"deprecated":True}})
    category_bdd[1].update_one({'_id':bson.ObjectId(id)},{"$pull":{"ads":uuid}})
    return True

# =============================================
# Parthner functions. Create and update ACCOUNT
# =============================================

#Check user parthner
def check_parther(parthner_login:ParthnerLogin):
    category_bdd = select_db()
    try:
        document = category_bdd[1].find_one({"email":parthner_login["email"]},{"email":1, "password":1})
        if Hasher.verify_password(parthner_login["password"],document["password"]):
            return document
        return False
    except:
        raise HTTPException(401,"Unauthorized")

#Create a Parthner
def create_parthner(parthner_info:ParthnerInfo):
    category_parthner_bd = select_db()
    document = category_parthner_bd[1].find_one({"email":parthner_info["email"]},{"email":1})
    if not document:
        parthner_info["password"] = Hasher.get_hash_password(parthner_info["password"])
        category_parthner_bd[1].insert_one(dict(parthner_info)) #add to collection
        return signJWT(parthner_info["email"])
    else :
        return False

#Update a Parthner info
def update_parthner(Parthner_info_update:ParthnerInfoUpdate, id:str):
    Validator.is_valid(id)
    category_parthner_bd = select_db()
    category_parthner_bd[1].update_one({'_id':bson.ObjectId(id)},{"$set":dict(Parthner_info_update)}) #add to colection
    return Parthner_info_update

#Retrieve Parthner info
def get_parthner_info_bd (email:str):
    category_bdd = select_db()
    document = category_bdd[1].find_one({"email":email},{"password":0})
    return json.loads(json_util.dumps(document))

#Retrieve all ads Parthner email path parameter
def fetch_all_ads_parthner(email:str):
    category = select_db()
    document = category[0].find({"email":email, "deprecated":False})
    return json.loads(json_util.dumps(document))

#Delete a product, Integrate to category ads
def remove_parthner_bd(id:str,email:str):
    Validator.is_valid(id)
    category_bdd = select_db()
    category_bdd[0].delete_many({"email":email})
    category_bdd[1].delete_one({'_id':bson.ObjectId(id)})
    return True

