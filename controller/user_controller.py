# Importaciones
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from connection.connect import get_db
from persistence.model.user import UserDTO, UserAddDTO
from service.user_service import search_all_users, save_user, replace_user, search_user_by_id

# Instanciar router Users
user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],
    responses={404: {"message": "No encontrado"}}
)

# Petición GET "/api/v1/users"
@user_router.get("/", response_model=list[UserDTO])
async def show_all_users(db: Session = Depends(get_db)):
    return search_all_users(db)

# Petición POST "/api/v1/users"
@user_router.post("/", response_model=UserDTO, status_code=status.HTTP_201_CREATED)
async def add_user(user: UserAddDTO, db: Session = Depends(get_db)):
    return save_user(user, db)

# Petición PUT "/api/v1/users/user_id"
@user_router.put("/{user_id:int}", response_model=UserDTO, status_code=status.HTTP_202_ACCEPTED)
async def edit_user(user_id: int, user: UserAddDTO, db: Session = Depends(get_db)):
    return replace_user(user_id, user, db)

# Petición GET "/api/v1/users/user_id"
@user_router.get("/{user_id:int}", response_model=UserDTO, status_code=status.HTTP_302_FOUND)
async def find_user_by_id(user_id:int, db: Session = Depends(get_db)):
    return search_user_by_id(user_id, db) 
