from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CASSANDRA_HOST: str
    CASSANDRA_PORT: int
    CASSANDRA_CLUSTER_NAME: str
    CASSANDRA_DC: str
    CASSANDRA_RACK: str
    CASSANDRA_SEEDS: str
    CASSANDRA_USERNAME: str
    CASSANDRA_PASSWORD: str

    class Config:
        env_file = '.env'


settings = Settings()
