# Importaciones
from fastapi import HTTPException
from sqlalchemy.orm import Session
from service.auth_service import current_user
from persistence.repository.message_repository import select_all_messages, insert_message
from persistence.model.message_dto import MessageAddDTO

# Llamadas a las funciones del repositorio
def search_all_messages(db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    return select_all_messages(db)

def save_chat(message: MessageAddDTO, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    return insert_message(message, db)