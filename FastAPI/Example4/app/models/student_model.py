from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from ..database.base import Base

class Student(Base):
    __tablename__ = "student"

    sid: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(150), nullable=False)
