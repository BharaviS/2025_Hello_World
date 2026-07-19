from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.engine import Connection
from app.config import Config
from .base import Base
from app.models import Student

engine = create_async_engine(Config.DATABASE_URL)

def create_tables(connection: Connection):
    Base.metadata.create_all(bind=connection)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(create_tables)