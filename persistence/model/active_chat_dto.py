# FORM TYPE DTO

# Importaciones
from pydantic import BaseModel
from typing import Optional
from persistence.model.user_dto import UserDTO
from persistence.model.form_type_dto import FormTypeDTO 

#Desarrollamos la clase base del DTO, con los atributos comunes
class ActiveChatBaseDTO(BaseModel):
    chat_name: str

#Desarrollamos la clase DTO y la configuramos para poder mostrarla en lectura
class ActiveChatDTO(ActiveChatBaseDTO):
    chat_id: int
    client_id:int
    chat_user_admin: Optional[UserDTO]
    chat_user_client: Optional[UserDTO]
    chat_form_type: Optional[FormTypeDTO]

    class Config:
        orm_mode = True