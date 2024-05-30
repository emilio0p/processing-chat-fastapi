import os
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import jwt, JWTError
from dotenv import load_dotenv  

from persistence.repository.rol_repository import select_rol_name
from persistence.repository.user_repository import insert_user, select_user_by_email 
from persistence.model.user_dto import UserAddDTO
from persistence.model.json_dto import JSONResp

#Cargamos el .env
load_dotenv()

#Tomamos el string de conexión del .env
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_DURATION = int(os.getenv("ACCESS_TOKEN_DURATION"))
SECRET = os.getenv("SECRET")

crypt = CryptContext(schemes=["bcrypt"])


def register_user(user: UserAddDTO, db: Session):
    db_rol = select_rol_name("user", db)
    user.password = crypt.hash(user.password)
    return insert_user(user, db_rol.rol_id, db)

#Método que llamará a la función search_user_by_username del servicio de usuario y lanzará
#una excepción en caso de que las contraseñas no coincidan. Finalmente, llamará a la función 
#create_access_token.
def check_login(form: OAuth2PasswordRequestForm, db: Session):
    user_db = select_user_by_email(form.username, db)
    
    if not user_db :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Credenciales incorrectas")

    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="La contraseña no es correcta")

    return create_access_token(user_db)

#Método que dado un usuario, lo codifica a JWT
def create_access_token(user_db):
    access_token = {
        "sub": str(user_db.user_id),
        "name": user_db.email,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }

    return JSONResp(access_token=jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
            token_type= "bearer")

#Método que dado un token, devuelve el usuario que representa.
def current_user(db: Session, token: str):
    try:
        jwt_user = jwt.decode(token, SECRET, algorithms=ALGORITHM)
        username = jwt_user.get("name")
        if username is None:
            raise JWTError
        user_db = select_user_by_email(username, db)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Credenciales de autenticación inválidas",
                            headers={"WWW-Authenticate": "Bearer"})
    return user_db
