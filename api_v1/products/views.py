from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, status, Depends
from . import crud
from .schemas import Product, ProductCreate
from core.models import db_helper


router = APIRouter(tags=["products"])


@router.get("/", response_model=list[Product])
async def get_products(session:AsyncSession = Depends(db_helper.scoped_session_dependency)):

    return await crud.get_products(session=session)


@router.get("/{product_id}", response_model=Product)
async def get_products(product_id:int, session:AsyncSession = Depends(db_helper.scoped_session_dependency)):

    return await crud.get_products(session=session, 
                                    product_id=product_id)



@router.post("/", response_model=ProductCreate)
async def create_product(product_in:ProductCreate,
                         session:AsyncSession = Depends(db_helper.scoped_session_dependency)):
    print(product_in)
    product = await crud.create_product(session=session, product_in=product_in)
    
    if product is not None:
        
        return product_in

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product {product_in} not found" )
