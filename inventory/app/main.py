from contextlib import asynccontextmanager
from typing import Literal

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.core.db import init_db
from app.api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.ENVIRONMENT == "development":
        init_db()
        yield


app = FastAPI(title=settings.TITLE, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost:8080", "localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
def read_root() -> Literal["hello"]:
    return "hello"


app.include_router(router)
