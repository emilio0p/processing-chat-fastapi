# Importaciones
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from persistence.model.active_chat_dto import ActiveChatDTO
from persistence.model.user_dto import UserDTO

#Vamos a desarrollar el objeto de transferencia de datos

# Entidad DTO User Add
class MessageAddDTO(BaseModel):
    chat_id: int
    user_id: int
    content: str


# Entidad DTO User
class MessageDTO(MessageAddDTO):
    message_id: int
    message_chat: Optional[ActiveChatDTO]
    message_user: Optional[UserDTO]

    class Config:
        orm_mode = True