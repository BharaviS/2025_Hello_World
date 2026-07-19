from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class StudentCreate(BaseModel):
    name: str
    email: str
    password: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    sid: int
    name: str
    email: str

class StudentsList(BaseModel):
    message: Optional[str] = None
    students: List[StudentResponse]