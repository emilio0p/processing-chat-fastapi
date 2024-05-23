# Importaciones
from sqlalchemy.orm import Session
from persistence.model.chat_status import ChatStatus

# Función obtener rol_id
def select_status_by_name(name:str, db:Session):
    return db.query(ChatStatus).filter(ChatStatus.status_name == name).first()

def select_status_by_id(id:int, db:Session):
    return db.query(ChatStatus).filter(ChatStatus.status_id == id).first()