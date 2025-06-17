import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from urllib.parse import quote_plus

# Use DATABASE_URL if available (e.g., on Railway)
DATABASE_URL = os.getenv("DATABASE_URL")

if os.getenv("TESTING") or os.getenv("PYTEST_CURRENT_TEST"):
    # Use SQLite for testing
    SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
elif DATABASE_URL:
    # Use Render-provided URL
    SQLALCHEMY_DATABASE_URL = DATABASE_URL
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    # Use local PostgreSQL config
    encoded_password = quote_plus(settings.database_password)
    SQLALCHEMY_DATABASE_URL = (
        f"postgresql://{settings.database_username}:{encoded_password}"
        f"@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
    )
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
