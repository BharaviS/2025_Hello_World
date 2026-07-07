from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

STUDENTS = {1: {"sid": 1, "name": "Bharavi", "email": "bharavi@mail.com", "password": "1234567890", "fees": "10 000"},
            2: {"sid": 2, "name": "Bharani", "email": "bharani@mail.com", "password": "1234567890", "fees": "10500"},
            3: {"sid": 3, "name": "Ravi", "email": "ravi@mail.com", "password": "1234567890", "fees": "12000"}}

class Student(BaseModel):
    sid: int
    name: str
    email: str

class StudentResponse(BaseModel):
    message: str
    student: Student | List[Student]

@app.get("/")
def index():
    return {"message": "Hello World to FastAPI", "owner": "Bharavi"}

@app.get("/student", response_model=StudentResponse)
def get_students(limit: int | None = None):
    if limit is not None:
        return {"message": "Student found", "student":list(STUDENTS.values())[:limit]}

    return {"message": "Student found", "student": list(STUDENTS.values())}

@app.get("/student/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student found", "student": STUDENTS[student_id]}