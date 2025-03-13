from collections.abc import Callable, Coroutine
from typing import Any, Generic, TypeVar, cast

from starlette.requests import Request

from app.api.utils.exceptions import UndefinedDependencyError

T = TypeVar("T")


def determine_name(key: type[T] | str) -> str:
    """Определяет имя зависимости по типу или строке."""
    if isinstance(key, type):
        return key.__name__.lower()
    if isinstance(key, str):
        return key
    raise UndefinedDependencyError(tp=key, dependency_key=key)


class DependencyKey(Generic[T]):
    """Класс для хранения и получения зависимости."""

    __slots__ = ("key", "instance")

    def __init__(self, instance: T, tp: type[T] | None = None) -> None:
        self.key = determine_name(tp or type(instance))
        self.instance = instance

    def __call__(self) -> T:
        """Возвращает зависимость."""
        return self.instance


def dependency_getter(
    tp: type[T], dependency_key: str | None = None
) -> Callable[[Request], Coroutine[Any, Any, T]]:
    """Получает зависимость из `request.state`."""
    key = determine_name(dependency_key or tp)

    async def getter(request: Request) -> T:
        return cast(T, getattr(request.state, key))

    return getter
