# Importaciones
from sqlalchemy.orm import Session

from persistence.repository.chat_repository import select_all_chats

# Llamadas a las funciones del repositorio
def search_all_chats(db: Session):
    return select_all_chats(db)