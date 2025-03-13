from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.crud.password import PasswordCRUD
from app.api.v1.schemas.client.password import PasswordResponseSchema
from app.core.security import decrypt_password
from app.api.utils.usecase import Usecase
from app.api.utils.exceptions import NotFoundError


class GetPasswordUsecase(Usecase[str, PasswordResponseSchema]):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.password_crud = PasswordCRUD(self.session)

    async def __call__(self, service_name: str) -> PasswordResponseSchema:
        """Возвращает расшифрованный пароль, если он есть в БД."""
        password_entry = await self.password_crud.get_password_by_service(
            service_name=service_name
        )

        if password_entry is None:
            raise NotFoundError("Пароль для данного имени службы не найден")

        decrypted_password = decrypt_password(
            password_entry.encrypted_password
        )

        return PasswordResponseSchema(
            service_name=service_name,
            password=decrypted_password,
        )
