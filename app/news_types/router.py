from fastapi import APIRouter
from app.news_types.schema import SNewsTypesView
from app.news_types.utils import get_types as secure_get_types, create_type as secure_create_type


router = APIRouter(
    prefix="/news/types",
    tags=["NewsTypes"]
)


@router.get('/get')
async def get_types():
    return await secure_get_types()


@router.post('/add')
async def get_types(news_type: SNewsTypesView):
    return await secure_create_type(news_type)
