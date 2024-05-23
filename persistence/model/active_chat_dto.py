# FORM TYPE DTO

# Importaciones
from pydantic import BaseModel
from typing import Optional
from persistence.model.user_dto import UserDTO
from persistence.model.form_type_dto import FormTypeBaseDTO 
from persistence.model.chat_status_dto import ChatStatusBaseDTO 

#Desarrollamos la clase base del DTO, con los atributos comunes

class ActiveChatAddDTO(BaseModel):
    client_id: int
    admin_id: int
    form_id: int


#Desarrollamos la clase DTO y la configuramos para poder mostrarla en lectura
class ActiveChatDTO(ActiveChatAddDTO):
    chat_id: int
    chat_name: str
    chat_user_admin: Optional[UserDTO]
    chat_user_client: Optional[UserDTO]
    chat_form_type: Optional[FormTypeBaseDTO]
    chat_chat_status: Optional[ChatStatusBaseDTO]

    class Config:
        orm_mode = True