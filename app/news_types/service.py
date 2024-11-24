from app.service.base import BaseService
from app.news_types.model import NewsType
from app.news_types.schema import SNewsTypes
from app.database import db
from cassandra.query import SimpleStatement


class NewsTypes(BaseService):
    __keyspace__ = NewsType.__keyspace__
    __table_name__ = NewsType.__table_name__

    @classmethod
    async def find_all(cls, **filter_by) -> list:
        query = f"SELECT * FROM {cls.__keyspace__}.{cls.__table_name__}"
        result = await db.execute_async(SimpleStatement(query))

        return [SNewsTypes(**row._asdict()) for row in result.all()]


    # @classmethod
    # async def find_by_id(cls, model_id) -> object:
    #     query = f"SELECT * FROM {cls.__keyspace__}.{cls.__table_name__} WHERE id = %s"
    #     result = await db.execute_async(SimpleStatement(query), (model_id,))
    #     if row := result.one():
    #         return SNews(**row._asdict())
    #     return None
