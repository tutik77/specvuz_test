from typing import Annotated
from fastapi import APIRouter, Depends

from src.schemas.event_types import EventTypeSchema
from src.services.event_types import EventTypesService
from src.dependencies.event_types import get_types_service


router = APIRouter()


@router.post("/types")
async def add_type(
    event_type: EventTypeSchema,
    service: Annotated[EventTypesService, Depends(get_types_service)],
):
    return await service.add_event_type(event_type)


@router.get("/types")
async def get_types(service: EventTypesService = Depends(get_types_service)):
    return await service.get_all_event_types()
