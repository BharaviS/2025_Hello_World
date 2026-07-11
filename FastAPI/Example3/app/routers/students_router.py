from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from ..models.student_header_model import StudentHeader
from ..schemas import StudentCreate, StudentResponse, StudentUpdate
from ..database.session import get_db

router = APIRouter()

@router.get("/students", response_model=List[StudentResponse])
def get_students(db: Session = Depends(get_db), limit: int | None = None):
    students = db.query(StudentHeader).all()

    if limit is not None:
        return students[:limit]

    return students

@router.get("/students/{sid}", response_model=StudentResponse)
def get_student(sid: int, db: Session = Depends(get_db)):
    student = db.query(StudentHeader).filter(StudentHeader.sid == sid).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student

@router.post("/students", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    student_db = StudentHeader(**student.model_dump())
    existing_student = db.query(StudentHeader).filter(StudentHeader.email == student.email).first()

    if existing_student:
        raise HTTPException(status_code=400, detail="Student already exists")

    db.add(student_db)
    db.commit()
    db.refresh(student_db)

    return student_db

@router.delete("/students/{sid}", response_model=StudentResponse)
def delete_student(sid: int, db: Session = Depends(get_db)):
    student = db.query(StudentHeader).filter(StudentHeader.sid == sid).first()

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return student

@router.put("/students/{sid}", response_model=StudentResponse)
def put_student(sid: int,student: StudentCreate, db: Session = Depends(get_db)):
    existing_student = db.query(StudentHeader).filter(StudentHeader.sid == sid).first()

    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.model_dump().items():
        setattr(existing_student, key, value)

    db.commit()
    db.refresh(existing_student)

    return existing_student

@router.patch("/students/{sid}", response_model=StudentResponse)
def update_student(sid: int, student: StudentUpdate, db: Session = Depends(get_db)):
    existing_student = db.query(StudentHeader).filter(StudentHeader.sid == sid).first()

    if not existing_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.model_dump(exclude_unset=True).items():
        setattr(existing_student, key, value)

    db.commit()
    db.refresh(existing_student)
    return existing_student