from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

from connection.connect import get_db
from persistence.model.user import User, UserDTO, UserAddDTO
from service.user_service import search_all_users, save_user

user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],
    responses={404: {"message": "Not found"}}
)

@user_router.get("/", response_model=list[UserDTO])
async def show_all_users(db: Session = Depends(get_db)):
    return search_all_users(db)

@user_router.post("/", response_model=UserDTO, status_code=status.HTTP_201_CREATED)
async def add_user(user: UserAddDTO, db: Session = Depends(get_db)):
    return save_user(user, db)