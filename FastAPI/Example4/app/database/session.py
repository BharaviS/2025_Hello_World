from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from collections.abc import AsyncGenerator
from .database import engine

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autocommit=False, autoflush=False)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as db:
            yield db