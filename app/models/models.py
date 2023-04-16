#Python
from typing import Optional
from importlib_metadata import email

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#Datetime
import datetime

# ===================================================================
# Define models, NewProduct,NewOwner, NewSeller, NewVenue WAROCOL.COM
# ===================================================================

class NewProduct(BaseModel):

    address_product:str = Field( ...,example="Cll 39 f # 68 f 64 norte") #User input
    date_limit_product:str = Field( ...,example="2021-04-31") #User input
    category_product:str = Field( ...,example="dancehall") #User input
    name_product:str = Field( ...,example="Sonidero Bogotano") #User input
    reazon_sell_product:str = Field( ...,example="Cll 39 f # 68 f 64 norte") #User input
    inicial_bid_product:int = Field( ...,example=100) #User input
    citie_product:str = Field( ...,example="Bogotá") #User input
    country_product:str = Field( ...,example="Colombia") #User input
    views_product:int = Field( ...,example=100) #Javascript Input
    status_product:bool = Field( ...,example=False) #Javascript Input
    available_product:bool = Field( ...,example=True) #Javascript Input
    id_seller:str = Field( ...,example="2021-04-31") #Javascript Input
    id_venue:str = Field( ...,example="_Id-object") #Javascript Input #OPTIONAL
    id_owner:str = Field( ...,example="_Id-object") #Javascript Input #OPTIONAL
    artist_product_event:list = Field(...) #Javascript Input #OPTIONAL
    
class NewOwner(BaseModel):

    name_owner_organiser:str = Field( ...,example="Anderson Arévalo") #User input
    description_owner:str = Field( ...,example="100 years experience") #User input
    profile_image_owner:str = Field( ...,example="hash") #User input

class NewSeller(BaseModel):

    name_seller:str = Field( ...,example="Anderson Arévalo") #User input
    email_seller:str = Field( ...,example="hola@warocol.com") #User input
    phone_seller:int = Field( ...,example="3142047013") #User input
    profile_image_seller:str = Field( ...,example="hash") #User input
    email_verification_seller:bool = Field( ...,example=False) #Python #OPTIONAL
    phone_verification_seller:bool = Field( ...,example=False) #Python #OPTIONAL
    kyc_verification_seller:bool = Field( ...,example=False) #Python #OPTIONAL

class NewVenue(BaseModel):

    name_venue:str = Field( ...,example="Def Jamaica") #User input
    description_venue:str = Field( ...,example="Suacha con puestos") #User input
    profile_image_venue:int = Field( ...,example="hash") #User input







