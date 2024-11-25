from fastapi import APIRouter
import uuid
from app.comments.schema import SCommentsInp, SComments
from app.comments.service import CommentsService


router = APIRouter(
    prefix="/news/comments",
    tags=["NewsComments"]
)


@router.get('/get')
async def get_comments(news_id: uuid.UUID) -> list[SComments]:
    return await CommentsService.find_by_id(
        news_id=news_id
    )


@router.post('/add')
async def add_comment(comment: SCommentsInp) -> None:
    await CommentsService.add(
        news_id=comment.news_id,
        body=comment.body
    )
