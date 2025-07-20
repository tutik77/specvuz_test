from typing import List
from src.schemas.events import EventSchemaAdd
from src.utils.repository import AbstractRepository


class EventsService:
    def __init__(self, events_repo: AbstractRepository):
        self.events_repo = events_repo()

    async def add_event(self, event: EventSchemaAdd) -> None:
        event_dict = event.model_dump()
        event_id = await self.events_repo.add_one(event_dict)

        return event_id

    async def get_all_events(self) -> List[dict]:
        return await self.events_repo.get_all()
