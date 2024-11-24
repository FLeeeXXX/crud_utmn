from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid


class NewsType(Model):
    __keyspace__ = 'news'
    __table_name__ = 'news_types'

    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text(required=True)
