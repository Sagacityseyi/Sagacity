from fastapi import APIRouter

from database import students
from schemas.student import Student

student_router = APIRouter()

@student_router.post("/")
def register_student(user : Student):
    create_student = user.model_dump()
    students.append(create_student)
    return {"message" : "Registration completed", "data" : create_student}

@student_router.get("/")
def get_students():
    return students