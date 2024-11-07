from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/news",
    tags=["News"]
)


@router.get('/get')
async def get_news(id: int):
    pass


@router.post('/create')
async def create_news(title: str, subtitle: str, body: str):
    pass


@router.put('/update')
async def update_news(id: int):
    pass


@router.delete('/delete')
async def delete_news(id: int):
    pass