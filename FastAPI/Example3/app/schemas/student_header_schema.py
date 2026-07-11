from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class StudentCreate(BaseModel):
    name: str
    age: int
    dob: date
    gender: str
    phone: str
    email: str
    father_name: str
    mother_name: str
    password: str
    status: str

class StudentResponse(BaseModel):
    sid: int
    name: str
    age: int
    dob: date
    gender: str
    phone: str
    email: str
    father_name: str
    mother_name: str
    status: str
    created_at: datetime
    updated_at: datetime

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    status: Optional[str] = None