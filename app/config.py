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

    # @property
    # def DATABASE_URL(self):
    #     return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = '.env'


settings = Settings()
