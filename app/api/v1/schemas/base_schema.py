"""Базовая схема ORJSON, можно использовать как базовую pydantic схему."""

from datetime import datetime
from typing import Any, Generic, Literal, TypeVar

from pydantic import BaseModel, ConfigDict, Field, GetCoreSchemaHandler
from pydantic.v1.datetime_parse import parse_datetime
from pydantic_core import CoreSchema, core_schema
from pydantic_core.core_schema import ValidationInfo
from app.api.utils.enums.internal_exception_status import InternalErrorEnum


class BaseSchema(BaseModel):
    """Базовая схема для всех моделей API."""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        from_attributes=True,
        arbitrary_types_allowed=True,
    )


class ErrorSchema(BaseSchema):
    message: str = Field(description="Сообщение об ошибке")
    code: InternalErrorEnum = Field(description="Системный код ошибки")


class StrictDatetime(datetime):
    """Валидатор datetime, запрещает инициализацию через int."""

    @classmethod
    def validate(cls, value: Any, _: ValidationInfo) -> datetime:
        if str(value).isdigit():
            raise ValueError(
                "Некорректный формат даты, используйте YYYY-MM-DD H:M:S!"
            )
        return parse_datetime(value)

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _: Any, handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.with_info_before_validator_function(
            cls.validate, handler(Any), field_name=handler.field_name
        )


class OkSchema(BaseSchema):
    """Схема ответа 'ok'."""

    status: Literal["ok"] = Field("ok", description="Статус")


TWith = TypeVar("TWith")
TSchema = TypeVar("TSchema", bound=BaseSchema)


class WithSchema(BaseSchema, Generic[TWith, TSchema]):
    """Общий ответ с данными."""

    with_data: TWith
    payload: TSchema
