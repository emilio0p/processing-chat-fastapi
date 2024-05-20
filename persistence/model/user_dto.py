# Importaciones
from pydantic import BaseModel
from typing import Optional
from persistence.model.rol_dto import RolDTO

#Vamos a desarrollar el objeto de transferencia de datos

# Entidad DTO User Base
class UserBaseDTO(BaseModel):
    username: str
    email: str
    phone: str

# Entidad DTO User Add
class UserAddDTO(UserBaseDTO):
    password: str


# Entidad DTO User
class UserDTO(UserBaseDTO):
    user_id: int
    user_rol: Optional[RolDTO]

    class Config:
        orm_mode = True