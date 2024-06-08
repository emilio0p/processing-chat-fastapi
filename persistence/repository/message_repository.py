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
           raise HTTPException(status_code=409, detail="Error al insertar el mensaje en la base de datos")
     

def select_messages_by_chat(chat_id: int, db: Session):
     return db.query(Message).filter(Message.chat_id == chat_id).all()

# Función obtener último mensaje por chat
def select_last_message_by_chat(chat_id: int, db: Session):
        last_message = db.query(Message).filter(Message.chat_id == chat_id).order_by(Message.timestamp.desc()).first()
        if not last_message:
             pass
        return last_message
