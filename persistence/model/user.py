from sqlalchemy import Column, Integer, String
from connection.connect import Base
from pydantic import BaseModel

# Entidad User
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(40))
    password = Column(String(60))
    phone = Column(String(20))
    rol = Column(String)

# DTO User
class UserBaseDTO(BaseModel):
    username: str
    email: str
    phone: str

class UserAddDTO(UserBaseDTO):
    password: str
    rol: str

class UserDTO(UserBaseDTO):
    user_id: int
    
    class Config:
        orm_mode = True