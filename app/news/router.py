from fastapi import APIRouter, Depends, HTTPException
from app.news.schema import SNews
from app.news.service import NewsService
import uuid

router = APIRouter(
    prefix="/news",
    tags=["News"]
)


@router.get('/get')
async def get_news(news_id: uuid.UUID | None = None):
    try:
        if news_id:
            news_id = uuid.UUID(str(news_id).strip())
            news_list = await NewsService.find_by_id(news_id)
        else:
            news_list = await NewsService.find_all()
        return news_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/create')
async def create_news(news: SNews) -> str:
    try:
        await NewsService.add(
            title=news.title,
            subtitle=news.subtitle,
            body=news.body
        )
        return "ok"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put('/update')
async def update_news(id: int):
    pass


@router.delete('/delete')
async def delete_news(id: int):
    pass