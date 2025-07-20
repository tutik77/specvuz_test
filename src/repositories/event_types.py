from src.models.event_types import EventTypes
from src.utils.repository import SQLAlchemyRepository


class EventTypesRepository(SQLAlchemyRepository):
    model = EventTypes
