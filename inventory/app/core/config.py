import os
from dataclasses import dataclass
from typing import Annotated, Any, Literal

from pydantic import AnyUrl, BeforeValidator


def parse_cors(cors: Any):
    if isinstance(cors, str) and not cors.startswith("["):
        return [uri.strip() for uri in cors.split(",")]
    if isinstance(cors, list):
        return cors


@dataclass
class Settings:
    TITLE: str = "vkusovshina"
    ENVIRONMENT: Literal["development", "stage", "production"] = "development"
    # DATABASE_URL = "sqlite:///db.sqlite3"
    POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_SERVER = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_DB = os.getenv("POSTGRES_DB", "vkusovshina")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
    TEST_DATABASE_URL = "sqlite:///./db.sqlite3"
    BACKEND_CORS_ORIGINS: Annotated[list[AnyUrl], BeforeValidator(parse_cors)]= ["http://127.0.0.1:8080"]


settings = Settings()
