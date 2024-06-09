# Importaciones
from sqlalchemy.orm import Session
from fastapi import HTTPException

from persistence.repository.chat_repository import select_all_chats, select_chat_by_id, insert_chat, delete_chat, select_chat_by_client, select_chat_by_admin, update_chat
from persistence.repository.status_repository import select_status_by_name
from persistence.model.active_chat_dto import ActiveChatAddDTO, ActiveChatStatusDTO
from service.auth_service import current_user
from persistence.repository.form_repository import select_all_forms

# Llamadas a las funciones del repositorio
def search_all_chats(db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    return select_all_chats(db)

def search_chat_by_id(chat_id: int, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")

    db_chat = select_chat_by_id(chat_id, db)
    if not db_chat:
        raise HTTPException(status_code=404, detail="Chat no encontrado")
    
    return db_chat 

def save_chat(chat: ActiveChatAddDTO, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    db_status = select_status_by_name("Creado", db)
    if not db_status:
        raise HTTPException(status_code=400, detail="ERROR: El estado a asignar no es correcto")
    
    return insert_chat(chat, db_status.status_id, db)

def remove_chat(chat_id: int, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    if user_db.rol_id == 1 :
        return delete_chat(search_chat_by_id(chat_id, db, token), db)
    else: raise HTTPException(status_code=401, detail="ERROR: No estás autorizado") 

def search_chat_by_client(client_id: int, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    db_chat = select_chat_by_client(client_id, db)
    if not db_chat:
        raise HTTPException(status_code=404, detail="Chat no encontrado")
    
    return db_chat 

def search_chat_by_admin(admin_id: int, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    db_chat = select_chat_by_admin(admin_id, db)
    if not db_chat:
        raise HTTPException(status_code=404, detail="Chat no encontrado")
    
    return db_chat 

def search_form_types(db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    return select_all_forms(db)

def replace_chat(chat_id: int,chat:ActiveChatStatusDTO, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    db_chat = search_chat_by_id(chat_id, db, token)
    if not db_chat:
        raise HTTPException(status_code=404, detail="Chat no encontrado")

    return update_chat(db_chat, chat, db)