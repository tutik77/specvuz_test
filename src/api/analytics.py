from typing import List
from datetime import datetime

from fastapi import APIRouter, Depends, Query

from src.services.analytics import AnalyticsService
from src.dependencies.analytics import get_analytics_service


router = APIRouter()


@router.get("/analytics")
async def get_analytics(
    user_id: int,
    date_from: datetime,
    date_to: datetime,
    events: List[int] = Query(None),
    service: AnalyticsService = Depends(get_analytics_service),
):
    return await service.get_analytics(user_id, date_from, date_to, events)
