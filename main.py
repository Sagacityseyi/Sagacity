from fastapi import FastAPI
from routers.student import student_router
from routers.teacher import teacher_router
from routers.assignment import assignment_router

app = FastAPI()

app.include_router(student_router)
app.include_router(teacher_router)
app.include_router(assignment_router)

@app.get ("/")
def home ():
    return {"message" : "Welcome to Assignment page"}