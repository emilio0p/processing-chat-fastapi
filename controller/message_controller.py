# Importaciones
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from connection.connect import get_db
from persistence.model.message_dto import MessageDTO, MessageAddDTO
from service.message_service import search_all_messages, save_chat

# Instanciar router Chats
message_router = APIRouter(
    prefix="/api/v1/messages",
    tags=["messages"],
    responses={404: {"message": "No encontrado"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# En el endpoint /me (En el caso local, http://localhost:8000/api/v1/auth/me)
# se ejecutará la función me, que mostrará los datos del usuario logueado.
@message_router.get("/", response_model=list[MessageDTO])
async def show_all_messages(db: Session=Depends(get_db), token: str = Depends(oauth2)):
    return search_all_messages(db, token)

@message_router.post("/", status_code=201)
async def add_chat(message: MessageAddDTO, db:Session=Depends(get_db), token:str = Depends(oauth2)):
    return save_chat(message, db, token)