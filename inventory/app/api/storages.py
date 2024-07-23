from collections.abc import Sequence

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.models import Storage, StorageIn
from app.core.db import get_session

router = APIRouter(prefix="/storages", tags=["storages"])


@router.get("/", response_model=list[Storage])
def read_storages(offset: int = 0, limit: int = 100, session: Session = Depends(get_session)) -> Sequence[Storage]:
    storages = session.exec(select(Storage).offset(offset).limit(limit)).all()
    return storages


@router.get("/{storage_id}/", response_model=Storage)
def read_storage(storage_id: int, session: Session = Depends(get_session)) -> Storage | None:
    storage = session.exec(select(Storage).where(Storage.id == storage_id)).first()
    if not storage:
        raise HTTPException(status_code=404, detail=f"storage with id {storage_id} not found")
    return storage


@router.post("/", response_model=Storage, status_code=201)
def create_storage(storage_in: StorageIn, session: Session = Depends(get_session)) -> Storage:
    storage_obj = Storage(**storage_in.model_dump())
    session.add(storage_obj)
    session.commit()
    session.refresh(storage_obj)
    return storage_obj
