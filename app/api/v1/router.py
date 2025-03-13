from fastapi import APIRouter

from app.api.v1.controllers.client.router import ROUTER as CLIENT_ROUTER

ROUTER = APIRouter()

ROUTER.include_router(CLIENT_ROUTER)
