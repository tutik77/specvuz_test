from src.repositories.event_types import EventTypesRepository
from src.services.event_types import EventTypesService


def get_types_service() -> EventTypesService:
    return EventTypesService(EventTypesRepository)
