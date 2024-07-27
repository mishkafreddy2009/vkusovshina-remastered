import os
from dataclasses import dataclass
from typing import Literal


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


settings = Settings()
