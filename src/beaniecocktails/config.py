from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mongo_server: str
    mongo_port: int
    mongo_database: str
    mongo_username: str
    mongo_password: str

    model_config = SettingsConfigDict(env_file=".env")
