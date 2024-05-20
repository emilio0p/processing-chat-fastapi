# Importaciones
from pydantic import BaseModel

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
    rol_id: int

    class Config:
        orm_mode = True