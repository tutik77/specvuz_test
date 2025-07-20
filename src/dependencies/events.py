from src.repositories.events import EventsRepository
from src.services.events import EventsService


def get_event_service() -> EventsService:
    return EventsService(EventsRepository)
