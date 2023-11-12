from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: Optional[int]
    name: str
    username: str
    password: str
    
    class Config:
        orm_mode = True

class DataUser(BaseModel):
    username: str
    password: str
