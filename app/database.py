import asyncio
from cassandra.cluster import Cluster, ExecutionProfile
from cassandra.auth import PlainTextAuthProvider
from cassandra.concurrent import execute_concurrent_with_args
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
        profile = ExecutionProfile()
        self.cluster = Cluster(
            [settings.CASSANDRA_HOST],
            port=settings.CASSANDRA_PORT,
            auth_provider=auth_provider,
            execution_profiles={"default": profile}
        )
        self.session = self.cluster.connect(settings.CASSANDRA_CLUSTER_NAME)

    async def execute_async(self, query, parameters=None):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.session.execute, query, parameters)

    async def execute_concurrent_async(self, query, parameters_list):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None,
            execute_concurrent_with_args,
            self.session,
            query,
            parameters_list
        )

    def close(self):
        self.cluster.shutdown()


db = Database()
