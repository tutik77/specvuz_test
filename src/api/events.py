from typing import Annotated
from fastapi import APIRouter, Depends

from src.dependencies.events import get_event_service
from src.schemas.events import EventSchemaAdd
from src.services.events import EventsService

router = APIRouter()


@router.post("/events")
async def add_event(
    event: EventSchemaAdd, service: Annotated[EventsService, Depends(get_event_service)]
):
    return await service.add_event(event)


@router.get("/events")
async def get_events(service: Annotated[EventsService, Depends(get_event_service)]):
    return await service.get_all_events()
