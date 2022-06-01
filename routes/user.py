from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
key = Fernet.generate_key()
f = Fernet(key)
user = APIRouter()

@user.get("/users", response_model=list[User], tags=["users"])
def get_users():
    return conn.execute(users.select()).fetchall()
@user.post("/users", response_model=User, )
def create_user(user: User):
    new_user = {
        "name": user.name, 
        "email": user.email,  
    }
    new_user["password"] = f.encrypt(user.password.encode("utf-8 "))
    result  = conn.execute(users.insert().values(new_user))
    isEqual2Last = users.c.id == result.lastrowid
    return conn.execute(users.select().where(isEqual2Last)).first()

    
@user.get("/users/{id}", tags=["users"])
def get_user(id: str):
    isEqual2Id = users.c.id == id
    return conn.execute(users.select().where(isEqual2Id)).first()

@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: str):
    isEqual2Id = users.c.id == id
    result = conn.execute(users.delete().where(isEqual2Id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}", response_model=User)
def update_user(id: str, user: User):
    isEqual2Id = users.c.id == id
    conn.execute(
        users.update().values(
            name = user.name,
            email = user.email,
            password = f.encrypt(user.password.encode("utf-8"))
        ).where(isEqual2Id)
    )
    return conn.execute(users.select().where(isEqual2Id)).first()
    
