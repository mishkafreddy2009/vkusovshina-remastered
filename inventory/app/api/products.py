from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.models import Product, ProductIn, Storage
from app.core.db import get_session

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/{product_id}/", response_model=Product)
def read_product(product_id: int, session: Session = Depends(get_session)) -> Product | None:
    product = session.exec(select(Product).where(Product.id == product_id)).first()
    if not product:
        raise HTTPException(status_code=404, detail=f"product with id {product_id} not found")
    return product


@router.get("/", response_model=list[Product])
def read_products(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)) -> Sequence[Product]:
    products = session.exec(select(Product).offset(offset).limit(limit)).all()
    return products


@router.post("/{storage_id}/", response_model=Product, status_code=201)
def create_product(storage_id: int, product_in: ProductIn, session: Session = Depends(get_session)) -> Product:
    storage_obj = session.exec(select(Storage).where(Storage.id == storage_id)).first()
    if not storage_obj:
        raise HTTPException(status_code=404, detail=f"storage with id {storage_id} not found")
    product_obj = Product(**product_in.model_dump(), storage_id=storage_id)
    session.add(product_obj)
    session.commit()
    session.refresh(product_obj)
    return product_obj
