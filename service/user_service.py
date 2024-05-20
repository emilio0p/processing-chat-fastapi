# Importaciones
from fastapi import HTTPException
from sqlalchemy.orm import Session
from persistence.repository.user_repository import select_all_users, insert_user, select_user_by_id, update_user, delete_user
from persistence.model.user_dto import UserAddDTO
from persistence.repository.rol_repository import select_rol_name

# Llamadas a las funciones del repositorio
def search_all_users(db: Session):
    return select_all_users(db)

def save_user(user: UserAddDTO, db: Session):
    db_rol = select_rol_name("user", db)
    if not db_rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    
    return insert_user(user,db_rol.rol_id,db)

def search_user_by_id(user_id: int, db: Session):
    db_user = select_user_by_id(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return db_user 

def replace_user(user_id: int, user: UserAddDTO, db: Session):
    db_user = search_user_by_id(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return update_user(db_user, user, db)

def remove_user(user_id: int, db:Session):
    db_user = search_user_by_id(user_id, db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return delete_user(db_user, db)