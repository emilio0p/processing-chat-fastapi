# Importaciones
from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError 
from persistence.model.active_chat import ActiveChat
from persistence.model.active_chat_dto import ActiveChatAddDTO
from persistence.repository.status_repository import select_status_by_id
from persistence.repository.form_repository import select_form_by_id

# Función obtener todos los chats
def select_all_chats(db:Session):
    return db.query(ActiveChat).all()

# Función obtener chat por id
def select_chat_by_id(chat_id: int, db: Session):
 return db.query(ActiveChat).filter(ActiveChat.chat_id==chat_id).first()

# dasdasdsad
def insert_chat(chat: ActiveChatAddDTO, status: int, db: Session):
   
   form_selected = select_form_by_id(chat.form_id, db)
   if not form_selected:
        raise HTTPException(status_code=404, detail=f"No existe tipo de formulario con id: {chat.form_id}")

   status_selected = select_status_by_id(status, db)
   if not status_selected:
        raise HTTPException(status_code=404, detail=f"No existe estado con id: {status}")


   chat_name = f"{form_selected.form_name} - {status_selected.status_name}"

   db_chat = ActiveChat(chat_name=chat_name,
                        client_id=chat.client_id, 
                        admin_id=chat.admin_id, 
                        form_id=chat.form_id, 
                        status_id = status)
   
   try:
        db.add(db_chat)
        db.commit()
        db.refresh(db_chat)
        return db_chat
   except SQLAlchemyError as e:
           raise HTTPException(status_code=409, detail=str(e))
