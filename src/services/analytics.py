from datetime import datetime
from typing import Dict, List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_

from src.models.events import Events
from src.models.event_types import EventTypes


class AnalyticsService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_analytics(
        self,
        user_id: int,
        date_from: datetime,
        date_to: datetime,
        events: Optional[List[int]] = None,
    ) -> Dict[str, int]:
        stmt = (
            select(EventTypes.name, func.count().label("count"))
            .join(Events, Events.event_type_id == EventTypes.id)
            .where(
                and_(
                    Events.user_id == user_id,
                    Events.event_date >= date_from,
                    Events.event_date <= date_to,
                )
            )
            .group_by(EventTypes.name)
        )

        if events:
            stmt = stmt.where(Events.event_type_id.in_(events))

        result = await self.session.execute(stmt)
        analytics = dict(result.all())

        return analytics
