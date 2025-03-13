import os
from typing import Any
from dotenv import load_dotenv
from pydantic import BaseModel
from dotenv import find_dotenv
from pydantic import RedisDsn
from pydantic import model_validator
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class PostgresSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str | None = "postgres"
    password: str | None = "postgres"
    db: str | None = "password_manager"
    database_uri: Any | None
    pool_size: int = 10
    overflow_pool_size: int = 20

    @model_validator(mode="before")
    @classmethod
    def database_uri_validator(cls, data: dict) -> Any:
        """Собираем PG-URI."""

        user = data.get("user") or os.getenv("POSTGRES_USER", "postgres")
        password = data.get("password") or os.getenv(
            "POSTGRES_PASSWORD", "postgres"
        )
        host = os.getenv("POSTGRES_HOST", "localhost")
        port = data.get("port") or os.getenv("POSTGRES_PORT", "5432")
        db = data.get("db") or os.getenv("POSTGRES_DB", "password_manager")

        sqlalchemy_db_uri = (
            f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"
        )

        data.update(
            {"database_uri": sqlalchemy_db_uri},
        )

        return data


class RedisSettings(BaseModel):
    """Настройки подключения к Redis."""

    host: str = "localhost"
    port: int = 6379
    username: str | None = None
    password: str | None = None

    @property
    def broker_url(self) -> str:
        """Получение ссылки сервиса."""
        return str(
            RedisDsn.build(
                scheme="redis",
                username=self.username,
                password=self.password,
                host=self.host,
                port=self.port,
            )
        )


class Settings(BaseSettings):
    """Основные настройки проекта."""

    secret_key: str

    def __init__(self, **values: Any) -> None:
        load_dotenv(find_dotenv())
        super().__init__(**values)

    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="UTF-8",
        arbitrary_types_allowed=True,
    )

    postgres: PostgresSettings = PostgresSettings()
    redis: RedisSettings = RedisSettings()


config = Settings()
