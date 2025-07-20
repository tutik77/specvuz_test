from pydantic import BaseModel


class EventTypeSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
