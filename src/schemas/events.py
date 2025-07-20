from datetime import datetime
from pydantic import BaseModel


class EventSchema(BaseModel):
    event_id: int
    user_id: int
    event_date: datetime
    event_type_id: int

    class Config:
        from_attributes = True


class EventSchemaAdd(BaseModel):
    user_id: int
    event_date: datetime
    event_type_id: int
