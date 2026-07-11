from sqlalchemy.orm import Mapped, mapped_column
from datetime import date, datetime
from ..database.base import Base

class StudentHeader(Base):
    __tablename__ = "student_header"

    sid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    dob: Mapped[date] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False)
    father_name: Mapped[str] = mapped_column(nullable=False)
    mother_name: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)