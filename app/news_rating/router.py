from fastapi import APIRouter
import uuid
from app.news.schema import SNews
from app.news_rating.service import NewsRatingService
from app.news.utils import get_news


router = APIRouter(
    prefix="/news/rating",
    tags=["NewsRating"]
)


@router.post('/add')
async def get_types(news_id: uuid.UUID, rating: float) -> SNews:
    await NewsRatingService.add_rating(
        news_id=news_id,
        rating=rating
    )

    return await get_news(news_id)
