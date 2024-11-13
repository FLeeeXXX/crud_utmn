import uuid
from app.news.schema import SNews, SNewsView
from app.news.service import NewsService
from app.utils import secure_request


@secure_request
async def get_news(news_id: uuid.UUID | None = None):
    if news_id:
        news_id = uuid.UUID(str(news_id).strip())
        news_list = await NewsService.find_by_id(news_id)
    else:
        news_list = await NewsService.find_all()
    return news_list


@secure_request
async def create_news(news: SNewsView):
    await NewsService.add(
        title=news.title,
        subtitle=news.subtitle,
        body=news.body
    )


@secure_request
async def update_news(news: SNews):
    await NewsService.change_by_id(
        model_id=news.id,
        title=news.title,
        subtitle=news.subtitle,
        body=news.body
    )


@secure_request
async def delete_news(news_id: uuid.UUID):
    await NewsService.delete_by_id(news_id)
