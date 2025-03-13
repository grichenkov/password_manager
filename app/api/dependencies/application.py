from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.api.dependencies.dependency_keys import dependency_getter

pg_engine_scope = dependency_getter(tp=AsyncEngine)


async def pg_sessionmaker_scope(
    pg_engine: AsyncEngine = Depends(pg_engine_scope),
) -> async_sessionmaker[AsyncSession]:
    """DI Scope для pg_sessionmaker."""
    sessionmaker = async_sessionmaker(bind=pg_engine, expire_on_commit=False)
    return sessionmaker
