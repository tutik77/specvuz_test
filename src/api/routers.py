from fastapi import APIRouter

from src.api.event_types import router as types_router
from src.api.events import router as events_router
from src.api.analytics import router as analytics_router

router = APIRouter()
router.include_router(types_router, tags=["types"])
router.include_router(events_router, tags=["events"])
router.include_router(analytics_router, tags=["analytics"])
