from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.v1.usecases.get_password import GetPasswordUsecase
from app.api.dependencies.request import pg_session_scope
from app.api.v1.usecases.password import PasswordUsecase
from app.api.v1.usecases.search_passwords import SearchPasswordsUsecase


async def password_usecase_scope(
    session: AsyncSession = Depends(pg_session_scope),
) -> PasswordUsecase:
    """DI Scope для PasswordUsecase."""
    return PasswordUsecase(session=session)


async def get_password_usecase_scope(
    session: AsyncSession = Depends(pg_session_scope),
) -> GetPasswordUsecase:
    """DI Scope для GetPasswordUsecase."""
    return GetPasswordUsecase(session=session)


async def get_search_passwords_usecase_scope(
    session: AsyncSession = Depends(pg_session_scope),
) -> SearchPasswordsUsecase:
    """DI Scope для SearchPasswordsUsecase."""
    return SearchPasswordsUsecase(session=session)
