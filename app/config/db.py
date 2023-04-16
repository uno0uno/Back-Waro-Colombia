#Python
from http.client import OK
from urllib import response
import uuid

#FastApi
from fastapi import HTTPException,UploadFile
import bson

#Models app Waro Colombia(Internal-post)

#Models app Waro Colombia(Internal)
from app.models.models import NewProduct
from app.models.models import NewOwner
from app.models.models import NewSeller
from app.models.models import NewVenue


#Dump the loaded BSON to valid JSON
from bson import json_util
import json

#Function db
from app.config.db_class import select_db
from app.config.db_class import Validator

#Creation token JWT
from app.auth.jwt_handler import signJWT

#Hash password
from app.auth.hash_class import Hasher

# ====================================
# PRODUCT functions. Create and dalete
# ====================================

#Post new product
def create_new_product(new_product:NewProduct):
    category_bd = select_db()
    _id = category_bd[0].insert_one(dict(new_product)) #add to products, MongoDb
    _id=str(_id.inserted_id)
    return {"_id":_id}

# ==================================
# OWNER functions. Create and dalete
# ==================================

#Post new Owner
def create_new_owner(new_owner:NewOwner):
    category_bd = select_db()
    _id = category_bd[1].insert_one(dict(new_owner)) #add to owners, MongoDb
    _id=str(_id.inserted_id)
    return {"_id":_id}

# =====================================
# # SELLER functions. Create and dalete
# =====================================

#Post new seller
def create_new_seller(new_seller:NewSeller):
    category_bd = select_db()
    _id = category_bd[2].insert_one(dict(new_seller)) #add to selles, MongoDb
    _id=str(_id.inserted_id)
    return {"_id":_id}

# =====================================
# # VENUE functions. Create and dalete
# =====================================

#Post new venue
def create_new_venue(new_venue:NewVenue):
    category_bd = select_db()
    _id = category_bd[2].insert_one(dict(new_venue)) #add to selles, MongoDb
    _id=str(_id.inserted_id)
    return {"_id":_id}

# =====================================
# # USER functions. ONLY QUERIES
# =====================================

#Retrieve all garage items category Body Request
def fetch_all_product_by_filter(category:str,citie_product:str,date_limit_product:str):
    category_bd = select_db()
    document = category_bd[0].find({ "$or":[
        {"category_product":category},
        {"citie_product":citie_product},
        {"date_limit_product":date_limit_product}
        ]})
    return json.loads(json_util.dumps(document))
