from fastapi import APIRouter

from database import teachers
from schemas.student import Teacher

teacher_router = APIRouter ()

@teacher_router.post("/teacher")
def register_teacher (user : Teacher):
    create_teacher = user.model_dump()
    teachers.append(create_teacher)
    return {"message" : "Registration completed", "data" : create_teacher}