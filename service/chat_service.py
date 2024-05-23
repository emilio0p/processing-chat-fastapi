# Importaciones
from sqlalchemy.orm import Session
from fastapi import HTTPException

from persistence.repository.chat_repository import select_all_chats, select_chat_by_id, insert_chat
from persistence.repository.status_repository import select_status_by_name
from persistence.model.active_chat_dto import ActiveChatAddDTO

# Llamadas a las funciones del repositorio
def search_all_chats(db: Session):
    return select_all_chats(db)

def search_chat_by_id(chat_id: int, db: Session):
    db_chat = select_chat_by_id(chat_id, db)
    if not db_chat:
        raise HTTPException(status_code=404, detail="Chat no encontrado")
    
    return db_chat 

def save_chat(chat: ActiveChatAddDTO, db: Session):
    db_status = select_status_by_name("Pruebas - Creado", db)
    if not db_status:
        raise HTTPException(status_code=400, detail="ERROR: El estado a asignar no es correcto")
    
    return insert_chat(chat, db_status.status_id, db)