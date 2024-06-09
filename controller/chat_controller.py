# Importaciones
# Importaciones
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from connection.connect import get_db
from persistence.model.active_chat_dto import ActiveChatDTO, ActiveChatAddDTO
from persistence.model.form_type_dto import FormTypeDTO
from service.chat_service import search_all_chats, search_chat_by_id, save_chat, remove_chat, search_chat_by_client, search_chat_by_admin, search_form_types

# Instanciar router Chats
chat_router = APIRouter(
    prefix="/api/v1/chats",
    tags=["chats"],
    responses={404: {"message": "No encontrado"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# Petición GET "/api/v1/chats"
@chat_router.get("/",response_model=list[ActiveChatDTO])
async def show_all_chats(db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return search_all_chats(db, token)

# Petición GET "/api/v1/chats/chat_id"
@chat_router.get("/{chat_id:int}", response_model=ActiveChatDTO)
async def find_chat_by_id(chat_id:int, db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return search_chat_by_id(chat_id, db, token)

# Petición POST "/api/v1/chats"
@chat_router.post("/", status_code=201)
async def add_chat(chat: ActiveChatAddDTO, db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return save_chat(chat, db, token)

# Petición DELETE "/api/v1/chats"
@chat_router.delete("/{chat_id:int}")
async def erase_chat(chat_id:int, db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return remove_chat(chat_id, db, token)

# Petición GET "/api/v1/chats/client_id"
@chat_router.get("/client={client_id:int}", response_model=list[ActiveChatDTO])
async def find_chat_by_client(client_id:int, db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return search_chat_by_client(client_id, db, token)

# Petición GET "/api/v1/chats/client_id"
@chat_router.get("/form-types", response_model=list[FormTypeDTO])
async def find_form_types(db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return search_form_types(db, token)

# Petición GET "/api/v1/chats/admin_id"
@chat_router.get("/admin={admin_id:int}", response_model=list[ActiveChatDTO])
async def find_chat_by_admin(admin_id:int, db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return search_chat_by_admin(admin_id, db, token)