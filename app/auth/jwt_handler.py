# This file is responsible for singing, encoding, decoding and returning JWTs.

#env configuration
from app.config.config import JWT_SECRET, JWT_ALGORITHM

#python tipe
import time 

#python JWT
import jwt

#Function return the genereted tokens(JWTs)
def token_response(token:str):
    return{"token" : token}
    
#Function used for singing the JWT string
def signJWT(user_id:str):
    payload = {
        "user_id" : user_id,
        "expires" : time.time() + 86400
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)

#Function to validate id token expires yet
def decodeJWT(token:str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
