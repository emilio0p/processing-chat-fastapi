# Importaciones
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer

from connection.connect import get_db
from persistence.model.user_dto import UserDTO, UserAddDTO
from persistence.model.user import User
from service.user_service import search_all_users, replace_user, search_user_by_id, remove_user, search_user_by_email
from persistence.model.email_check_response import EmailCheckResponse

# Instanciar router Users
user_router = APIRouter(
    prefix="/api/v1/users",
    tags=["users"],
    responses={404: {"message": "No encontrado"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# Petición GET "/api/v1/users"
@user_router.get("/", response_model=list[UserDTO])
async def show_all_users(db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return search_all_users(db, token)

# Petición PUT "/api/v1/users/user_id"
@user_router.put("/{user_id:int}", response_model=UserDTO, status_code=status.HTTP_202_ACCEPTED)
async def edit_user(user_id: int, user: UserAddDTO, db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return replace_user(user_id, user, db, token)

# Petición GET "/api/v1/users/user_id"
@user_router.get("/{user_id:int}", response_model=UserDTO)
async def find_user_by_id(user_id:int, db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return search_user_by_id(user_id, db, token)

# Petición GET "/api/v1/users/user_id"
@user_router.get("/email={email:str}", response_model=UserDTO)
async def find_user_by_email(email: str, db: Session = Depends(get_db), token: str = Depends(oauth2)):
    return search_user_by_email(email, db, token)  

# Petición DELETE "/api/v1/users/user_id"
@user_router.delete("/{user_id:int}", status_code=status.HTTP_204_NO_CONTENT)
async def erase_user(user_id: int, db:Session=Depends(get_db), token: str = Depends(oauth2)):
    remove_user(user_id, db, token)

# EXTRA
@user_router.get("/check-email", response_model=EmailCheckResponse)
def check_email_exists(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if user:
        return EmailCheckResponse(is_available=False)
    return EmailCheckResponse(is_available=True)
