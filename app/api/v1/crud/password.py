from app.api.v1.crud.base.base_crud import BaseCRUD
from app.api.v1.models.password import PasswordEntryModel
from sqlalchemy import select, update, insert
from app.core.security import encrypt_password
from collections.abc import Sequence


class PasswordCRUD(BaseCRUD[PasswordEntryModel]):
    async def get_password_by_service(
        self, service_name: str
    ) -> PasswordEntryModel | None:
        """Получить объект пароля по имени сервиса."""
        stmt = select(PasswordEntryModel).where(
            PasswordEntryModel.service_name == service_name
        )
        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def create_or_update(
        self, service_name: str, password: str
    ) -> PasswordEntryModel:
        """Создать или обновить пароль для сервиса."""
        encrypted_password = encrypt_password(password)

        existing_password = await self.get_password_by_service(service_name)

        if existing_password:
            stmt = (
                update(PasswordEntryModel)
                .where(PasswordEntryModel.service_name == service_name)
                .values(encrypted_password=encrypted_password)
                .returning(PasswordEntryModel)
            )
        else:
            stmt = (
                insert(PasswordEntryModel)
                .values(
                    service_name=service_name,
                    encrypted_password=encrypted_password,
                )
                .returning(PasswordEntryModel)
            )

        result = await self.db.execute(stmt)
        return result.scalars().first()

    async def search_passwords_by_service_name(
        self, part_of_service_name: str
    ) -> Sequence[PasswordEntryModel]:
        """Поиск паролей по части имени сервиса."""
        stmt = select(PasswordEntryModel).where(
            PasswordEntryModel.service_name.ilike(f"%{part_of_service_name}%")
        )
        result = await self.db.execute(stmt)
        return result.scalars().all()
