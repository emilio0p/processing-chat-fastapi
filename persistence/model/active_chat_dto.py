# FORM TYPE DTO

# Importaciones
from pydantic import BaseModel

#Desarrollamos la clase base del DTO, con los atributos comunes
class ActiveChatBaseDTO(BaseModel):
    chat_name: str

#Desarrollamos la clase DTO y la configuramos para poder mostrarla en lectura
class ActiveChatDTO(ActiveChatBaseDTO):
    chat_id: int
    client_id:int
    admin_id: int
    form_id: int

    class Config:
        orm_mode = True