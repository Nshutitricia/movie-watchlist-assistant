from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    anthropic_api_key: str
    claude_model: str = "claude-haiku-4-5"
    database_url: str = "sqlite:///data/watchlist.db"

    class Config:
        env_file = ".env"


settings = Settings()