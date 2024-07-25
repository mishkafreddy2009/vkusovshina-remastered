from collections.abc import Sequence
import os
import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError
from PIL import Image

from app.models import Product, ProductImage, ProductImageIn, ProductIn, Storage
from app.core.db import get_session

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/{product_id}/", response_model=Product)
def read_product(product_id: int, session: Session = Depends(get_session)) -> Product | None:
    product = session.exec(select(Product).where(Product.id == product_id)).first()
    if not product:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product with given id not found")
    try:
        return product
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="unexpected error occured while fethcing product"
        ) from e


@router.get("/", response_model=list[Product])
def read_products(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)) -> Sequence[Product]:
    products = session.exec(select(Product).offset(offset).limit(limit)).all()
    try:
        return products
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="unexpected error occured while fetching products"
        ) from e


@router.post("/{storage_id}/", response_model=Product, status_code=status.HTTP_201_CREATED)
def create_product(storage_id: int, product_in: ProductIn, session: Session = Depends(get_session)) -> Product:
    storage_obj = session.exec(select(Storage).where(Storage.id == storage_id)).first()
    if not storage_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="storage with given id not found"
        )
    if product_in.quantity + storage_obj.capacity > storage_obj.capacity:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="storage is full")
    try:
        storage_obj.current_stock += product_in.quantity
        product_obj = Product(**product_in.model_dump(), storage_id=storage_id)
        session.add(product_obj)
        session.add(storage_obj)
        session.commit()
        session.refresh(product_obj)
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="product with given data already exists")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="unexpected error occured while creating product")
    return product_obj


@router.post("/uploadfile/{product_id}")
def create_product_image(product_id: int, file_in: UploadFile = File(...), session: Session = Depends(get_session)):
    product_obj = session.exec(select(Product).where(Product.id == product_id)).first()
    if not product_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="product with given id not found"
        )
    if file_in.filename:
        try:
            uuid_str = str(uuid.uuid4())
            file_out = "app/static/" + uuid_str + ".jpg"
            with Image.open(file_in.file) as im:
                resized = im.resize((512, 512))
                resized.save(file_out)
            product_image_obj = ProductImage(url=file_out, product_id=product_id)
            session.add(product_image_obj)
            session.commit()
            session.refresh(product_image_obj)
            print(product_image_obj)
        except OSError:
            print("caannot")
    return "bebra"


@router.get("/{product_id}/images")
def read_product_images(product_id: int, session: Session = Depends(get_session)):
    product = session.exec(select(Product).where(Product.id == product_id)).first()
    return product.images
