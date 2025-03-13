from collections.abc import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.api.dependencies.application import pg_sessionmaker_scope


async def pg_session_scope(
    pg_sessionmaker: async_sessionmaker[AsyncSession] = Depends(
        pg_sessionmaker_scope
    ),
) -> AsyncGenerator[AsyncSession, None]:
    """DI Scope для AsyncSession."""
    async with pg_sessionmaker.begin() as session:
        yield session
