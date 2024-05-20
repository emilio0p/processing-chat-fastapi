# CHAT STATUS DTO

# Importaciones
from pydantic import BaseModel

#Desarrollamos la clase base del DTO, con los atributos comunes
class ChatStatusBaseDTO(BaseModel):
    status_name: str

#Desarrollamos la clase DTO y la configuramos para poder mostrarla en lectura
class ChatStatusDTO(ChatStatusBaseDTO):
    status_id: int

    class Config:
        orm_mode = True