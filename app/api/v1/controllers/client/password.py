from fastapi import APIRouter, Depends, status
from app.api.dependencies.usecase import password_usecase_scope
from app.api.dependencies.usecase import get_password_usecase_scope
from app.api.dependencies.usecase import get_search_passwords_usecase_scope
from app.api.v1.usecases.password import PasswordUsecase
from app.api.v1.usecases.get_password import GetPasswordUsecase
from app.api.v1.usecases.search_passwords import SearchPasswordsUsecase
from app.api.v1.schemas.base_schema import WithSchema
from app.api.v1.schemas.client.password import PasswordResponseSchema
from app.api.v1.schemas.client.password import PasswordCreateSchema

ROUTER = APIRouter()


@ROUTER.post(
    "/{service_name}",
    status_code=status.HTTP_200_OK,
    response_model=PasswordResponseSchema,
    name="Создание или обновление пароля",
    description="Сохраняет или обновляет пароль для указанного сервиса",
)
async def create_or_update_password(
    service_name: str,
    payload: PasswordCreateSchema,
    usecase: PasswordUsecase = Depends(password_usecase_scope),
) -> PasswordResponseSchema:
    """Создание или обновление пароля."""
    return await usecase(
        data=WithSchema(with_data=service_name, payload=payload)
    )


@ROUTER.get(
    "/{service_name}",
    response_model=PasswordResponseSchema,
    status_code=status.HTTP_200_OK,
    name="Получение пароля по имени сервиса",
    description="Возвращает расшифрованный пароль для указанного сервиса.",
)
async def get_password(
    service_name: str,
    usecase: GetPasswordUsecase = Depends(get_password_usecase_scope),
) -> PasswordResponseSchema:
    """Получение пароля по имени сервиса."""
    return await usecase(service_name=service_name)


@ROUTER.get(
    "/",
    response_model=list[PasswordResponseSchema],
    status_code=status.HTTP_200_OK,
    name="Поиск паролей по части имени сервиса",
    description="Возвращает список паролей для сервисов,"
    " содержащих указанную строку в имени.",
)
async def search_passwords(
    service_name: str,
    usecase: SearchPasswordsUsecase = Depends(
        get_search_passwords_usecase_scope
    ),
) -> list[PasswordResponseSchema]:
    """Поиск паролей по части имени сервиса."""
    return await usecase(service_name=service_name)
