from app.database import db
from app.news_rating.model import NewsRating
from cassandra.query import SimpleStatement
import uuid


class NewsRatingService:
    @staticmethod
    async def add_rating(news_id: uuid.UUID, rating: int):
        # Добавляем новую оценку
        new_rating = NewsRating(news_id=news_id, rating=rating)
        new_rating.save()

        # Пересчитываем средний рейтинг
        query = "SELECT AVG(rating) AS avg_rating FROM news.news_ratings WHERE news_id = %s"
        result = await db.execute_async(SimpleStatement(query), (news_id,))
        avg_rating = result.one().avg_rating

        # Обновляем поле `rating` в таблице `News`
        update_query = "UPDATE news.news SET rating = %s WHERE id = %s"
        await db.execute_async(SimpleStatement(update_query), (avg_rating, news_id))
