# Importaciones
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from persistence.model.message import Message
from persistence.model.message_dto import MessageAddDTO
from persistence.model.message import Message

# Función obtener rol_id
def select_all_messages(db:Session):
    return db.query(Message).all()

def insert_message(message: MessageAddDTO, db: Session):
   db_message = Message(
        chat_id = message.chat_id,
        user_id = message.user_id,
        content = message.content
   )
   try:
        db.add(db_message)
        db.commit()
        db.refresh(db_message)
        return db_message
   
   except SQLAlchemyError as e:
           raise HTTPException(status_code=409, detail=str(e))