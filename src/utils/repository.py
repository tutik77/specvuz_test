from abc import ABC, abstractmethod
from typing import List

from sqlalchemy import insert, select


from src.database.database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
        return res.scalar_one()

    async def get_all(self) -> List[dict]:
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
        return res.scalars().all()
