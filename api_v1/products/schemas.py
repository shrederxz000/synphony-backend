from typing import Annotated, Optional
from pydantic import EmailStr, BaseModel, Field, ConfigDict


class ProductBase(BaseModel):
    name:str = Field(max_length=100)
    description:str | None = Field(max_length=10000)
    price:int = Field(ge=1)


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(from_attributes=True)
    
    id:int
