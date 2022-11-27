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
    
    files:Optional[list] = None
    
    payments:Optional[list] = None
    
    songs:Optional[list] = None
class ModelAd(BaseModel):  #ads public generic parthner
        email:EmailStr = Field( ..., #Email Parthner
                            example="hola@warocol.com"
                            )
        phone:int = Field(
                            ...,#phone Parthner
                            example=3142047013
                            )
        link_contact:Optional[str] = Field(
                            None,#phone Parthner
                            max_length=100,
                            min_length=1,
                            example="https://chat.whatsapp.com/EED536nR8Et2Nh0DCRDsGs"
                            )
        full_price: int = Field(
                                ...,
                                example=50000
                                )

        off_price : int = Field(...,
                                example=30
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
        deadline_ad:str = Field(...)
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
        hood_ad: str = Field(
                            ...,
                            min_length=1,
                            max_length=30,
                            example="Ciudad Bolivar" 
                            )
class Payments(BaseModel):
        title:str = Field( ..., #Name Product
                            example="My product"
                            )
        currency_id:str = Field( ..., #Currency Payment
                            example="COP"
                            )
        description:str = Field( ..., #Description Product
                            example="description product"
                            )
        quantity:int = Field( ..., #Quantity products
                            example="1"
                            )
        unit_price:int = Field( ..., #Amount 10000
                            example="10000"
                            )   
        email:EmailStr = Field( ..., #Email Parthner
                            example="hola@warocol.com"
                            )                
class ModelSong(BaseModel):  #ads public generic parthner
        
        songHash: str = Field(
                            ...,
                            max_length=360,
                            min_length=1,
                            example="Qmb5p6W7o3BXecXM8dvW8ExhUgJqnUf7QWfDjGdK398RiD"
                            )
        imgHash: str = Field(
                            ...,
                            max_length=360,
                            min_length=1,
                            example="QmUhkW4mEaJyGWqVvBSrBXEp1ZzSDi548xcADWpn4S2GhP"
                            )

        nameSong: str = Field(
                            ...,
                            max_length=360,
                            min_length=1,
                            example="La Junta"
                            )

        nameArtist: str = Field(
                            ...,
                            min_length=1,
                            max_length=30, 
                            example="Tres Coronas"
                            )
        
        genre: str = Field(
                            ...,
                            min_length=1,
                            max_length=30, 
                            example="Hip-Hop"
                            )
                                    
        city: str = Field(
                            ...,
                            min_length=1,
                            max_length=30, 
                            example="Bogotá"
                            )
                                    
        country: str = Field(
                            ...,
                            min_length=1,
                            max_length=30, 
                            example="Colombia"
                            )
        dowlandType: str = Field(
                            ...,
                            min_length=1,
                            max_length=30, 
                            example="Descarga gratis"
                            )
        dowlands:int = Field(
                    ...,#phone Parthner
                    example=0
                    )
        play:int = Field(
                    ...,#phone Parthner
                    example=0
                    )

        status_ad:Optional[bool] = Field(None, example=False)

        deprecated: Optional[bool] = Field(None, example=False)

        ONErpm:str = Field(
                    ...,#phone Parthner
                    example="https://onerpm.link/LaJunta"
                    )
        youtube:str = Field(
                    ...,#phone Parthner
                    example="https://youtu.be/e8XrZ3g0qfY"
                    )
        description: str = Field(
                            ...,
                            max_length=1000,
                            min_length=1,
                            example="Esta es una descripcion corte del producto "
                            )
        


