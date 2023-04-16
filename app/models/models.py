#Python
from typing import Optional
from importlib_metadata import email

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

#Datetime
import datetime

# ============================================================
# Define models, Parthners WAROCOL.COM
# ============================================================
class ParthnerLogin(BaseModel): #Login parthner
    email:EmailStr = Field( ..., #Email Parthner
                        example="hola@warocol.com"
                        )

    password:str = Field(
                        ...,
                        min_length=8,
                        max_length=64,
                        example='password',
                        )
class ParthnerInfoUpdate(ParthnerLogin):  #Info Parthner
   
    phone:int = Field(
                    ...,#phone Parthner
                    example=3142047013
                    )

    name_business:str = Field(
                        ..., #Name Bussines required
                        min_length=1,
                        max_length=30,
                        example="Waro Colombia"
                        )

    status_parthner:Optional[bool] = Field(None, example=True) 
class ParthnerInfo(ParthnerInfoUpdate):  #Info Parthner
    ads:Optional[list] = None

    payments:Optional[list] = None
    
    songs:Optional[list] = None

    garage:Optional[list] = None
class Payments(BaseModel): #payments public generic parthner
        id_product:str = Field( ..., #Name Product
                            example="QmUhkW4mEaJyGWqVvBSrBXEp1ZzSDi548xcADWpn4S2GhP"
                            )
        id_parthner:str = Field( ..., #Name Product
                            example="QmUhkW4mEaJyGWqVvBSrBXEp1ZzSDi548xcADWpn4S2GhP"
                            )
        name_product:str = Field( ..., #Description Product
                            example="description product"
                            )
        quantity:int = Field( ..., #Quantity products
                            example="1"
                            )
        unit_price:int = Field( ..., #Amount 10000
                            example="10000"
                            )   
        phone:int = Field( ..., #Email Parthner
                            example="3142047013"
                            ) 
        address:str = Field( ..., #Email Parthner
                            example="hola@warocol.com"
                            )
        state:str = Field( ..., #Email Parthner
                            example="hola@warocol.com"
                            )                      
class ModelGarage(BaseModel):  #garage public generic parthner
    email:EmailStr = Field( ..., #Email Parthner
                            example="hola@warocol.com"
                            )
    full_price: int = Field(
                            ...,
                            example=50000
                            )
    description: str = Field(
                            ...,
                            max_length=1000,
                            min_length=1,
                            example="Esta es una descripcion corte del producto "
                            )

    category: str = Field(
                        ...,
                        min_length=1,
                        max_length=30, 
                        example="Eventos"
                        )

    status_ad:Optional[bool] = Field(None, example=True)

    deprecated: Optional[bool] = Field(None, example=False)

    name_ad: str = Field(
                        ...,
                        min_length=1,
                        max_length=90,
                        example="Sonidero Bogotano" 
                        )
    name_business:str = Field(
                        ..., #Name Bussines required
                        min_length=1,
                        max_length=30,
                        example="Waro Colombia"
                        )
    city_ad: str = Field(
                        ...,
                        min_length=1,
                        max_length=30,
                        example="Bogotá" 
                        )
    imgHash: str = Field(
                        ...,
                        max_length=360,
                        min_length=1,
                        example="QmUhkW4mEaJyGWqVvBSrBXEp1ZzSDi548xcADWpn4S2GhP"
                        )
    shipping:Optional[int] = Field(
                            None,#phone Parthner
                            example="7000"
                            )
    status_shipping:Optional[bool] = Field(None, example=True)
    status_pickup:Optional[bool] = Field(None, example=True)
    saving: int = Field(
                            ...,
                            example=50000
                            )
    

