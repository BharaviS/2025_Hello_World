from sqlalchemy import create_engine
from .base import Base
from ..config import Config
from ..models import student_header_model

engine = create_engine(Config.DATABASE_URL)

def init_db():
        Base.metadata.create_all(bind=engine)