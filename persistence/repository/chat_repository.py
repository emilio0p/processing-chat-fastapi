# Importaciones
from sqlalchemy.orm import Session
from persistence.model.active_chat import ActiveChat

# Función obtener todos los chats
def select_all_chats(db:Session):
    return db.query(ActiveChat).all()

# Función obtener chat por id
def select_chat_by_id(chat_id: int, db: Session):
 return db.query(ActiveChat).filter(ActiveChat.chat_id==chat_id).first()