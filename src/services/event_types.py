from typing import List
from src.schemas.event_types import EventTypeSchema
from src.utils.repository import AbstractRepository


class EventTypesService:
    def __init__(self, event_types_repo: AbstractRepository):
        self.event_types_repo = event_types_repo()

    async def add_event_type(self, event_type: EventTypeSchema) -> None:
        event_type_dict = event_type.model_dump()
        event_type_id = await self.event_types_repo.add_one(event_type_dict)

        return event_type_id

    async def get_all_event_types(self) -> List[dict]:
        return await self.event_types_repo.get_all()
