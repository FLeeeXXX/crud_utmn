from faker import Faker
from app.news_types.service import NewsTypes
import asyncio

fake = Faker()


async def seed_news_types(count=5):
    for _ in range(count):
        name = fake.word()
        await NewsTypes.add(name=name)

if __name__ == "__main__":
    asyncio.run(seed_news_types(5))