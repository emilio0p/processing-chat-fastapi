# Importaciones
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from connection.connect import Base
from pydantic import BaseModel

# Entidad modelada User
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(40))
    password = Column(String(60))
    phone = Column(String(20))
    rol = Column(String)


# Entidad DTO User Base
class UserBaseDTO(BaseModel):
    username: str
    email: str
    phone: str

# Entidad DTO User Add
class UserAddDTO(UserBaseDTO):
    password: str
    rol: str

# Entidad DTO User
class UserDTO(UserBaseDTO):
    user_id: int
    
    class Config:
        orm_mode = True