from app.news_types.schema import SNewsTypesView
from app.news_types.service import NewsTypes
from app.utils import secure_request


@secure_request
async def get_types():
    news_list = await NewsTypes.find_all()
    return news_list


@secure_request
async def create_type(news_type: SNewsTypesView):
    return await NewsTypes.add(
        name=news_type.name
    )
