from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid


class Comment(Model):
    __keyspace__ = 'news'
    __table_name__ = 'comments'

    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    news_id = columns.UUID(required=True)
    body = columns.Text(required=True)
