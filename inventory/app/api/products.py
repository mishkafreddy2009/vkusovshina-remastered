from collections.abc import Sequence
import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlmodel import Session, select
from sqlalchemy.exc import IntegrityError
from PIL import Image

from app.models import (
    Product,
    ProductCreate,
    ProductPublic,
    ProductImage,
    Storage,
)
from app.core.db import get_session

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/{product_id}/", response_model=Product)
def read_product(
    product_id: int, session: Session = Depends(get_session)
) -> Product | None:
    product = session.get(Product, product_id)
    if not product:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="product with given id not found",
        )
    try:
        return product
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="unexpected error occured while fethcing product",
        )


@router.get("/", response_model=list[ProductPublic])
def read_products(
    offset: int = 0, limit: int = 100, session: Session = Depends(get_session)
) -> Sequence[Product]:
    products = session.exec(select(Product).offset(offset).limit(limit)).all()
    try:
        return products
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="unexpected error occured while fetching products",
        )


@router.post(
    "/{storage_id}/", response_model=ProductPublic, status_code=status.HTTP_201_CREATED
)
def create_product(
    storage_id: int, product_in: ProductCreate, session: Session = Depends(get_session)
) -> Product:
    db_storage = session.get(Storage, id)
    if not db_storage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="storage with given id not found",
        )
    if product_in.quantity + db_storage.capacity > db_storage.capacity:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="storage is full"
        )
    try:
        db_storage.current_stock += product_in.quantity
        product_obj = Product.model_validate(
            product_in, update={"storage_id": storage_id}
        )
        session.add(product_obj)
        session.add(db_storage)
        session.commit()
        session.refresh(product_obj)
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="product with given data already exists",
        )
    except Exception:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="unexpected error occured while creating product",
        )
    return product_obj


@router.post("/{product_id}/image/")
def create_product_image(
    product_id: int,
    file_in: UploadFile = File(...),
    session: Session = Depends(get_session),
):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="product with given id not found",
        )
    if file_in.filename:
        try:
            uuid_str = str(uuid.uuid4())
            file_out = "app/static/" + uuid_str + ".jpg"
            with Image.open(file_in.file) as im:
                resized = im.resize((512, 512))
                resized.save(file_out)
            db_product_image = ProductImage(
                url=uuid_str + ".jpg", product_id=product_id
            )
            session.add(db_product_image)
            session.commit()
            session.refresh(db_product_image)
        except OSError:
            print("bebra")
    return "bebra"


@router.get("/{product_id}/image/")
def read_product_images(product_id: int, session: Session = Depends(get_session)):
    product_image = session.exec(
        select(ProductImage).where(ProductImage.product_id == product_id)
    ).first()
    return product_image
