from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    QR_CODE_EXPIRATION: int  # in seconds

    class Config:
        env_file = ".env"

settings = Settings()