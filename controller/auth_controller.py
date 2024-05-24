# Importaciones
# Importaciones
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from connection.connect import get_db
from persistence.model.user_dto import UserDTO, UserAddDTO
from persistence.model.json_dto import JSONResp
from service.auth_service import register_user, check_login, current_user

# Instanciar router Chats
auth_router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"],
    responses={404: {"message": "No encontrado"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# Petición POST "/api/v1/auth/register"
# En el endpoint /register (En el caso local, http://localhost:8000/api/v1/auth/register)
# se ejecutará la función register si la petición es de tipo post.
# Registraremos un usuario en la bbdd.
@auth_router.post("/register", response_model=UserDTO, status_code=status.HTTP_201_CREATED)
async def register(user: UserAddDTO, db: Session=Depends(get_db)):
    try:
        return register_user(user, db)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El usuario ya existe")
    

# En el endpoint /login (En el caso local, http://localhost:8000/api/v1/auth/login)
# se ejecutará la función login si la petición es de tipo post.
# Recibiremos un usuario y una contraseña y verificaremos en la bbdd si los datos son correctos,
# devolviendo un token como respuesta.
@auth_router.post("/login", response_model=JSONResp)
async def login(form: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(get_db)):
    return check_login(form, db)


# En el endpoint /me (En el caso local, http://localhost:8000/api/v1/auth/me)
# se ejecutará la función me, que mostrará los datos del usuario logueado.
@auth_router.get("/me", response_model=UserDTO)
async def me(db: Session=Depends(get_db), token: str = Depends(oauth2)):
    return current_user(db, token)
