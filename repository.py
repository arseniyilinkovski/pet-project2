from database import new_session, ItemsOrm
from schemas import ItemsAdd, Items
from sqlalchemy import select


class ItemsRepository:
    @classmethod
    async def add_one(cls, data: ItemsAdd) -> int:
        async with new_session() as session:
            items_dict = data.model_dump()
            item = ItemsOrm(**items_dict)
            session.add(item)
            await session.flush()
            await session.commit()
            return item.id

    @classmethod
    async def find_all(cls) -> list[Items]:
        async with new_session() as session:
            query = select(ItemsOrm)
            result = await session.execute(query)
            item_model = result.scalars().all()
            return item_model

    @classmethod
    async def find_task(cls, name: str, data: ItemsAdd):
        async with new_session() as session:
            items_dict = data.model_dump()
