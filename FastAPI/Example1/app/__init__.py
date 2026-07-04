from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

STUDENTS = {1: {"sid": 1, "name": "Bharavi", "email": "baravi@mail.com"},
            2: {"sid": 2, "name": "Bharani", "email": "bharani@mail.com"},}

COURSES = {1: {"title": "Python", "content": "Python is a powerful, high-level programming language used for web development, automation, data science, artificial intelligence, and scripting."},
           2: {"title": "Java", "content": "Java is an object-oriented programming language widely used for enterprise applications, Android development, desktop software, and backend systems."},
           3: {"title": "JavaScript", "content": "JavaScript is the programming language of the web, used to create interactive websites, dynamic user interfaces, and full-stack applications."},
           4: {"title": "HTML", "content": "HTML (HyperText Markup Language) is the standard markup language used to structure and display content on web pages."},
           5: {"title": "CSS", "content": "CSS (Cascading Style Sheets) is used to style and design web pages by controlling colors, layouts, fonts, animations, and responsiveness."},
           6: {"title": "React", "content": "React is a JavaScript library for building fast, reusable, and interactive user interfaces using a component-based architecture."},
           7: {"title": "Three.js", "content": "Three.js is a JavaScript library that enables developers to create and render interactive 3D graphics directly in web browsers using WebGL."},
           8: {"title": "YAML", "content": "YAML (YAML Ain't Markup Language) is a human-readable data serialization format commonly used for configuration files and DevOps tools."},
           9: {"title": "MySQL", "content": "MySQL is a popular relational database management system used to store, manage, and retrieve structured data using SQL."},
           10: {"title": "MongoDB", "content": "MongoDB is a NoSQL document database that stores data in flexible JSON-like documents, making it ideal for scalable modern applications."}}

class Student(BaseModel):
    sid: int
    name: str
    email: str

class Course(BaseModel):
    title: str
    content: str


@app.get("/")
def index():
    return {"message": "Welcome to FastAPI"}

@app.get("/about")
def about():
    return {"course": "FastAPI", "trainer": "Major Siri", "student": "Cadet Bharavi"}

@app.get("/student")
def get_students():
    return STUDENTS

@app.get("/student/{student_id}")
def get_student(student_id: int):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message":"Student found", "student": STUDENTS[student_id]}

@app.get("/course")
def get_all_courses(limit: int | None = None):
    if limit is not None:
        return list(COURSES.values())[:limit]
    return COURSES

@app.get("/course/{course_id}")
def get_course(course_id: int):
    if course_id not in COURSES:
        raise HTTPException(status_code=404, detail="Course not found")

    return {"message": "course found","course": COURSES[course_id]}

# Post methods

@app.post("/student")
def create_student(student: Student):
    if student.sid in STUDENTS:
        raise HTTPException(status_code=409, detail="Student already exists")

    STUDENTS[student.sid] = {"sid": student.sid, "name": student.name, "email": student.email}

    return {"message": "Student created successfully", "student": STUDENTS[student.sid]}

@app.put("/student/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")

    STUDENTS[student.sid] = {"sid": student.sid, "name": student.name, "email": student.email}

    return {"message": "Student updated successfully", "student": STUDENTS[student.sid]}

@app.delete("/student/{student_id}")
def delete_student(student_id: int):
    if student_id not in STUDENTS:
        raise HTTPException(status_code=404, detail="Student not found")

    deleted_student = STUDENTS.pop(student_id)

    return {"message": "Student deleted successfully", "student": deleted_student}