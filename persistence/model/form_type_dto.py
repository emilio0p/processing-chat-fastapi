# FORM TYPE DTO

# Importaciones
from pydantic import BaseModel
from persistence.model.active_chat_dto import ActiveChatDTO

#Desarrollamos la clase base del DTO, con los atributos comunes
class FormTypeBaseDTO(BaseModel):
    form_name: str

#Desarrollamos la clase DTO y la configuramos para poder mostrarla en lectura
class FormTypeDTO(FormTypeBaseDTO):
    form_id: int
    form_type_chats: list[ActiveChatDTO]

    class Config:
        orm_mode = True