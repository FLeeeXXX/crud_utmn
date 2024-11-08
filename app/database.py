from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from app.config import settings


class DatabaseMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(DatabaseMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=DatabaseMeta):
    def __init__(self):
        auth_provider = PlainTextAuthProvider(settings.CASSANDRA_USERNAME, settings.CASSANDRA_PASSWORD)
        self.cluster = Cluster([settings.CASSANDRA_HOST], port=settings.CASSANDRA_PORT, auth_provider=auth_provider)
        self.session = self.cluster.connect(settings.CASSANDRA_CLUSTER_NAME)

    def close(self):
        self.cluster.shutdown()


db = Database()
