from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.schemas.client.password import PasswordResponseSchema
from app.api.v1.crud.password import PasswordCRUD
from app.core.security import decrypt_password
from app.api.utils.usecase import Usecase


class SearchPasswordsUsecase(Usecase[str, list[PasswordResponseSchema]]):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.password_crud = PasswordCRUD(self.session)

    async def __call__(
        self, service_name: str
    ) -> list[PasswordResponseSchema]:
        """Возвращает список паролей, если имя частично совпадает."""
        password_entries = (
            await self.password_crud.search_passwords_by_service_name(
                service_name
            )
        )

        return [
            PasswordResponseSchema(
                service_name=entry.service_name,
                password=decrypt_password(entry.encrypted_password),
            )
            for entry in password_entries
        ]
