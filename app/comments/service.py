from app.service.base import BaseService
from app.comments.model import Comment
from cassandra.query import SimpleStatement
from app.database import db
from app.comments.schema import SComments


class CommentsService(BaseService):
    __keyspace__ = Comment.__keyspace__
    __table_name__ = Comment.__table_name__

    @classmethod
    async def find_by_id(cls, news_id) -> list[SComments]:
        query = f"SELECT * FROM {cls.__keyspace__}.{cls.__table_name__} WHERE news_id = %s ALLOW FILTERING"
        result = await db.execute_async(SimpleStatement(query), (news_id,))
        rows = result.all()
        return [SComments(**row._asdict()) for row in rows]
