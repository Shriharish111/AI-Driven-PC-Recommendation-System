from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PC Recommendation Backend"
    env: str = "development"
    debug: bool = True
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()
