from sqlalchemy.ext.asyncio import AsyncSession

from app.api.utils.usecase import Usecase
from app.api.v1.schemas.base_schema import WithSchema
from app.api.v1.crud.password import PasswordCRUD
from app.api.v1.schemas.client.password import (
    PasswordCreateSchema,
    PasswordResponseSchema,
)


class PasswordUsecase(
    Usecase[WithSchema[str, PasswordCreateSchema], PasswordResponseSchema]
):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.password_crud = PasswordCRUD(self.session)

    async def __call__(
        self, data: WithSchema[str, PasswordCreateSchema]
    ) -> PasswordResponseSchema:
        """Создает или обновляет пароль для сервиса."""
        service_name = data.with_data
        password = data.payload.password

        password_entry = await self.password_crud.create_or_update(
            service_name=service_name,
            password=password,
        )

        return PasswordResponseSchema(
            service_name=password_entry.service_name,
            password=password,
        )
