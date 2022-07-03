from models import User, sexe, Role
from uuid import uuid4, UUID
from typing import List
from fastapi import FastAPI

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
        id=uuid4(),
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


@app.