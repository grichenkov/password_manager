from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from app.api.dependencies.setup import setup_dependencies
from app.api.utils.exception_handler import setup_exception_handlers
from app.api.router import ROUTER


@asynccontextmanager
async def lifespan(*args, **kwargs) -> AsyncGenerator[dict, None]:
    """Жизненный цикл FastAPI."""
    async with setup_dependencies() as dependencies:
        yield dependencies


app = FastAPI(
    title="Password Manager",
    description="API для управления паролями",
    version="1.0.0",
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

setup_exception_handlers(app)

app.include_router(ROUTER)


def run_server():
    """Функция для запуска сервера через poetry run password-manager"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    run_server()
