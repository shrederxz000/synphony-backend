from typing import Annotated, Optional
from pydantic import EmailStr, BaseModel, Field




class CreateUser(BaseModel):
    name:str= Field(min_length=1, max_length=50) 
    email:EmailStr
    age:int= Field(ge=18, le=120)
