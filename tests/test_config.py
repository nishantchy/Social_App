from app.config import Settings
import os

class TestSettings(Settings):
    # Required fields with dummy values for Pydantic validation
    database_hostname: str = os.getenv("DATABASE_HOSTNAME", "localhost")
    database_port: int = int(os.getenv("DATABASE_PORT", "5432"))
    database_password: str = os.getenv("DATABASE_PASSWORD", "dummy")
    database_name: str = os.getenv("DATABASE_NAME", "dummy")
    database_username: str = os.getenv("DATABASE_USERNAME", "dummy")
    
    # Authentication settings
    secret_key: str = os.getenv("SECRET_KEY", "test-secret-key-for-testing-only")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    @property
    def DATABASE_URL(self) -> str:
        # Always use SQLite for testing
        return "sqlite:///./test.db"
    
    class Config:
        env_file = None

test_settings = TestSettings()