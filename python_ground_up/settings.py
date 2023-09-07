from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    db_driver: str = "postgresql"
    db_username: str
    db_password: str
    db_hostname: str
    db_port: int
    db_name: str
    db_echo: bool = False
    db_pool_size: int = 5
    db_max_overflow: int = 0

    @property
    def db_uri(self) -> str:
        # driver://username:password@hostname:port/database
        return f"{self.db_driver}://{self.db_username}:{self.db_password}@{self.db_hostname}:{self.db_port}/{self.db_name}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()