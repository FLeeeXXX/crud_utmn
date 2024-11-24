from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
import uuid
import datetime


class NewsRating(Model):
    __keyspace__ = 'news'
    __table_name__ = 'news_ratings'

    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    news_id = columns.UUID(required=True)
    rating = columns.Double(required=True)
