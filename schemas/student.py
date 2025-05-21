from pydantic import  BaseModel
from typing import Optional


class Student (BaseModel):
    name : str
    email : str

class Teacher (BaseModel):
    name : str
    email : str


class Assignment (BaseModel):
    id : str
    student_name : str
    description : str
    filename : str
    teacher_comment : Optional[str] = None