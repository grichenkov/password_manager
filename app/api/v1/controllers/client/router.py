from fastapi import APIRouter

from app.api.v1.controllers.client.password import ROUTER as PASSWORD_ROUTER

ROUTER = APIRouter()

ROUTER.include_router(
    PASSWORD_ROUTER, prefix="/password", tags=["Password Manager"]
)
