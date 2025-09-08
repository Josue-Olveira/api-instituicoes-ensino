from pydantic import BaseModel, EmailStr
from api.models.base import UserRole

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    role: UserRole = UserRole.LEITOR

class UserSchema(UserBase):
    id: int
    role: UserRole

    class Config:
        from_attributes = True