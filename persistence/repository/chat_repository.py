# Importaciones
from sqlalchemy.orm import Session
from persistence.model.active_chat import ActiveChat

# Función obtener rol_id
def select_all_chats(db:Session):
    return db.query(ActiveChat).all()