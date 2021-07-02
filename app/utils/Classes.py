from typing import List, Optional
from pydantic import BaseModel

class Users(BaseModel):
    name: Optional[str]
    email: Optional[str]
    password: Optional[str] = None
    login_type: Optional[str]
    username: Optional[str]
    badges: Optional[List] = None
    prefered_technologies: Optional[List] = None
    profile_pic: Optional[str] = ""

class Technology(BaseModel):
    name: str

class Progress(BaseModel):
    percentage: int
    user: Users
    technology: Technology

class Questions(BaseModel):
    answers: List[str]
    image: str
    level: int
    technology: int
    question: str
    right_answer: str
    password: str