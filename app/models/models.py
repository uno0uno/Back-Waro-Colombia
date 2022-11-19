#Python
from typing import Optional

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
   
    street:str = Field(
                    ...,  #Stees Parthner 
                    min_length=8,
                    max_length=64,
                    example="Calle 39 f # 68 f 66 Sur"
                    )

    city:str = Field(
                    ..., #City Parthner
                    min_length=4,
                    max_length=14,
                    example="Bogotá"
                    )

    neighborhood:str = Field(
                        ..., #Hood Parthner
                        min_length=6,
                        max_length=64,
                        example="Talavera de la reina"
                        )  

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

class ModelAd(BaseModel):  #ads generic parthner
        email:EmailStr = Field( ..., #Email Parthner
                            example="hola@warocol.com"
                            )
        phone:int = Field(
                    ...,#phone Parthner
                    example=3142047013
                    )
        img_ad: str = Field(...,
                            example="QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH"
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
                            max_length=360,
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

