# Importaciones
from sqlalchemy.orm import Session
from fastapi import HTTPException

from persistence.repository.chat_repository import select_all_chats, select_chat_by_id

# Llamadas a las funciones del repositorio
def search_all_chats(db: Session):
    return select_all_chats(db)

def search_chat_by_id(chat_id: int, db: Session):
    db_chat = select_chat_by_id(chat_id, db)
    if not db_chat:
        raise HTTPException(status_code=404, detail="Chat no encontrado")
    
    return db_chat 