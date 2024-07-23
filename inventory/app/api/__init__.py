from fastapi import APIRouter

from app.api.storages import router as storages_router
from app.api.products import router as products_router

router = APIRouter(prefix="/api")
router.include_router(storages_router)
router.include_router(products_router)
