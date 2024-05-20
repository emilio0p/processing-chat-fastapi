# ROLES DTO

# Importaciones
from pydantic import BaseModel

#Desarrollamos la clase base del DTO, con los atributos comunes
class RolBaseDTO(BaseModel):
    rol_name: str

#Desarrollamos la clase DTO y la configuramos para poder mostrarla en lectura
class RolDTO(RolBaseDTO):
    rol_id: int

    class Config:
        orm_mode = True