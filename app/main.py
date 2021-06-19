from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from typing import List, Optional
from pydantic import BaseModel

import bcrypt

from app.core.config import settings

from app.utils.users import get_user, add_user, get_all_users, get_questions, update_user, delete_user
from app.utils.questions_formating import questions_formating
from app.utils.users_formating import user_format,users_format

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

if settings.ENVIRONMENT == "production":
    origins = [settings.CLIENT]
else:
    origins = [
        "http://localhost:3000",
        "http://localhost:8080",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### THIS CLASSES NEED TO BE IN A DIFFERENT FILE MY DUDE

class Users(BaseModel):
        name: str
        email: str
        password: str
        login_type: str
        username: str
        badges: Optional[List] = None
        prefered_technologies: Optional[List] = None


@app.post("/users/create")
async def POST_users(user: Users):

    hashed = bcrypt.hashpw(bytes(user.password, encoding='utf-8'),bcrypt.gensalt()) # THIS NEEDS TO BE A FUNCTION SOMEWHERE ELSE

    messege = add_user(user.name,user.email,hashed.decode("utf-8"),user.login_type,user.username)

    return {"response": messege}



@app.get("/user")
async def GET_user( username: str ):

    user = get_user(username)
    response = user_format(user[0])
    return {"response": response}



@app.get("/users")
async def GET_users():

    users = get_all_users()
    response = users_format(users)
    return {"response": response}



@app.put("/user/edit")
async def UPDATE_user(user: Users):

    messege = update_user(user.name, user.password, user.login_type, user.username, user.email, user.badges, user.prefered_technologies)

    return {"response": messege}



@app.delete("/user/delete")
async def DELETE_user(user: Users):

    messege = delete_user(user.email, user.username,)

    return {"response": messege}



@app.get("/questions")
async def GET_questions(
    technology: str,
    level: str,
    number_of_questions: int = 5,
):

    questions = get_questions(technology,level)
    if len(questions) < number_of_questions:
        raise HTTPException(status_code=400, detail="Sorry we don't have that many questions of this specific type")  
    response = questions_formating(questions,number_of_questions)
    return {"response": response}