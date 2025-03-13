from fastapi import APIRouter, Request
from fastapi.openapi.utils import get_openapi
from starlette.responses import HTMLResponse
from app.api.utils.swagger.ui import get_swagger_ui_html

ROUTER = APIRouter()


@ROUTER.get(
    "/docs",
    include_in_schema=False,
)
async def custom_swagger_ui_html() -> HTMLResponse:
    """Генерация кастомного HTML для Swagger UI."""
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    )


@ROUTER.get("/openapi.json", include_in_schema=False)
async def get_custom_openapi(request: Request) -> dict:
    """Получение OpenAPI схемы."""
    if not request.app.openapi_schema:
        request.app.openapi_schema = get_openapi(
            title=request.app.title,
            version=request.app.version,
            description=request.app.description,
            routes=request.app.routes,
        )

    return request.app.openapi_schema
