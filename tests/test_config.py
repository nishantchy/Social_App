import os
from app.config import Settings

class TestSettings(Settings):
    database_hostname: str = "localhost"
    database_port: str = "5432"
    database_password: str = "postgres"
    database_name: str = "postgres"
    database_username: str = "postgres"
    secret_key: str = "test_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    DATABASE_URL: str = "sqlite:///./test.db"
    
    class Config:
        env_file = None

test_settings = TestSettings()