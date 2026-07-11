from pydantic import BaseModel
from typing import List

class Students(BaseModel):
    sid: int
    name: str
    age: int
    email: str

class StudentResponse(BaseModel):
    message: str
    students: Students | List[Students]