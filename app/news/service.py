from app.service.base import BaseService
from app.news.schema import SNews
from app.news.model import News
from app.database import db
from cassandra.query import SimpleStatement


class NewsService(BaseService):
    __keyspace__ = News.__keyspace__
    __table_name__ = News.__table_name__

    @classmethod
    async def find_all(cls, **filter_by) -> list:
        query = f"SELECT * FROM {cls.__keyspace__}.{cls.__table_name__}"
        result = await db.execute_async(SimpleStatement(query))

        news_list = []
        for row in result.all():
            news = SNews(
                id=row.id,
                title=row.title,
                subtitle=row.subtitle,
                body=row.body
            )
            news_list.append(news)

        return news_list

    @classmethod
    async def find_by_id(cls, model_id) -> object:
        query = f"SELECT * FROM {cls.__keyspace__}.{cls.__table_name__} WHERE id = %s"
        result = await db.execute_async(SimpleStatement(query), (model_id,))
        if row := result.one():
            return SNews(**row._asdict())
        return None
