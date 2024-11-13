import uuid
from fastapi import APIRouter
from app.news.schema import SNewsView, SNews
from app.news.utils import (get_news as secure_get_news, create_news as secure_create_news,
                            update_news as secure_update_news, delete_news as secure_delete_news)


router = APIRouter(
    prefix="/news",
    tags=["News"]
)


@router.get('/get')
async def get_news(news_id: uuid.UUID | None = None) -> SNewsView | list[SNewsView]:
    return await secure_get_news(news_id)


@router.post('/create')
async def create_news(news: SNewsView) -> None:
    return await secure_create_news(news)


@router.put('/update')
async def update_news(news: SNews) -> None:
    return await secure_update_news(news)


@router.delete('/delete')
async def delete_news(news_id: uuid.UUID) -> None:
    await secure_delete_news(news_id)
