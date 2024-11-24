import time
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster
from app.news.model import News
from app.comments.model import Comment
from app.news_types.model import NewsType
from app.news_rating.model import NewsRating
from app.config import settings


def create_keyspace():
    cluster = Cluster([settings.CASSANDRA_HOST])
    session = cluster.connect()
    session.execute(f"""
        CREATE KEYSPACE IF NOT EXISTS {settings.CASSANDRA_CLUSTER_NAME}
        WITH REPLICATION = {{ 'class': 'SimpleStrategy', 'replication_factor': 1 }}
    """)
    cluster.shutdown()


def run_migrations():
    while True:
        try:
            create_keyspace()
            connection.setup([settings.CASSANDRA_HOST], settings.CASSANDRA_CLUSTER_NAME, protocol_version=3)
            sync_table(News)
            sync_table(NewsType)
            sync_table(Comment)
            sync_table(NewsRating)
            break
        except Exception as e:
            print(f"Не удалось подключиться к Cassandra, повторная попытка через 5 секунд.\nОшибка: {e}")
            time.sleep(5)


if __name__ == "__main__":
    run_migrations()
