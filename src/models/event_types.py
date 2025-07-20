from sqlalchemy.orm import Mapped, mapped_column

from src.database.database import Base


class EventTypes(Base):
    __tablename__ = "event_types"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
