from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.analytics import AnalyticsService
from src.database.database import get_session


async def get_analytics_service(
    session: AsyncSession = Depends(get_session),
) -> AnalyticsService:
    return AnalyticsService(session)
