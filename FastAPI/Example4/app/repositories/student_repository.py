from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas import StudentCreate, StudentUpdate
from app.models import Student
from typing import cast

class StudentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_student(self, student: StudentCreate) -> Student:
        db_student = Student(**student.model_dump())
        stmt = select(Student).where(Student.email == db_student.email)
        result = await self.db.execute(stmt)
        existing_student = result.scalar_one_or_none()

        if existing_student:
            raise HTTPException(status_code=400, detail="Student already exists")

        self.db.add(db_student)
        await self.db.commit()
        await self.db.refresh(db_student)

        return db_student

    async def get_students(self, limit: int | None=None) -> list[Student]:
        stmt = select(Student)

        if limit is not None:
            stmt = stmt.limit(limit)

        result = await self.db.execute(stmt)
        students = cast(list[Student], result.scalars().all())

        return students

    async def get_student_by_id(self, sid: int) -> Student | None:
        stm = select(Student).where(Student.sid == sid)
        result = await self.db.execute(stm)
        student = result.scalar_one_or_none()

        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        return student

    async def update_student(self, sid: int, students_data: StudentUpdate) -> Student | None:
        stmt = select(Student).where(Student.sid == sid)
        result = await self.db.execute(stmt)
        student = result.scalar_one_or_none()

        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        for key, value in students_data.model_dump(exclude_unset=True).items():
            setattr(student, key, value)

        await self.db.commit()
        await self.db.refresh(student)

        return student

    async def delete_student(self, sid: int) -> None:
        stmt = select(Student).where(Student.sid == sid)
        result = await self.db.execute(stmt)
        student = result.scalar_one_or_none()

        if not student:
            raise HTTPException(status_code=404, detail="Student not found")

        await self.db.delete(student)
        await self.db.commit()
