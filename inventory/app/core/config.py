from dataclasses import dataclass
from typing import Literal


@dataclass
class Settings:
    TITLE: str = "vkusovshina"
    ENVIRONMENT: Literal["development", "stage", "production"] = "development"
    DATABASE_URL = "sqlite:///db.sqlite3"
    TEST_DATABASE_URL = "sqlite:///./db.sqlite3"


settings = Settings()
