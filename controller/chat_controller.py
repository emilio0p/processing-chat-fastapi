# Importaciones
# Importaciones
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from connection.connect import get_db
from persistence.model.active_chat_dto import ActiveChatDTO
from persistence.model.active_chat import ActiveChat

# Instanciar router Chats
chat_router = APIRouter(
    prefix="/api/v1/chats",
    tags=["chats"],
    responses={404: {"message": "No encontrado"}}
)

# Petición GET "/api/v1/chats"
@chat_router.get("/", response_model=list[ActiveChatDTO])
async def show_all_chats(db: Session = Depends(get_db)):
    return db.query(ActiveChat).all()