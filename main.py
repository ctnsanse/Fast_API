from models import User, sexe, Role
from uuid import UUID
from typing import List
from fastapi import FastAPI, HTTPException

app = FastAPI()


db: List[User] = [
    User(
        id=UUID("d8c047b3-5acc-44cb-9a77-39ff8140bc88"),
        first_name = "Cleyton",
        last_name = "Sanse",
        sexe = sexe.masculin,
        roles = [Role.admin]
    ),
    User(
        id=("d8c047b3-5acc-44cb-9a77-39ff8140bc88"),
        first_name = "Duvensky",
        last_name = "Ozil",
        sexe = sexe.femminin,
        roles = [Role.user, Role.helper]
    )
]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
async def fetch_users():
    return db;


@app.post("/api/v1/users")
async def register_user(user: User): 
    db.append(user)
    return {"id" : user.id}

@app.delete("/api/v1/user/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code = 404,
        detail = "L'utilisateur de cet ID : {user_id} n'éxiste pas."
    )