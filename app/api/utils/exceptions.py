from starlette import status

from app.api.utils.enums.internal_exception_status import InternalErrorEnum


class BaseError(Exception):
    message: str
    internal_status_code: InternalErrorEnum | None = None
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(
        self,
        message: str,
        internal_status_code: InternalErrorEnum | None = None,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ) -> None:
        self.message = message
        self.internal_status_code = (
            internal_status_code or InternalErrorEnum.INTERNAL_ERROR
        )
        self.status_code = status_code

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.message}"


class UndefinedDependencyError(BaseError):
    def __init__(self, tp: type, dependency_key: str) -> None:
        super().__init__(
            message=f"Нераспознанная зависимость: {tp=} {dependency_key=}",
            internal_status_code=InternalErrorEnum.INTERNAL_ERROR,
        )


class DatabaseError(BaseError):
    def __init__(
        self,
        message: str,
        internal_status_code: InternalErrorEnum = InternalErrorEnum.INTERNAL_ERROR,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
    ) -> None:
        super().__init__(
            message=message,
            internal_status_code=internal_status_code,
            status_code=status_code,
        )


class NotFoundError(DatabaseError):
    def __init__(
        self,
        message: str,
        internal_status_code: InternalErrorEnum = InternalErrorEnum.INTERNAL_ERROR,
    ) -> None:
        super().__init__(
            message=message,
            internal_status_code=internal_status_code,
            status_code=status.HTTP_404_NOT_FOUND,
        )


class UniqueError(BaseError):
    def __init__(self, model_name: str) -> None:
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            message=f"Поля переданные в модель {model_name} содержат "
            f"неуникальные значения!",
        )
