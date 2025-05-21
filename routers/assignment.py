from schemas.student import Assignment
from typing import Annotated
from fastapi import APIRouter, Form, File, HTTPException, UploadFile


assignment_router = APIRouter()

@assignment_router.post ("/")
def submit_assignment (
        name : Annotated[str, Form()],
        subject : Annotated[str, Form()],
        description : Annotated[str, Form()],
        file : UploadFile = File(...)

):
    if name.students != name:
        raise HTTPException(status_code =404,detail= "Student not Registered" )

