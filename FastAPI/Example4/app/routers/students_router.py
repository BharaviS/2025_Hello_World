from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.repositories import StudentRepository
from app.schemas import StudentCreate, StudentResponse, StudentUpdate

router = APIRouter()

@router.post("/students", response_model=StudentResponse)
async def create_student(student: StudentCreate, db: AsyncSession = Depends(get_db)):
    repository = StudentRepository(db=db)

    return await repository.create_student(student)

@router.get("/students", response_model=list[StudentResponse])
async def get_students(limit: int | None=None , db: AsyncSession = Depends(get_db)):
    repository = StudentRepository(db=db)

    return await repository.get_students(limit=limit)

@router.get("/students/{sid}", response_model=StudentResponse)
async def get_student(sid: int, db: AsyncSession = Depends(get_db)):
    repository = StudentRepository(db=db)

    return await repository.get_student_by_id(sid=sid)

@router.patch("/students/{sid}", response_model=StudentResponse)
async def update_student(sid: int, student: StudentUpdate, db: AsyncSession = Depends(get_db)):
    repository = StudentRepository(db=db)

    return await repository.update_student(sid=sid, students_data=student)

@router.delete("/students/{sid}")
async def delete_student(sid: int, db: AsyncSession = Depends(get_db)):
    repository = StudentRepository(db=db)
    await repository.delete_student(sid=sid)

    return {"message": "Student deleted successfully"}
