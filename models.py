from typing import Optional, List
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum


class sexe(str, Enum):
    masculin = "homme"
    femminin = "femme"


class Role(str, Enum):
    admin = "Staff"
    user = "Utilisateur"
    helper = "helpeur"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    sexe: sexe
    roles: List[Role]