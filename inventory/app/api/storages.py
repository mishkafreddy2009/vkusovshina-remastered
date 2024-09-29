from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.models import Storage, StorageCreate, StoragePublic, StoragesPublic
from app.core.db import get_session

router = APIRouter(prefix="/storages", tags=["storages"])


@router.get("/", response_model=list[StoragesPublic])
def read_storages(
    offset: int = 0, limit: int = 100, session: Session = Depends(get_session)
) -> Sequence[Storage]:
    storages = session.exec(select(Storage).offset(offset).limit(limit)).all()
    return storages


@router.get("/{storage_id}/", response_model=StoragePublic)
def read_storage(
    storage_id: int, session: Session = Depends(get_session)
) -> Storage | None:
    storage = session.get(Storage, storage_id)
    if not storage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"storage with id {storage_id} not found",
        )
    return storage


@router.post("/", response_model=StoragePublic, status_code=status.HTTP_201_CREATED)
def create_storage(
    storage_in: StorageCreate, session: Session = Depends(get_session)
) -> Storage:
    db_storage = Storage.model_validate(storage_in)
    session.add(db_storage)
    session.commit()
    session.refresh(db_storage)
    return db_storage


@router.get("/{storage_id}/products/")
def read_storage_products(storage_id: int, session: Session = Depends(get_session)):
    storage = session.get(Storage, storage_id)
    if not storage:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="storage with given id not found",
        )
    return storage.products
