from typing import Optional
from pydantic import BaseModel

class UserLoginCredential(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: str

    items: Optional[list] = []