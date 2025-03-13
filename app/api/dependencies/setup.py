from collections.abc import AsyncGenerator
from contextlib import AsyncExitStack
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import config


@asynccontextmanager
async def setup_dependencies() -> AsyncGenerator[dict, None]:
    """Настраивает все зависимости уровня APP."""

    async with AsyncExitStack() as stack:
        asyncengine = create_async_engine(
            config.postgres.database_uri,
            pool_size=config.postgres.pool_size,
            max_overflow=config.postgres.overflow_pool_size,
            pool_pre_ping=True,
        )

        sessionmaker = async_sessionmaker(
            bind=asyncengine, expire_on_commit=False
        )

        dependencies = {
            "asyncengine": asyncengine,
            "sessionmaker": sessionmaker,
        }

        yield dependencies

        await asyncengine.dispose()
        await stack.aclose()
