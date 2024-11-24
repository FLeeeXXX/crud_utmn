from app.database import db
from app.service.base import BaseService
from app.news_rating.model import NewsRating
from app.news.model import News
from cassandra.query import SimpleStatement
import uuid


class NewsRatingService(BaseService):
    __keyspace__ = NewsRating.__keyspace__
    __table_name__ = NewsRating.__table_name__
    __news_keyspace__ = News.__keyspace__
    __news_table_name__ = News.__table_name__

    @classmethod
    async def add_rating(cls, news_id: uuid.UUID, rating: float):
        id = uuid.uuid4()

        insert_query = f"INSERT INTO {cls.__keyspace__}.{cls.__table_name__} (id, news_id, rating) VALUES (%s, %s, %s)"
        await db.execute_async(SimpleStatement(insert_query), (id, news_id, rating))

        avg_query = f"SELECT AVG(rating) AS avg_rating FROM {cls.__keyspace__}.{cls.__table_name__} WHERE news_id = %s ALLOW FILTERING"
        result = await db.execute_async(SimpleStatement(avg_query), (news_id,))

        avg_rating = result.one().avg_rating

        update_query = f"UPDATE {cls.__news_keyspace__}.{cls.__news_table_name__} SET rating = %s WHERE id = %s"
        await db.execute_async(SimpleStatement(update_query), (avg_rating, news_id))
