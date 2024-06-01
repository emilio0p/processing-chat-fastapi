# Importaciones
from fastapi import HTTPException
from sqlalchemy.orm import Session
from persistence.repository.user_repository import select_all_users, select_user_by_id, update_user, delete_user
from persistence.model.user_dto import UserAddDTO
from service.auth_service import current_user

# TODO Hacer la verificacion de los token para los endpoint privados
# Llamadas a las funciones del repositorio
def search_all_users(db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    return select_all_users(db)

def search_user_by_id(user_id: int, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    db_user = select_user_by_id(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return db_user 

def replace_user(user_id: int, user: UserAddDTO, db: Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    db_user = search_user_by_id(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return update_user(db_user, user, db)

# TODO Si al comprobar el usuario es el propio user o es de rol admin lo podra borrar, si no no
def remove_user(user_id: int, db:Session, token: str):
    user_db = current_user(db, token)
    if not user_db:
        raise HTTPException(status_code=400, detail="ERROR: El token no es válido")
    
    db_user = search_user_by_id(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return delete_user(db_user, db)