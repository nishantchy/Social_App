from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

# Check if we're running tests
if os.getenv("PYTEST_CURRENT_TEST"):
    from tests.test_config import test_settings
    settings = test_settings
else:
    settings = Settings()