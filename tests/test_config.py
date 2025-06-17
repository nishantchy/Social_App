from app.config import Settings

class TestSettings(Settings):
    DATABASE_URL: str = "sqlite:///./test.db"
    
    class Config:
        env_file = None

test_settings = TestSettings() 