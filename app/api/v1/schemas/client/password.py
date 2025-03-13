from pydantic import Field
from app.api.v1.schemas.base_schema import BaseSchema


class PasswordCreateSchema(BaseSchema):
    """Схема для создания пароля."""

    password: str = Field(
        ..., min_length=5, description="Пароль не может быть пустым"
    )


class PasswordResponseSchema(BaseSchema):
    """Схема для ответа с паролем."""

    service_name: str = Field(..., description="Название сервиса")
    password: str = Field(..., description="Расшифрованный пароль")
