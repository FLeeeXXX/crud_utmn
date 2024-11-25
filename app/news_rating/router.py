from fastapi import APIRouter
import uuid
from app.news.schema import SNews
from app.news_rating.service import NewsRatingService
from app.news.utils import get_news
from app.news_rating.schema import SRating


router = APIRouter(
    prefix="/news/rating",
    tags=["NewsRating"]
)


@router.post('/add')
async def add_rating(news_rating: SRating) -> SNews:
    await NewsRatingService.add_rating(
        news_id=news_rating.id,
        rating=news_rating.rating
    )

    return await get_news(news_rating.id)
