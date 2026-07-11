from sqlalchemy.orm import sessionmaker, Session
from collections.abc import Generator
from .database import engine

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()