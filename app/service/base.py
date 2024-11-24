from app.database import db
import uuid
from cassandra.query import SimpleStatement


class BaseService:
    __keyspace__ = None
    __table_name__ = None

    @classmethod
    async def find_by_id(cls, model_id) -> object:
        query = f"SELECT * FROM {cls.__keyspace__}.{cls.__table_name__} WHERE id = %s"
        result = await db.execute_async(SimpleStatement(query), (model_id,))
        return result.one()

    @classmethod
    async def find_all(cls, **filter_by) -> list:
        query = f"SELECT * FROM {cls.__keyspace__}.{cls.__table_name__}"
        result = await db.execute_async(SimpleStatement(query), tuple(filter_by.values()))
        return result.all()

    @classmethod
    async def add(cls, **data) -> object:
        new_id = uuid.uuid4()
        data['id'] = new_id

        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {cls.__keyspace__}.{cls.__table_name__} ({columns}) VALUES ({placeholders})"

        await db.execute_async(SimpleStatement(query), tuple(data.values()))

        return await cls.find_by_id(new_id)

    @classmethod
    async def change_by_id(cls, model_id, **data) -> None:
        set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {cls.__keyspace__}.{cls.__table_name__} SET {set_clause} WHERE id = %s"
        await db.execute_async(SimpleStatement(query), tuple(data.values()) + (model_id,))

    @classmethod
    async def delete_by_id(cls, model_id) -> None:
        query = f"DELETE FROM {cls.__keyspace__}.{cls.__table_name__} WHERE id = %s"
        await db.execute_async(SimpleStatement(query), (model_id,))