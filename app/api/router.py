from fastapi import APIRouter
from starlette import status

from app.api.utils.swagger.default_response import get_responses
from app.api.utils.swagger.docs import ROUTER as DOCS_ROUTER
from app.api.v1.router import ROUTER as API_ROUTER

ROUTER = APIRouter(
    responses=get_responses([status.HTTP_422_UNPROCESSABLE_ENTITY])
)

ROUTER.include_router(API_ROUTER, prefix="/api/v1")
ROUTER.include_router(DOCS_ROUTER)
