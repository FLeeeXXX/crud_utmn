from faker import Faker
from app.news.service import NewsService
from app.news_types.service import NewsTypes
import asyncio
import random

fake = Faker()


async def seed_news(count=5):
    news_types = await NewsTypes.find_all()
    news_type_ids = [news_type.id for news_type in news_types]

    for _ in range(count):
        title = fake.sentence(nb_words=6)
        subtitle = fake.sentence(nb_words=10)
        body = fake.paragraph(nb_sentences=5)
        type_id = random.choice(news_type_ids)

        await NewsService.add(
            title=title,
            subtitle=subtitle,
            body=body,
            type=type_id
        )


if __name__ == "__main__":
    asyncio.run(seed_news(100))
