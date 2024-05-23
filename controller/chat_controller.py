# Importaciones
# Importaciones
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from connection.connect import get_db
from persistence.model.active_chat_dto import ActiveChatDTO, ActiveChatAddDTO
from service.chat_service import search_all_chats, search_chat_by_id, save_chat

# Instanciar router Chats
chat_router = APIRouter(
    prefix="/api/v1/chats",
    tags=["chats"],
    responses={404: {"message": "No encontrado"}}
)

# Petición GET "/api/v1/chats"
@chat_router.get("/",response_model=list[ActiveChatDTO])
async def show_all_chats(db: Session = Depends(get_db)):
    return search_all_chats(db)

# Petición GET "/api/v1/chats/chat_id"
@chat_router.get("/{chat_id:int}", response_model=ActiveChatDTO)
async def find_chat_by_id(chat_id:int, db: Session = Depends(get_db)):
    return search_chat_by_id(chat_id, db)

# Petición POST "/api/v1/chats"
@chat_router.post("/", status_code=201)
async def add_chat(chat: ActiveChatAddDTO, db: Session = Depends(get_db)):
    return save_chat(chat, db)