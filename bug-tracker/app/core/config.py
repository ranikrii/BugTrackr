from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Bug Tracker"
    SQLALCHEMY_DATABASE_URI: str
    SECRET_KEY: str = "CHANGE_ME"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    ALGORITHM: str = "HS256"
    
    SENTRY_DSN: str | None = None      # optional for local dev
    ENV: str = "local"                 # 'local' or 'production'
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()