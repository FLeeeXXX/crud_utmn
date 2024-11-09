from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid


class News(Model):
    __keyspace__ = 'news'
    __table_name__ = 'news'

    id = columns.UUID(primary_key=True, default=uuid.uuid4, required=False)
    title = columns.Text(required=True)
    subtitle = columns.Text(required=True)
    body = columns.Text(required=True)
